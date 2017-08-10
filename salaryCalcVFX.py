#!/usr/bin/python3

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox, QApplication, QComboBox, QDialog, QFrame, QLabel, QSpinBox, QGridLayout
from taxCalculator import SimpleTax
from jsonParser import jsonFile

class Form(QDialog):
	def __init__ (self, parent=None):
		super().__init__(parent)
		self.gridLayout = QGridLayout()
		self.hourlyLabel = QLabel(" per hour")
		hourlyLabelFont = self.hourlyLabel.font()
		hourlyLabelFont.setPointSize(8)
		self.hourlyLabel.setFont(hourlyLabelFont)

		self.gridLayout.addWidget(self.hourlyLabel, 0, 0, 1, 1)
		self.annualLabel = QLabel(" per year") 
		annualLabelFont = self.annualLabel.font()
		annualLabelFont.setPointSize(8)
		self.annualLabel.setFont(annualLabelFont)

		self.gridLayout.addWidget(self.annualLabel, 0, 1, 1, 1)
		self.hourlyRate = QSpinBox()
		self.hourlyRate.setRange(15, 500)
		self.hourlyRate.setValue(55)
		self.hourlyRate.setPrefix("CAD$ ")
		self.hourlyRate.setSuffix("/h")
		self.gridLayout.addWidget(self.hourlyRate, 1, 0, 1, 1)
		self.annualRate = QSpinBox()
		self.annualRate.setRange(40000, 500000)
		self.annualRate.setValue(114400)
		self.annualRate.setProperty("showGroupSeparator", True)
		self.annualRate.setPrefix("CAD$ ")
		self.annualRate.setSuffix("/y")
		self.gridLayout.addWidget(self.annualRate, 1, 1, 1, 1)
		self.totalTaxOut = QLabel("totalTaxOut")
		self.totalTaxOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		totalTaxOutFont = self.totalTaxOut.font()
		totalTaxOutFont.setPointSize(10)
		self.totalTaxOut.setFont(totalTaxOutFont)

		self.gridLayout.addWidget(self.totalTaxOut, 2, 1, 1, 1)
		self.netPayOut = QLabel("netPayOut")
		self.netPayOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		netPayOutFont = self.netPayOut.font()
		netPayOutFont.setPointSize(10)
		self.netPayOut.setFont(netPayOutFont)

		self.gridLayout.addWidget(self.netPayOut, 3, 1, 1, 1)
		self.line = QFrame()
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)
		self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
		self.sFreq = QComboBox()
		self.sFreq.addItems(["Net bi-weekly", "Net weekly"])
		self.gridLayout.addWidget(self.sFreq, 5, 0, 1, 1)
		self.salaryOut = QLabel()
		self.salaryOut.setFrameShape(QFrame.Panel)
		self.salaryOut.setFrameShadow(QFrame.Sunken)
		self.salaryOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.salaryOut, 5, 1, 1, 1)
		# self.buttonBox = QDialogButtonBox()
		# self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		# self.buttonBox.setStandardButtons(QDialogButtonBox.Close)#|QDialogButtonBox.Ok)
		# self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
		self.commentary = QLabel("")
		self.commentary.setFrameShape(QFrame.StyledPanel)
		self.commentary.setFrameShadow(QFrame.Sunken)
		self.commentary.setLineWidth(1)
		self.commentary.setMaximumSize(QtCore.QSize(16777215, 22))
		cfont = self.commentary.font()
		cfont.setPointSize(8)
		self.commentary.setFont(cfont)
		self.gridLayout.addWidget(self.commentary, 6, 0, 1, 2)
		self.setLayout(self.gridLayout)
		self.hourlyRate.valueChanged.connect(self.updateUi)
		self.annualRate.valueChanged.connect(self.updateUi)
		self.sFreq.currentIndexChanged.connect(self.updateUi)
		self.setWindowTitle("VFX Salary Conversion")
		self.updateUi()

	def updateUi(self):
		_translate = QtCore.QCoreApplication.translate #copied from QT Designer
		sbox = self.sender() #Check which spinbox requested update

		if sbox is self.hourlyRate: 
			#if hourly rate spinbox requested update
			hr = self.hourlyRate.value()
			ann = hr*2080
			self.annualRate.setValue(ann)

		elif sbox is self.annualRate:
			#if annual rate spinbox requested update
			ann = self.annualRate.value()
			hr = ann/2080
			self.hourlyRate.setValue(hr)
		else:
			#if update came from UI inicialization
			hr = self.hourlyRate.value()
			ann = hr*2080

		taxfile = jsonFile("BCtax2017.json")
		taxdata = taxfile.load()

		salaryFreq = str(self.sFreq.currentText())
		calcTax = SimpleTax(ann, taxdata)

		self.totalTaxOut.setText(_translate("Dialog", "Total tax : $ {0:,.1f}/y".format(calcTax.taxDue())))
		self.netPayOut.setText(_translate("Dialog", "Net Pay : $ {:,.1f}/y".format(calcTax.afterTax())))
		if(salaryFreq=="Net weekly"):
			self.salaryOut.setText(_translate("Dialog", "CAD$ {:,.1f}".format(calcTax.afterTax()/52)))
		else:
			self.salaryOut.setText(_translate("Dialog", "CAD$ {:,.1f}".format(calcTax.afterTax()/26)))

		if hr<=30:
			comment = "runner salary"
		elif hr>30 and hr<=40:
			comment = "Junior Artist salary"
		elif hr>40 and hr<=50:
			comment = "Mid Artist salary"
		elif hr>50 and hr<=65:
			comment = "Senior Artist salary"
		elif hr>65 and hr<=85:
			comment = "Supervisor salary"
		elif hr>85:
			comment = "Mid at Weta or senior Sup in Canada"
		self.commentary.setText("{}".format(comment))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()