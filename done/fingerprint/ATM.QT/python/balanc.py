

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_self(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        import sqlite3
        self.conn=sqlite3.connect("data.db")
        self.con=self.conn.cursor()
        self.idno=self.con.execute("SELECT NUM FROM ID WHERE SINO=1").fetchall()[0][0]
        self.balance=self.con.execute("SELECT BALANCE FROM ACCOUNT WHERE ID=?",(self.idno,)).fetchall()[0][0]
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"blue.jpg\")")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(230, 250, 491, 101))
        self.lcdNumber.setStyleSheet("color: rgb(239, 41, 41);\n"
"background:transparent;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(self.balance)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(350, 60, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(39)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(237, 212, 0);\n"
"background:transparent;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(814, 447, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Balance"))
        self.pushButton.setText(_translate("self", "Continue"))
        self.pushButton.clicked.connect(self.thanks)

    def thanks(self):
        from thankyou import Ui_M
        self.ext=Ui_M()
        self.close()
        self.ext.show()



