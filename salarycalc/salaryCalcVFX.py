#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Small tool calculating BC Net Pay based on hour/annual rate with graphing capabilities
'''
from glob import glob
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow, QFrame, QLabel, QDoubleSpinBox, QGridLayout, QWidget, QAction, qApp
from PyQt5.QtGui import QIcon
from modules import SimpleTax
from modules import JsonFile
from taxEditor import Editor
import pyqtgraph as pg

class MainUI(QMainWindow):
    ''' Whole code dumped into PyQT class '''
    def __init__(self, parent=None):
        super().__init__(parent) # Python => 3.0 method\
        # super(MainUI, self).__init__(parent) # Python  < 3.0 method

        self.taxyear = "BCtax2018"

        # load and set stylesheet look
        style_file = "modules/darkorange.stylesheet"
        with open(style_file, "r") as sfile:
            self.setStyleSheet(sfile.read())

        # store window dimensions so that we can open editor next to it
        # winW = self.frameGeometry().width()
        # winH = self.frameGeometry().height()

        # kick off init of main window
        self.initUI()

    def show_editor(self, taxyear=None):
        ''' QT signal connector, when editor is called from top menu '''
        self.edit_win = Editor(taxyear)
        self.edit_win.show()

    def update_tax(self, taxyear):
        ''' QT signal connector '''
        self.taxyear = taxyear
        self.setWindowTitle("VFX Salary Conversion {}".format(taxyear))
        self.updateUi()

    def top_menu(self):
        """ Top menu as aseparate method, so it's easy to maintain and find it"""
        exit_action = QAction(QIcon('images/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        edit_action = QAction(QIcon('images/exit.png'), '&Edit', self)
        edit_action.setShortcut('Ctrl+E')
        edit_action.setStatusTip('Edit Tax Rates')
        edit_action.triggered.connect(lambda: self.show_editor(self.taxyear))

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        tax_menu = menubar.addMenu('&Year')

        tax_files = [file.strip("data/") for file in glob("data/*tax*.json")]
        tax_menu_entry = {}
        for pos, element in enumerate(tax_files):
            key = 'Q'+str(pos)

            tax_menu_entry[key] = QAction(element.strip(".json"), self)
            tax_menu_entry[key].setObjectName('taxYearChange')
            tax_menu.addAction(tax_menu_entry[key])
            tax_menu_entry[key].triggered.connect(lambda checked, key=key: self.update_tax(tax_menu_entry[key].text()))
        tax_menu.addAction(edit_action)

    def initUI(self):
        ''' Main UI initializatin '''
        self.statusBar()
        self.top_menu()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        self.hourly_label = QLabel(" per hour")
        hourly_label_font = self.hourly_label.font()
        hourly_label_font.setPointSize(8)
        self.hourly_label.setFont(hourly_label_font)
        self.grid_layout.addWidget(self.hourly_label, 0, 0, 1, 1)

        self.annual_label = QLabel(" per year")
        annual_label_font = self.annual_label.font()
        annual_label_font.setPointSize(8)
        self.annual_label.setFont(annual_label_font)
        self.grid_layout.addWidget(self.annual_label, 0, 1, 1, 1)

        self.hourly_rate_box = QDoubleSpinBox()
        self.hourly_rate_box.setRange(0, 500)
        self.hourly_rate_box.setValue(55)
        self.hourly_rate_box.setPrefix("CAD$ ")
        self.hourly_rate_box.setSuffix("/h")

        self.grid_layout.addWidget(self.hourly_rate_box, 1, 0, 1, 1)
        self.annual_rate_box = QDoubleSpinBox()
        self.annual_rate_box.setRange(4000, 500000)
        self.annual_rate_box.setValue(114400)
        self.annual_rate_box.setSingleStep(10000)

        self.annual_rate_box.setProperty("showGroupSeparator", True)
        self.annual_rate_box.setPrefix("CAD$ ")
        self.annual_rate_box.setSuffix("/y")

        self.grid_layout.addWidget(self.annual_rate_box, 1, 1, 1, 1)
        self.totalTaxOut = QLabel("totalTaxOut")
        self.totalTaxOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        totalTaxOutFont = self.totalTaxOut.font()
        totalTaxOutFont.setPointSize(10)
        self.totalTaxOut.setFont(totalTaxOutFont)

        self.grid_layout.addWidget(self.totalTaxOut, 2, 1, 1, 1)
        self.netPayOut = QLabel("netPayOut")
        self.netPayOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        netPayOutFont = self.netPayOut.font()
        netPayOutFont.setPointSize(10)
        self.netPayOut.setFont(netPayOutFont)

        self.grid_layout.addWidget(self.netPayOut, 3, 1, 1, 1)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.grid_layout.addWidget(self.line, 4, 0, 1, 2)
        self.sFreq = QComboBox()
        self.sFreq.addItems(["Net bi-weekly", "Net weekly"])

        self.grid_layout.addWidget(self.sFreq, 5, 0, 1, 1)
        self.salaryOut = QLabel()
        self.salaryOut.setFrameShape(QFrame.Panel)
        self.salaryOut.setFrameShadow(QFrame.Sunken)
        self.salaryOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.grid_layout.addWidget(self.salaryOut, 5, 1, 1, 1)
        self.commentary = QLabel("")
        self.commentary.setFrameShape(QFrame.StyledPanel)
        self.commentary.setFrameShadow(QFrame.Sunken)
        self.commentary.setLineWidth(1)
        self.commentary.setMaximumSize(QtCore.QSize(16777215, 22))
        cfont = self.commentary.font()
        cfont.setPointSize(8)
        self.commentary.setFont(cfont)

        self.plotgraph = pg.PlotWidget()
        self.bpen = pg.mkPen('b', width=1)
        self.rpen = pg.mkPen('r', width=1)
        self.plotgraph.showGrid(False, True, 0.4)
        self.plotgraph.setMaximumSize(QtCore.QSize(1600, 300))
        self.grid_layout.addWidget(self.plotgraph, 6, 0, 1, 2)

        self.grid_layout.addWidget(self.commentary, 7, 0, 1, 2)
        self.hourly_rate_box.valueChanged.connect(self.updateUi)
        self.annual_rate_box.valueChanged.connect(self.updateUi)
        self.sFreq.currentIndexChanged.connect(self.updateUi)
        self.setWindowTitle("VFX Salary Conversion {}".format(self.taxyear))

        self.updateUi()

    def updateUi(self):
        _translate = QtCore.QCoreApplication.translate #copied from QT Designer
        senderNode = self.sender() # Check which spinbox requested update

        # check desired frequency (weekly or biweekly)
        salaryFreqBox = str(self.sFreq.currentText())

        if salaryFreqBox == "Net weekly":
            self.weeks = 52.0
        else:
            self.weeks = 26.0

        if senderNode is self.hourly_rate_box:
            # if hourly rate spinbox requested update
            hr = self.hourly_rate_box.value()
            ann = hr*2080.0
            self.annual_rate_box.setValue(ann)

        elif senderNode is self.annual_rate_box:
            # if annual rate spinbox requested update
            ann = self.annual_rate_box.value()
            hr = ann/2080.0
            self.hourly_rate_box.setValue(hr)
        else:
            # if update came from UI inicialization OR sFreq (weekly/biweekly)
            hr = self.hourly_rate_box.value()
            ann = hr*2080.0


        # read json with data from specific Province/year
        self.taxfile = JsonFile("data/{}.json".format(self.taxyear))
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
        for x in range(0, 300):
            dph.append(x)
            npb.append(SimpleTax(x*2080, taxdata).afterTax()/self.weeks)

        self.plotgraph.clear()
        plotXrange = 500
        plotYrange = 10
        # self.plotgraph.addLegend()
        self.plotgraph.setXRange((salaryFrequency)-plotXrange, (salaryFrequency)+plotXrange, padding=0)
        self.plotgraph.setYRange(hr-plotYrange, hr+plotYrange, padding=0)
        self.plotgraph.plot(y=dph, x=npb, pen='#2196F3', clear=True, name='bi-weekly net pay')
        self.plotgraph.plot(y=[hr], x=[salaryFrequency], pen=None, symbol='+', size=15, name='current CAD per hour')
        self.plotgraph.addLine(x=salaryFrequency, pen=self.rpen)
        self.text = pg.TextItem("${:,.1f}".format(salaryFrequency), anchor=(-0.1, -0.05))
        self.text.setPos(salaryFrequency, hr)
        self.plotgraph.addItem(self.text)

        # END GRAPH ----------------------------------------------------------------------

        if hr <= 20:
            comment = "runner salary"
        elif hr > 20 and hr <= 30:
            comment = "Coordinator"
        elif hr > 30 and hr <= 40:
            comment = "Junior Artist salary"
        elif hr > 40 and hr <= 50:
            comment = "Mid Artist salary"
        elif hr > 50 and hr <= 65:
            comment = "Senior Artist salary"
        elif hr > 65 and hr <= 85:
            comment = "Supervisor salary"
        elif hr > 85:
            comment = "Mid at Weta or senior Sup in Canada"
        self.commentary.setText("{}".format(comment))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainUI = MainUI()
    MainUI.show()
    sys.exit(app.exec_())
