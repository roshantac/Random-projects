
from PyQt5 import QtCore, QtGui, QtWidgets

class welcome(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        import sqlite3
        self.conn=sqlite3.connect("data.db")
        self.con=self.conn.cursor()
        self.con.execute(''' CREATE TABLE IF NOT EXISTS ACCOUNT(ID INTEGER PRIMARY KEY,
            NAME TEXT,
            BALANCE INTEGER)''')
        self.con.execute("SELECT COUNT (*) FROM ACCOUNT")
        if self.con.fetchone()[0]==0:
            self.con.execute("INSERT INTO ACCOUNT VALUES(1,'Shafeeq',99999)")
            self.con.execute("INSERT INTO ACCOUNT VALUES(2,'Sharanya',89999)") 
            self.con.execute("INSERT INTO ACCOUNT VALUES(3,'aiswarya',70000)")
            self.con.execute("INSERT INTO ACCOUNT VALUES(4,'athira',65000)")
            self.con.execute("INSERT INTO ACCOUNT VALUES(5,'roshan',65000)")
        self.con.execute('''CREATE TABLE IF NOT EXISTS ID(SINO INTEGER PRIMARY KEY,NUM INTEGER)''')
        self.con.execute("SELECT COUNT (*) FROM ID")
        if self.con.fetchone()[0]==0:
            self.con.execute("INSERT INTO ID VALUES(1,0)")
        self.con.execute("UPDATE ID SET NUM=0 WHERE SINO=1")
        self.conn.commit()
        self.setupUi()

    def setupUi(self):
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"blue.jpg\");\n"
"")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 130, 651, 171))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent;\n"
"\n"
"font: 75 italic 48pt \"Courier 10 Pitch\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(70, 280, 651, 171))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label2.setFont(font)
        self.label2.setStyleSheet("background:transparent;\n"
"\n"
"font: 75 italic 48pt \"Courier 10 Pitch\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 600, 85, 61))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/y.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.Enter = QtWidgets.QPushButton(self.centralWidget)
        self.Enter.setGeometry(QtCore.QRect(810, 390, 131, 121))
        self.Enter.setStyleSheet("background:transparent;\n"
"border:0px;")
        self.Enter.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("login-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Enter.setIcon(icon1)
        self.Enter.setIconSize(QtCore.QSize(100, 100))
        self.Enter.setObjectName("Enter")
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Welcome to ATM service</span></p></body></html>"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Press Enter and hold on sensor</span></p></body></html>"))
        self.Enter.clicked.connect(self.finger)
    def finger(self):
        from scanner import Scanner
        self.scan =Scanner()
        self.scan.show()
        self.scan.hide()
        self.close()

    	 




