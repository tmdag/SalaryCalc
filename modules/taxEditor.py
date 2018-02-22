from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QSplitter, QLabel, QSizePolicy, QComboBox, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QMenuBar, QMenu, QStatusBar, QAction

class Editor(QMainWindow):
    def __init__ (self, parent=None):
        # super().__init__(parent) # Python => 3.0 method
        super(Editor, self).__init__(parent) # Python  < 3.0 method
        self.initUI()
    def initUI(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(400, 800)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.ProvinceLabel = QLabel(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProvinceLabel.sizePolicy().hasHeightForWidth())
        self.ProvinceLabel.setSizePolicy(sizePolicy)
        self.ProvinceLabel.setMaximumSize(QtCore.QSize(80, 30))
        self.ProvinceLabel.setObjectName("ProvinceLabel")
        self.provinceBox = QComboBox(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.provinceBox.sizePolicy().hasHeightForWidth())
        self.provinceBox.setSizePolicy(sizePolicy)
        self.provinceBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.provinceBox.setObjectName("provinceBox")
        self.provinceBox.addItem("")
        self.taxYearLabel = QLabel(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxYearLabel.sizePolicy().hasHeightForWidth())
        self.taxYearLabel.setSizePolicy(sizePolicy)
        self.taxYearLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.taxYearLabel.setObjectName("taxYearLabel")
        self.taxYearBox = QSpinBox(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxYearBox.sizePolicy().hasHeightForWidth())
        self.taxYearBox.setSizePolicy(sizePolicy)
        self.taxYearBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.taxYearBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.taxYearBox.setAutoFillBackground(False)
        self.taxYearBox.setMinimum(1990)
        self.taxYearBox.setMaximum(2050)
        self.taxYearBox.setProperty("value", 2018)
        self.taxYearBox.setObjectName("taxYearBox")
        self.verticalLayout_3.addWidget(self.splitter)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.ProvincialTab = QWidget()
        self.ProvincialTab.setObjectName("ProvincialTab")
        self.verticalLayout = QVBoxLayout(self.ProvincialTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.provLabel = QLabel(self.ProvincialTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.provLabel.sizePolicy().hasHeightForWidth())
        self.provLabel.setSizePolicy(sizePolicy)
        self.provLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.provLabel.setObjectName("provLabel")
        self.verticalLayout.addWidget(self.provLabel)
        self.provTable = QTableWidget(self.ProvincialTab)
        self.provTable.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.provTable.sizePolicy().hasHeightForWidth())
        self.provTable.setSizePolicy(sizePolicy)
        self.provTable.setAcceptDrops(True)
        self.provTable.setAutoFillBackground(False)
        self.provTable.setGridStyle(QtCore.Qt.SolidLine)
        self.provTable.setObjectName("provTable")
        self.provTable.setColumnCount(2)
        self.provTable.setRowCount(5)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.provTable.setHorizontalHeaderItem(1, item)
        self.provTable.horizontalHeader().setVisible(True)
        self.provTable.horizontalHeader().setCascadingSectionResizes(False)
        self.provTable.horizontalHeader().setDefaultSectionSize(180)
        self.provTable.horizontalHeader().setStretchLastSection(True)
        self.provTable.verticalHeader().setVisible(False)
        self.provTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.provTable)
        self.provPerLabel = QLabel(self.ProvincialTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.provPerLabel.sizePolicy().hasHeightForWidth())
        self.provPerLabel.setSizePolicy(sizePolicy)
        self.provPerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.provPerLabel.setObjectName("provPerLabel")
        self.verticalLayout.addWidget(self.provPerLabel)
        self.provPerTable = QTableWidget(self.ProvincialTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.provPerTable.sizePolicy().hasHeightForWidth())
        self.provPerTable.setSizePolicy(sizePolicy)
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
        self.fedTable = QTableWidget(self.FederalTab)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fedTable.sizePolicy().hasHeightForWidth())
        self.fedTable.setSizePolicy(sizePolicy)
        self.fedTable.setMinimumSize(QtCore.QSize(0, 0))
        self.fedTable.setObjectName("fedTable")
        self.fedTable.setColumnCount(2)
        self.fedTable.setRowCount(5)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.fedTable.setHorizontalHeaderItem(1, item)
        self.fedTable.horizontalHeader().setDefaultSectionSize(180)
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
        self.menubar = QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen = QAction()
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction()
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QAction()
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        # QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProvinceLabel.setText(_translate("MainWindow", "Province"))
        self.provinceBox.setItemText(0, _translate("MainWindow", "BC"))
        self.taxYearLabel.setText(_translate("MainWindow", "Tax Year"))
        self.provLabel.setText(_translate("MainWindow", "Provincial Tax Rates, Personal income"))
        item = self.provTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.provTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.provTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.provTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.provTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.provTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "taxable Income"))
        item = self.provTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "taxRate"))
        self.provPerLabel.setText(_translate("MainWindow", "Personal Amount"))
        item = self.provPerTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.provPerTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "amount"))
        item = self.provPerTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tax rate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProvincialTab), _translate("MainWindow", "Provincial Tax"))
        self.fedLabel.setText(_translate("MainWindow", "Federal Tax Rates"))
        item = self.fedTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.fedTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.fedTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.fedTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.fedTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.fedTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "taxable Income"))
        item = self.fedTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "taxRate"))
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
        self.cppLabel.setText(_translate("MainWindow", "CPP"))
        item = self.cppTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPP"))
        item = self.cppTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "max cpp contribution"))
        item = self.cppTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tax"))
        item = self.cppTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "cpp excempt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    form = Editor()
    form.show()
    sys.exit(app.exec_())

