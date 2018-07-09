

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        
        #MainWindow.setObjectName("MainWindow")
        self.resize(1000, 600)
        self.setStyleSheet("background-color: rgb(252, 200, 200);\n"
"color: rgb(239, 41, 41);")
        self.setStyleSheet("background-image:url(\"Hotel-Royal-Palace-logo.png\");\n"
"\n"
"\n"
"")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 360, 71, 101))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pub_bar-13-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralWidget)
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.clicked.connect(self.menu)

    def menu(self):
        from menut import menu_window
        self.MENU=menu_window()
        self.close()
        self.MENU.show()
          




