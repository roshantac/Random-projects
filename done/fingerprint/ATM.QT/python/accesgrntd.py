

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class access(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.conn=sqlite3.connect("data.db")
        self.con=self.conn.cursor()
        self.idno=self.con.execute("SELECT NUM FROM ID WHERE SINO=1").fetchall()[0][0]
        #self.idno=self.idno[0]
        print(self.idno)
        self.hname=self.con.execute("SELECT NAME FROM ACCOUNT WHERE ID=?",(self.idno,)).fetchall()[0][0]
        #self.hname=self.hname[0]
        print(self.hname)
        
        
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000,600)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setFont(font)
        self.setStyleSheet("background-image: url(\"2.jpg\");")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 471, 121))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(53)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background:transparent;\n"
"color: rgb(115, 210, 22);\n"
"font: 53pt \"Cantarell\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(239, 41, 41);\n"
"font: 75 italic 40pt \"Century Schoolbook L\";\n"
"background:transparent;\n"
"")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.NAME = QtWidgets.QLabel(self.centralWidget)
        self.NAME.setEnabled(True)
        self.NAME.setGeometry(QtCore.QRect(140, 240, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.NAME.setFont(font)
        self.NAME.setAutoFillBackground(False)
        self.NAME.setStyleSheet("color: rgb(239, 41, 41);\n"
"font: 75 italic 30pt \"Century Schoolbook L\";\n"
"background:transparent;\n"
"")
        self.NAME.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.NAME.setObjectName("NAME")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(252, 175, 62);\n"
"color: rgb(252, 233, 79);\n"
"background:transparent;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("window", "window"))
        self.label.setText(_translate("window", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Access Granded</span></p></body></html>"))
        self.label_2.setText(_translate("window", "WELCOME"))
        self.NAME.setText(self.hname)
        self.pushButton.setText(_translate("window", "CONTINUE"))
        self.pushButton.clicked.connect(self.select1)
    def select1(self):
        from selected import main
        self.sel2=main()
        self.close()
        self.sel2.show()
        




