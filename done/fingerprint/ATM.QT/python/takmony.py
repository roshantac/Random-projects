

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_self(QtWidgets.QMainWindow):
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
        self.label.setGeometry(QtCore.QRect(330, 250, 441, 141))
        self.label.setStyleSheet("background:transparent;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 450, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(204, 0, 0);")
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
        self.label.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">TAKE YOUR CASH.....</span></p></body></html>"))
        self.pushButton.setText(_translate("self", "Continue"))
        self.pushButton.clicked.connect(self.thanks)

    def thanks(self):
        from thankyou import Ui_M
        self.ext=Ui_M()
        self.close()
        self.ext.show()



