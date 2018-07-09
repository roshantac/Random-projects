

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.numbr=0
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"maxresdefault.jpg\");")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.clearbutton = QtWidgets.QPushButton(self.centralWidget)
        self.clearbutton.setGeometry(QtCore.QRect(0, 220, 141, 41))
        self.clearbutton.setStyleSheet("background-color: rgb(250, 163, 13);\n"
"color: rgb(245, 121, 0);")
        self.clearbutton.setObjectName("clearbutton")
        self.closebutton = QtWidgets.QPushButton(self.centralWidget)
        self.closebutton.setGeometry(QtCore.QRect(0, 320, 141, 41))
        self.closebutton.setStyleSheet("background-color: rgb(249, 11, 11);\n"
"color: rgb(239, 41, 41);")
        self.closebutton.setObjectName("closebutton")
        self.enterbutton = QtWidgets.QPushButton(self.centralWidget)
        self.enterbutton.setGeometry(QtCore.QRect(860, 220, 141, 41))
        self.enterbutton.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(138, 226, 52);")
        self.enterbutton.setObjectName("enterbutton")
        self.cancelbutton = QtWidgets.QPushButton(self.centralWidget)
        self.cancelbutton.setGeometry(QtCore.QRect(860, 320, 141, 41))
        self.cancelbutton.setStyleSheet("background-color: rgb(249, 11, 11);\n"
"color: rgb(239, 41, 41);")
        self.cancelbutton.setObjectName("cancelbutton")
        self.key5 = QtWidgets.QPushButton(self.centralWidget)
        self.key5.setGeometry(QtCore.QRect(427, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key5.setFont(font)
        self.key5.setStyleSheet("color: rgb(243, 243, 243);")
        self.key5.setObjectName("key5")
        self.key7 = QtWidgets.QPushButton(self.centralWidget)
        self.key7.setGeometry(QtCore.QRect(347, 350, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key7.setFont(font)
        self.key7.setStyleSheet("color: rgb(243, 243, 243);")
        self.key7.setObjectName("key7")
        self.key3 = QtWidgets.QPushButton(self.centralWidget)
        self.key3.setGeometry(QtCore.QRect(507, 250, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key3.setFont(font)
        self.key3.setStyleSheet("color: rgb(243, 243, 243);")
        self.key3.setObjectName("key3")
        self.key6 = QtWidgets.QPushButton(self.centralWidget)
        self.key6.setGeometry(QtCore.QRect(507, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key6.setFont(font)
        self.key6.setStyleSheet("color: rgb(243, 243, 243);")
        self.key6.setObjectName("key6")
        self.key4 = QtWidgets.QPushButton(self.centralWidget)
        self.key4.setGeometry(QtCore.QRect(347, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key4.setFont(font)
        self.key4.setStyleSheet("color: rgb(243, 243, 243);")
        self.key4.setObjectName("key4")
        self.key8 = QtWidgets.QPushButton(self.centralWidget)
        self.key8.setGeometry(QtCore.QRect(427, 350, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key8.setFont(font)
        self.key8.setStyleSheet("color: rgb(243, 243, 243);")
        self.key8.setObjectName("key8")
        self.key2 = QtWidgets.QPushButton(self.centralWidget)
        self.key2.setGeometry(QtCore.QRect(427, 250, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key2.setFont(font)
        self.key2.setStyleSheet("color: rgb(243, 243, 243);")
        self.key2.setObjectName("key2")
        self.key0 = QtWidgets.QPushButton(self.centralWidget)
        self.key0.setGeometry(QtCore.QRect(427, 400, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key0.setFont(font)
        self.key0.setStyleSheet("color: rgb(243, 243, 243);")
        self.key0.setObjectName("key0")
        self.key9 = QtWidgets.QPushButton(self.centralWidget)
        self.key9.setGeometry(QtCore.QRect(507, 350, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key9.setFont(font)
        self.key9.setStyleSheet("color: rgb(243, 243, 243);")
        self.key9.setObjectName("key9")
        self.key1 = QtWidgets.QPushButton(self.centralWidget)
        self.key1.setGeometry(QtCore.QRect(347, 250, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.key1.setFont(font)
        self.key1.setAutoFillBackground(False)
        self.key1.setStyleSheet("color: rgb(243, 243, 243);")
        self.key1.setObjectName("key1")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 170, 300, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"color: rgb(243, 243, 243);\n"
"background:transparent;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 491, 101))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.label.setObjectName("label")
        self.key1.raise_()
        self.closebutton.raise_()
        self.cancelbutton.raise_()
        self.clearbutton.raise_()
        self.key5.raise_()
        self.key7.raise_()
        self.key3.raise_()
        self.key6.raise_()
        self.key4.raise_()
        self.key8.raise_()
        self.key2.raise_()
        self.key0.raise_()
        self.key9.raise_()
        self.enterbutton.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.clearbutton.setText(_translate("self", "CLEAR"))
        self.closebutton.setText(_translate("self", "CLOSE"))
        self.enterbutton.setText(_translate("self", "ENTER"))
        self.cancelbutton.setText(_translate("self", "CANCEL"))
        self.key5.setText(_translate("self", "5"))
        self.key7.setText(_translate("self", "7"))
        self.key3.setText(_translate("self", "3"))
        self.key6.setText(_translate("self", "6"))
        self.key4.setText(_translate("self", "4"))
        self.key8.setText(_translate("self", "8"))
        self.key2.setText(_translate("self", "2"))
        self.key0.setText(_translate("self", "0"))
        self.key9.setText(_translate("self", "9"))
        self.key1.setText(_translate("self", "1"))
        self.label.setText(_translate("self", "Enter The Amount"))
        self.enterbutton.clicked.connect(self.enter)
        self.key1.clicked.connect(self.add1)
        self.key2.clicked.connect(self.add2)
        self.key3.clicked.connect(self.add3)
        self.key4.clicked.connect(self.add4)
        self.key5.clicked.connect(self.add5)
        self.key6.clicked.connect(self.add6)
        self.key7.clicked.connect(self.add7)
        self.key8.clicked.connect(self.add8)
        self.key9.clicked.connect(self.add9)
        self.key0.clicked.connect(self.add0)
        self.clearbutton.clicked.connect(self.clear)
        self.closebutton.clicked.connect(self.closed)
        self.cancelbutton.clicked.connect(self.cancel)

    def clear(self):
        self.numbr=int(self.numbr/10)
        self.lcdNumber.display(self.numbr)

    def closed(self):
        from thankyou import Ui_M
        self.ext=Ui_M()
        self.close()
        self.ext.show()
        

    def cancel(self):
        self.numbr=0
        self.lcdNumber.display(self.numbr)



    def add0(self):
        self.numbr=(self.numbr*10)+0
        self.lcdNumber.display(self.numbr)
    def add1(self):
        self.numbr=(self.numbr*10)+1
        self.lcdNumber.display(self.numbr)
    def add2(self):
        self.numbr=(self.numbr*10)+2
        self.lcdNumber.display(self.numbr)
    def add3(self):
        self.numbr=(self.numbr*10)+3
        self.lcdNumber.display(self.numbr)
    def add4(self):
        self.numbr=(self.numbr*10)+4
        self.lcdNumber.display(self.numbr)
    def add5(self):
        self.numbr=(self.numbr*10)+5
        self.lcdNumber.display(self.numbr)
    def add6(self):
        self.numbr=(self.numbr*10)+6
        self.lcdNumber.display(self.numbr)
    def add7(self):
        self.numbr=(self.numbr*10)+7
        self.lcdNumber.display(self.numbr)
    def add8(self):
        self.numbr=(self.numbr*10)+8
        self.lcdNumber.display(self.numbr)
    def add9(self):
        self.numbr=(self.numbr*10)+9
        self.lcdNumber.display(self.numbr)

    def enter(self):
        import sqlite3
        self.conn=sqlite3.connect("data.db")
        self.con=self.conn.cursor()
        self.idno=self.con.execute("SELECT NUM FROM ID WHERE SINO=1").fetchall()[0][0]
        self.balance=self.con.execute("SELECT BALANCE FROM ACCOUNT WHERE ID=?",(self.idno,)).fetchall()[0][0]
        self.newblnce=self.balance-self.numbr
        self.con.execute("UPDATE ACCOUNT SET BALANCE=? WHERE ID=?",(self.newblnce,self.idno))
        self.conn.commit()
        #add db portions here
        #
        #
        from takmony import Ui_self
        self.thank=Ui_self()
        self.thank.show()
        self.close()



