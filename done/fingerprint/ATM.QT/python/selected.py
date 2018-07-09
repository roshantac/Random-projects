# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"3.png\")")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.balancebutton = QtWidgets.QPushButton(self.centralWidget)
        self.balancebutton.setGeometry(QtCore.QRect(440, 100, 250, 81))
        self.balancebutton.setMaximumSize(QtCore.QSize(251, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.balancebutton.setFont(font)
        self.balancebutton.setStyleSheet("background-color: rgb(244, 236, 4);\n"
"color: rgb(83, 247, 4);")
        self.balancebutton.setObjectName("balancebutton")
        self.withdrawalbutton = QtWidgets.QPushButton(self.centralWidget)
        self.withdrawalbutton.setGeometry(QtCore.QRect(440, 290, 250, 81))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.withdrawalbutton.setFont(font)
        self.withdrawalbutton.setStyleSheet("background-color: rgb(244, 236, 4);\n"
"color: rgb(83, 247, 4);")
        self.withdrawalbutton.setObjectName("withdrawalbutton")
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.balancebutton.setText(_translate("MainWindow", "Balance Enquiry"))
        self.withdrawalbutton.setText(_translate("MainWindow", "Withdrawal"))
        self.balancebutton.clicked.connect(self.Balance)
        self.withdrawalbutton.clicked.connect(self.Withdrawal)

    def Balance(self):
        from balanc import Ui_self
        self.k=Ui_self()
        
        self.k.show()
        self.close()

    def Withdrawal(self):
        from amntwindw import Ui_Main
        self.tes=Ui_Main()
        self.close()
        self.tes.show()



