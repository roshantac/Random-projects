# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_M(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"blue.jpg\")")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(310, 70, 66, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(280, 230, 541, 101))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setObjectName("label_2")
        self.home = QtWidgets.QPushButton(self.centralWidget)
        self.home.setGeometry(QtCore.QRect(710, 407, 85, 81))
        self.home.setStyleSheet("border:0px;\n"
"background:transparent;")
        self.home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/home-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(70, 70))
        self.home.setObjectName("home")
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_2.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Thank you for using this ATM </span></p><p align=\"center\"><br/></p></body></html>"))
        self.home.clicked.connect(self.exit)

    def exit(self):
        from welcom import welcome
        self.ext=welcome()
        self.close()
        self.ext.show()




