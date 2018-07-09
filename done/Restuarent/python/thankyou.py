

from PyQt5 import QtCore, QtGui, QtWidgets

class Message(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        
        self.resize(1000, 650)
        self.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"color: rgb(239, 41, 41);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 230, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 91, 91))
        self.pushButton.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("restaurant-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(75, 75))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "THANK YOU "))
        self.pushButton.clicked.connect(self.welcom)

    def welcom(self):
        from welcom import Ui_MainWindow
        self.home=Ui_MainWindow()
        self.close()
        self.home.show()



