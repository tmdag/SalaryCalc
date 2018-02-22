#!/usr/bin/python
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox, QApplication, QComboBox, QMainWindow, QFrame, QLabel, QDoubleSpinBox, QGridLayout, QWidget, QAction, qApp
from PyQt5.QtGui import QIcon
from modules.taxCalculator import SimpleTax
from modules.jsonParser import jsonFile
from modules.taxEditor import Editor
import pyqtgraph as pg
from glob import glob

class Form(QMainWindow):
    def __init__ (self, parent=None):
        # super().__init__(parent) # Python => 3.0 method
        super(Form, self).__init__(parent) # Python  < 3.0 method

        self.taxfile = jsonFile("data/BCtax2018.json")
        sshFile="modules/darkorange.stylesheet"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

        self.initUI()

    def showEditor(self):
        self.edit_win = Editor(self)
        self.edit_win.show()

    def initUI(self):               
        
        exitAct = QAction(QIcon('images/exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        editAct = QAction(QIcon('images/exit.png'), '&Edit', self)        
        editAct.setShortcut('Ctrl+E')
        editAct.setStatusTip('Edit Tax Rates')
        editAct.triggered.connect(self.showEditor)

        self.statusBar()

        # ----------  Top Nenu ------------
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        taxMenu = menubar.addMenu('&Year')

        taxFiles = [file.strip("data/") for file in glob("data/BCtax*.json")]
        taxMenuEntry = {}
        for x, element in enumerate(taxFiles):
            key = 'Q'+str(x)

            taxMenuEntry[key] = QAction(element.strip(".json"), self)
            taxMenuEntry[key].setObjectName('taxYearChange')
            taxMenu.addAction(taxMenuEntry[key])
            taxMenuEntry[key].triggered.connect(lambda checked, key=key : self.updateUi(taxMenuEntry[key].text()))
        taxMenu.addAction(editAct)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.gridLayout = QGridLayout(self.central_widget)

        # ----------  Main Gui ------------

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
        self.hourlyRateBox = QDoubleSpinBox()
        self.hourlyRateBox.setRange(0, 500)
        self.hourlyRateBox.setValue(55)
        self.hourlyRateBox.setPrefix("CAD$ ")
        self.hourlyRateBox.setSuffix("/h")

        self.gridLayout.addWidget(self.hourlyRateBox, 1, 0, 1, 1)
        self.annualRateBox = QDoubleSpinBox()
        self.annualRateBox.setRange(4000, 500000)
        self.annualRateBox.setValue(114400)
        self.annualRateBox.setSingleStep(10000)

        self.annualRateBox.setProperty("showGroupSeparator", True)
        self.annualRateBox.setPrefix("CAD$ ")
        self.annualRateBox.setSuffix("/y")

        self.gridLayout.addWidget(self.annualRateBox, 1, 1, 1, 1)
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
        self.commentary = QLabel("")
        self.commentary.setFrameShape(QFrame.StyledPanel)
        self.commentary.setFrameShadow(QFrame.Sunken)
        self.commentary.setLineWidth(1)
        self.commentary.setMaximumSize(QtCore.QSize(16777215, 22))
        cfont = self.commentary.font()
        cfont.setPointSize(8)
        self.commentary.setFont(cfont)

        self.plotgraph = pg.PlotWidget()        
        self.bpen=pg.mkPen('b', width=1)
        self.rpen=pg.mkPen('r', width=1)
        self.plotgraph.showGrid(False, True, 0.4)
        self.plotgraph.setMaximumSize(QtCore.QSize(1600, 300))
        self.gridLayout.addWidget(self.plotgraph, 6, 0, 1, 2)

        self.gridLayout.addWidget(self.commentary, 7, 0, 1, 2)
        self.hourlyRateBox.valueChanged.connect(self.updateUi)
        self.annualRateBox.valueChanged.connect(self.updateUi)
        self.sFreq.currentIndexChanged.connect(self.updateUi)
        self.setWindowTitle("VFX Salary Conversion 2018")
        self.updateUi("BCtax2018")

    def updateUi(self, taxyear):
        _translate = QtCore.QCoreApplication.translate #copied from QT Designer
        senderNode = self.sender() # Check which spinbox requested update
            
        # check desired frequency (weekly or biweekly)
        salaryFreqBox = str(self.sFreq.currentText())

        if(salaryFreqBox=="Net weekly"):
            self.weeks = 52.0
        else:
            self.weeks = 26.0

        if senderNode is self.hourlyRateBox: 
            # if hourly rate spinbox requested update
            hr = self.hourlyRateBox.value()
            ann = hr*2080.0
            self.annualRateBox.setValue(ann)

        elif senderNode is self.annualRateBox:
            # if annual rate spinbox requested update
            ann = self.annualRateBox.value()
            hr = ann/2080.0
            self.hourlyRateBox.setValue(hr)
        else:
            # if update came from UI inicialization OR sFreq (weekly/biweekly)
            hr = self.hourlyRateBox.value()
            ann = hr*2080.0


        # read json with data from specific Province/year

        if(senderNode != None and senderNode.objectName() == "taxYearChange"):
            self.taxfile = jsonFile("data/{}.json".format(taxyear))
            self.setWindowTitle("VFX Salary Conversion {}".format(taxyear.strip("BCtax")))

        taxdata = self.taxfile.load()
        # pass tax data to SimpleTax module
        calcTax = SimpleTax(ann, taxdata)
        salaryFrequency = calcTax.afterTax()/self.weeks

        self.totalTaxOut.setText(_translate("Dialog", "Total tax : $ {0:,.1f}/y".format(calcTax.taxDue())))
        self.netPayOut.setText(_translate("Dialog", "Net Pay : $ {:,.1f}/y".format(calcTax.afterTax())))
        self.salaryOut.setText(_translate("Dialog", "CAD$ {:,.1f}".format(salaryFrequency)))

        # GRAPH -------------------------------------------------------------------------
        dph = []
        npb = []
        for x in range(0,300):
            dph.append(x)
            npb.append(SimpleTax(x*2080, taxdata).afterTax()/self.weeks)

        self.plotgraph.clear()
        plotXrange = 500
        plotYrange = 10
        # self.plotgraph.addLegend()
        self.plotgraph.setXRange((salaryFrequency)-plotXrange, (salaryFrequency)+plotXrange, padding=0)
        self.plotgraph.setYRange(hr-plotYrange, hr+plotYrange, padding=0)
        self.plotgraph.plot(y=dph, x=npb, pen='#2196F3',clear=True, name='bi-weekly net pay')
        self.plotgraph.plot(y=[hr], x=[salaryFrequency], pen=None, symbol='+', size=15, name='current CAD per hour')
        self.plotgraph.addLine(x=salaryFrequency, pen=self.rpen)
        self.text = pg.TextItem("${:,.1f}".format(salaryFrequency), anchor=(-0.1, -0.05))
        self.text.setPos(salaryFrequency, hr)
        self.plotgraph.addItem(self.text)

        # END GRAPH ----------------------------------------------------------------------

        if hr<=20:
            comment = "runner salary"
        elif hr>20 and hr<=30:
            comment = "Coordinator"
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

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())