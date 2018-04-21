from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableView, QMessageBox, QMainWindow, QApplication, QWidget, QVBoxLayout, qApp, QSplitter, QLabel, QSizePolicy, QComboBox, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QMenuBar, QMenu, QStatusBar, QAction, QFileDialog
from modules import jsonFile
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/data"

class Editor(QMainWindow):
    def __init__ (self, taxfile=None, parent=None):
        # super().__init__(parent) # Python => 3.0 method
        super(Editor, self).__init__(parent) # Python  < 3.0 method

        # load and set stylesheet look
        sshFile="modules/darkorange.stylesheet"
        with open(sshFile,"r") as fh:
            self.mystyle = fh.read()
            self.setStyleSheet(self.mystyle)

        self.move(710,0)

        if(taxfile != None):
            self.taxyear = taxfile
        else:
            self.taxyear = "BCtax2018"

        self.initUI(self.taxyear)

    def openFile(self):
        fname, _filter = QFileDialog.getOpenFileName(self, 'Open json file', DATA_DIR ,"Json file (*.json)")
        if(fname!=''):
            jsonTaxFile = fname.split("/")[-1:][0]
            self.updateTax(jsonTaxFile.split(".")[0])

    def saveFile(self):
        data = self.readData()
        fname = "{}tax{}.json".format(data['info']['prov'], data['info']['year'])
        sname = DATA_DIR + "/{}".format(fname)
        if os.path.isfile(sname):
            msgBox = QMessageBox() ;
            msgBox.setStyleSheet(self.mystyle)
            buttonReply = msgBox.question(self, 'File Exists', "Do you want overwrite {}?".format(fname), QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if buttonReply == QMessageBox.Yes:
                jsonFile(sname).save(data)
            if buttonReply == QMessageBox.Cancel:
                print('Cancel')
        else:
            jsonFile(sname).save(data)

    def saveFileAs(self):
        data = self.readData()
        sname, _filter  = QFileDialog.getSaveFileName(self, 'Save json File',DATA_DIR,"Json file (*.json)")
        if(sname!=''):
            jsonFile(sname).save(data)

    def updateTax(self, taxyear):
        self.taxyear = taxyear
        self.setWindowTitle("Editing {}".format(taxyear))
        self.fillData(taxyear)

    def loadData(self, taxyear):
        taxdata = jsonFile("data/{}.json".format(taxyear))
        return taxdata.load()

    def initMenu(self):
        self.menubar = QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setTitle("File")

        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionOpen = QAction()
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openFile)
        self.actionOpen.setText("Open")

        self.actionSave = QAction()
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave.setText("Save")

        self.actionSaveAs = QAction()
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSaveAs.triggered.connect(self.saveFileAs)
        self.actionSaveAs.setText("Save As..")

        self.actionExit = QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(qApp.quit)
        self.actionExit.setText("Exit")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

    def initUI(self, taxyear):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(400, 800)

        self.centralwidget = QWidget()
        # self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        # self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        # self.splitter.setOrientation(QtCore.Qt.Horizontal)
        # self.splitter.setObjectName("splitter")

        # --------------------- TOP MENU -------------------------

        self.initMenu()

        # ------------- Province ----------------
        self.ProvinceLabel = QLabel(self.splitter)
        # sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.ProvinceLabel.sizePolicy().hasHeightForWidth())
        # self.ProvinceLabel.setSizePolicy(sizePolicy)
        # self.ProvinceLabel.setMaximumSize(QtCore.QSize(80, 30))
        # self.ProvinceLabel.setObjectName("ProvinceLabel")
        self.provinceBox = QComboBox(self.splitter)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.provinceBox.sizePolicy().hasHeightForWidth())
        # self.provinceBox.setSizePolicy(sizePolicy)
        # self.provinceBox.setMaximumSize(QtCore.QSize(200, 16777215))
        # self.provinceBox.setObjectName("provinceBox")
        self.provinceBox.addItem("Alberta")
        self.provinceBox.setItemText(0, "AB")

        self.provinceBox.addItem("British Columbia")
        self.provinceBox.setItemText(1, "BC")

        self.provinceBox.addItem("Manitoba")
        self.provinceBox.setItemText(2, "MB")

        self.provinceBox.addItem("New Brunswick")
        self.provinceBox.setItemText(3, "NB")

        self.provinceBox.addItem("Newfoundland and Labrador")
        self.provinceBox.setItemText(4, "NL")

        self.provinceBox.addItem("Nova Scotia")
        self.provinceBox.setItemText(5, "NS")

        self.provinceBox.addItem("Nunavut")
        self.provinceBox.setItemText(6, "BC")

        self.provinceBox.addItem("Ontario")
        self.provinceBox.setItemText(7, "ON")

        self.provinceBox.addItem("Prince Edward Island")
        self.provinceBox.setItemText(8, "PE")

        self.provinceBox.addItem("Quebec")
        self.provinceBox.setItemText(9, "QC")

        self.provinceBox.addItem("Saskatchewan")
        self.provinceBox.setItemText(10, "SK")

        self.taxYearLabel = QLabel(self.splitter)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.taxYearLabel.sizePolicy().hasHeightForWidth())
        # self.taxYearLabel.setSizePolicy(sizePolicy)
        # self.taxYearLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        # self.taxYearLabel.setObjectName("taxYearLabel")
        self.taxYearBox = QSpinBox(self.splitter)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.taxYearBox.sizePolicy().hasHeightForWidth())

        # self.taxYearBox.setSizePolicy(sizePolicy)
        # self.taxYearBox.setMaximumSize(QtCore.QSize(150, 16777215))
        # self.taxYearBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.taxYearBox.setAutoFillBackground(False)
        self.taxYearBox.setMinimum(1990)
        self.taxYearBox.setMaximum(2050)
        # self.taxYearBox.setProperty("value", 2018)
        self.taxYearBox.setValue(2018)
        # self.taxYearBox.setObjectName("taxYearBox")





        self.verticalLayout_3.addWidget(self.splitter)
        self.tabWidget = QTabWidget(self.centralwidget)
        # self.tabWidget.setTabPosition(QTabWidget.North)
        # self.tabWidget.setTabShape(QTabWidget.Rounded)
        # self.tabWidget.setDocumentMode(False)
        # self.tabWidget.setTabsClosable(False)
        # self.tabWidget.setObjectName("tabWidget")
        self.ProvincialTab = QWidget()
        # self.ProvincialTab.setObjectName("ProvincialTab")
        self.verticalLayout = QVBoxLayout(self.ProvincialTab)
        # self.verticalLayout.setObjectName("verticalLayout")
        self.provLabel = QLabel(self.ProvincialTab)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.provLabel.sizePolicy().hasHeightForWidth())
        # self.provLabel.setSizePolicy(sizePolicy)
        # self.provLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.provLabel.setObjectName("provLabel")
        self.verticalLayout.addWidget(self.provLabel)




        # ---------- PROVINCIAL TABLE ---------------
        # self.provTable = QTableView(self.ProvincialTab)
        self.provTable = QTableWidget(self.ProvincialTab)
        # self.provTable.setModel(QtCore.QAbstractTableModel)
        # self.provTable.setEnabled(True)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.provTable.sizePolicy().hasHeightForWidth())
        # self.provTable.setSizePolicy(sizePolicy)
        # self.provTable.setAcceptDrops(True)
        # self.provTable.setAutoFillBackground(False)
        # self.provTable.setGridStyle(QtCore.Qt.SolidLine)
        # self.provTable.setObjectName("provTable")
        self.provTable.setColumnCount(3)
        self.provTable.setRowCount(6)

        font = QtGui.QFont()
        font.setPointSize(9)
 
        item = QTableWidgetItem()
        self.provTable.setHorizontalHeaderItem(0, item)
        self.provTable.horizontalHeaderItem(0).setText("Bracket From")
        self.provTable.horizontalHeaderItem(0).setFont(font)

        item = QTableWidgetItem()
        self.provTable.setHorizontalHeaderItem(1, item)
        self.provTable.horizontalHeaderItem(1).setText("Bracket To")
        self.provTable.horizontalHeaderItem(1).setFont(font)

        item = QTableWidgetItem()
        self.provTable.setHorizontalHeaderItem(2, item)
        self.provTable.horizontalHeaderItem(2).setText("tax Rate")
        self.provTable.horizontalHeaderItem(2).setFont(font)


        # self.provTable.horizontalHeader().setVisible(True)
        # self.provTable.horizontalHeader().setCascadingSectionResizes(False)
        self.provTable.horizontalHeader().setDefaultSectionSize(110)
        self.provTable.horizontalHeader().setStretchLastSection(True)
        self.provTable.verticalHeader().setVisible(False)
        # self.provTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.provTable)
        self.provPerLabel = QLabel(self.ProvincialTab)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.provPerLabel.sizePolicy().hasHeightForWidth())
        # self.provPerLabel.setSizePolicy(sizePolicy)
        # self.provPerLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.provPerLabel.setObjectName("provPerLabel")
        self.verticalLayout.addWidget(self.provPerLabel)




        # ----------- PROVINCE PERSONAL -------------------

        self.provPerTable = QTableWidget(self.ProvincialTab)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.provPerTable.sizePolicy().hasHeightForWidth())
        # self.provPerTable.setSizePolicy(sizePolicy)
        self.provPerTable.setMaximumSize(QtCore.QSize(16777215, 60))
        self.provPerTable.setRowCount(1)
        self.provPerTable.setColumnCount(2)
        self.provPerTable.setObjectName("provPerTable")
        item = QTableWidgetItem()
        self.provPerTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.provPerTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.provPerTable.setHorizontalHeaderItem(1, item)
        self.provPerTable.horizontalHeader().setDefaultSectionSize(180)
        self.provPerTable.horizontalHeader().setStretchLastSection(True)
        self.provPerTable.verticalHeader().setVisible(False)
        self.provPerTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.provPerTable)


        self.tabWidget.addTab(self.ProvincialTab, "")
        self.FederalTab = QWidget()
        self.FederalTab.setObjectName("FederalTab")
        self.verticalLayout_2 = QVBoxLayout(self.FederalTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fedLabel = QLabel(self.FederalTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fedLabel.sizePolicy().hasHeightForWidth())
        self.fedLabel.setSizePolicy(sizePolicy)
        self.fedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fedLabel.setObjectName("fedLabel")
        self.verticalLayout_2.addWidget(self.fedLabel)

        # ----------- FEDERAL TABLE -----------------

        self.fedTable = QTableWidget(self.FederalTab)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.fedTable.sizePolicy().hasHeightForWidth())
        # self.fedTable.setSizePolicy(sizePolicy)
        # self.fedTable.setMinimumSize(QtCore.QSize(0, 0))
        # self.fedTable.setObjectName("fedTable")
        self.fedTable.setColumnCount(3)
        self.fedTable.setRowCount(5)

        font = QtGui.QFont()
        font.setPointSize(9)

        item = QTableWidgetItem()
        self.fedTable.setHorizontalHeaderItem(0, item)
        self.fedTable.horizontalHeaderItem(0).setText("Bracket From")
        self.fedTable.horizontalHeaderItem(0).setFont(font)

        item = QTableWidgetItem()
        self.fedTable.setHorizontalHeaderItem(1, item)
        self.fedTable.horizontalHeaderItem(1).setText("Bracket To")
        self.fedTable.horizontalHeaderItem(1).setFont(font)

        item = QTableWidgetItem()
        self.fedTable.setHorizontalHeaderItem(2, item)
        self.fedTable.horizontalHeaderItem(2).setText("tax Rate")
        self.fedTable.horizontalHeaderItem(2).setFont(font)

        self.fedTable.horizontalHeader().setDefaultSectionSize(100)
        self.fedTable.horizontalHeader().setStretchLastSection(True)
        self.fedTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.fedTable)

        self.fedPerLabel = QLabel(self.FederalTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fedPerLabel.sizePolicy().hasHeightForWidth())
        self.fedPerLabel.setSizePolicy(sizePolicy)
        self.fedPerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fedPerLabel.setObjectName("fedPerLabel")
        self.verticalLayout_2.addWidget(self.fedPerLabel)




        # ----------- FEDERAL PERSONAL TABLE -----------------


        self.fedPerTable = QTableWidget(self.FederalTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fedPerTable.sizePolicy().hasHeightForWidth())
        self.fedPerTable.setSizePolicy(sizePolicy)
        self.fedPerTable.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fedPerTable.setRowCount(1)
        self.fedPerTable.setColumnCount(2)
        self.fedPerTable.setObjectName("fedPerTable")
        item = QTableWidgetItem()
        self.fedPerTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.fedPerTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.fedPerTable.setHorizontalHeaderItem(1, item)
        self.fedPerTable.horizontalHeader().setDefaultSectionSize(180)
        self.fedPerTable.horizontalHeader().setStretchLastSection(True)
        self.fedPerTable.verticalHeader().setVisible(False)
        self.fedPerTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.fedPerTable)
        self.tabWidget.addTab(self.FederalTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)



        self.eiLabel = QLabel(self.centralwidget)
        self.eiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eiLabel.setObjectName("eiLabel")
        self.verticalLayout_3.addWidget(self.eiLabel)
        self.eiTable = QTableWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eiTable.sizePolicy().hasHeightForWidth())
        self.eiTable.setSizePolicy(sizePolicy)
        self.eiTable.setMaximumSize(QtCore.QSize(16777215, 60))
        self.eiTable.setObjectName("eiTable")
        self.eiTable.setColumnCount(2)
        self.eiTable.setRowCount(1)
        item = QTableWidgetItem()
        self.eiTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.eiTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.eiTable.setHorizontalHeaderItem(1, item)
        self.eiTable.horizontalHeader().setDefaultSectionSize(180)
        self.eiTable.horizontalHeader().setStretchLastSection(True)
        self.eiTable.verticalHeader().setVisible(False)
        self.eiTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.eiTable)

        self.cppLabel = QLabel(self.centralwidget)
        self.cppLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cppLabel.setObjectName("cppLabel")
        self.cppLabel.setText("Canada Pension Plan")

        self.verticalLayout_3.addWidget(self.cppLabel)
        self.cppTable = QTableWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cppTable.sizePolicy().hasHeightForWidth())
        self.cppTable.setSizePolicy(sizePolicy)
        self.cppTable.setMaximumSize(QtCore.QSize(16777215, 60))
        self.cppTable.setObjectName("cppTable")
        self.cppTable.setColumnCount(3)
        self.cppTable.setRowCount(1)
        item = QTableWidgetItem()
        self.cppTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.cppTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()



        self.cppTable.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.cppTable.setHorizontalHeaderItem(2, item)
        self.cppTable.horizontalHeader().setDefaultSectionSize(120)
        self.cppTable.horizontalHeader().setStretchLastSection(True)
        self.cppTable.verticalHeader().setVisible(False)
        self.cppTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.cppTable)
        self.setCentralWidget(self.centralwidget)

 
        item = self.cppTable.horizontalHeaderItem(0)
        item.setText("max contrib")
        item = self.cppTable.horizontalHeaderItem(1)
        item.setText("tax")
        item = self.cppTable.horizontalHeaderItem(2)
        item.setText("excempt")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        # QtCore.QMetaObject.connectSlotsByName()
        self.setWindowTitle("Editing {}".format(taxyear))
        self.fillData(taxyear)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ProvinceLabel.setText(_translate("MainWindow", "Province"))
        self.taxYearLabel.setText(_translate("MainWindow", "Tax Year"))
        self.provLabel.setText(_translate("MainWindow", "Provincial Tax Rates, Personal income"))

        self.provPerLabel.setText(_translate("MainWindow", "Personal Amount"))
        item = self.provPerTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.provPerTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "amount"))
        item = self.provPerTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tax rate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProvincialTab), _translate("MainWindow", "Provincial Tax"))
        self.fedLabel.setText(_translate("MainWindow", "Federal Tax Rates"))

        self.fedPerLabel.setText(_translate("MainWindow", "Personal Amount"))
        item = self.fedPerTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.fedPerTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "amount"))
        item = self.fedPerTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tax rate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FederalTab), _translate("MainWindow", "Federal Tax"))
        self.eiLabel.setText(_translate("MainWindow", "Employee Insurance"))
        item = self.eiTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee Insurance"))
        item = self.eiTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "maxei"))
        item = self.eiTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tax"))

    def readData(self):
        taxdata = {}

        taxdata['info'] = {}
        taxdata['info']['year'] = self.taxYearBox.value()
        taxdata['info']['prov'] = self.provinceBox.currentText()

        taxdata['province'] = {}
        for i in range(0,6):
            taxdata['province']['brk{}'.format(i+1)] = [float(self.provTable.item(i, c).text()) for c in range(3)]

        taxdata['province']['PersonalAmount'] = [float(self.provPerTable.item(0, c).text()) for c in range(2)]

        taxdata['federal'] = {}
        for i in range(0,5):
            taxdata['federal']['brk{}'.format(i+1)] = [float(self.fedTable.item(i, c).text()) for c in range(3)]

        taxdata['federal']['PersonalAmount'] = [float(self.fedPerTable.item(0, c).text()) for c in range(2)]
        taxdata['employeeInsurance'] = {}
        taxdata['employeeInsurance']['maxei'] = [float(self.eiTable.item(0, c).text()) for c in range(2)]

        taxdata['cpp'] = {}
        taxdata['cpp']['maxcppContrib'] = [float(self.cppTable.item(0, c).text()) for c in range(2)]
        taxdata['cpp']['cppExempt'] = float(self.cppTable.item(0, 2).text())

        return taxdata

    def fillData(self, taxyear):
        taxdata = self.loadData(taxyear)

        year = taxdata['info']['year']
        print(year)
        self.taxYearBox.setValue(year)

        prov = taxdata['info']['prov']
        index = self.provinceBox.findText(prov, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.provinceBox.setCurrentIndex(index)

        self.prov_brk = [taxdata['province']['brk{}'.format(x)] for x in range(1,7)]
        self.prov_PersonalAmount = taxdata['province']['PersonalAmount']
        self.federal_brk = [taxdata['federal']['brk{}'.format(x)] for x in range(1,6)]
        self.federal_PersonalAmount = taxdata['federal']['PersonalAmount']
        self.maxei = taxdata['employeeInsurance']['maxei']
        self.maxcppContrib = taxdata['cpp']['maxcppContrib']
        self.cppExempt = taxdata['cpp']['cppExempt']

        for c in range(0, self.provTable.columnCount()):
            for r in range(0, self.provTable.rowCount()):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, self.prov_brk[r][c])
                self.provTable.setItem(r, c, item)

        for i in range(0, self.provPerTable.columnCount()):
            item = QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, self.prov_PersonalAmount[i])
            self.provPerTable.setItem(0, i, item)

        for c in range(0, self.fedTable.columnCount()):
            for r in range(0, self.fedTable.rowCount()):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, self.federal_brk[r][c])
                self.fedTable.setItem(r, c, item)

        for i in range(0, self.fedPerTable.columnCount()):
            item = QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, self.federal_PersonalAmount[i])
            self.fedPerTable.setItem(0, i, item)

        for i in range(0, self.eiTable.columnCount()):
            item = QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, self.maxei[i])
            self.eiTable.setItem(0, i, item)

        item = QTableWidgetItem()
        item.setData(QtCore.Qt.EditRole, self.maxcppContrib[0])
        self.cppTable.setItem(0, 0, item)

        item = QTableWidgetItem()
        item.setData(QtCore.Qt.EditRole, self.maxcppContrib[1])
        self.cppTable.setItem(0, 1, item)

        item = QTableWidgetItem()
        item.setData(QtCore.Qt.EditRole, self.cppExempt)
        self.cppTable.setItem(0, 2, item)


if __name__ == '__main__':
    from modules import jsonFile
    import sys

    app = QApplication(sys.argv)
    form = Editor()
    form.show()
    sys.exit(app.exec_())

