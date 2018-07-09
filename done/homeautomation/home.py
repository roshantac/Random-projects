
from PyQt5 import QtCore, QtGui, QtWidgets
import serial

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        try:
        	self.ser=serial.Serial('/dev/ttyACM0',9600)
        except:
        	print("not connected")
        self.setupUi()
    def setupUi(self):
        #MainWindow.setObjectName("MainWindow")
        self.resize(510, 600)
        self.setStyleSheet("\n"
"background-color: rgb(255, 255, 240);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.L1_ON = QtWidgets.QPushButton(self.centralwidget)
        self.L1_ON.setGeometry(QtCore.QRect(280, 260, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.L1_ON.setFont(font)
        self.L1_ON.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.L1_ON.setObjectName("L1_ON")
        self.L1_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.L1_OFF.setGeometry(QtCore.QRect(350, 260, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.L1_OFF.setFont(font)
        self.L1_OFF.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.L1_OFF.setObjectName("L1_OFF")
        self.L2_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.L2_OFF.setGeometry(QtCore.QRect(350, 370, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.L2_OFF.setFont(font)
        self.L2_OFF.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.L2_OFF.setObjectName("L2_OFF")
        self.L2_ON = QtWidgets.QPushButton(self.centralwidget)
        self.L2_ON.setGeometry(QtCore.QRect(280, 370, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.L2_ON.setFont(font)
        self.L2_ON.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.L2_ON.setObjectName("L2_ON")
        self.F1_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.F1_OFF.setGeometry(QtCore.QRect(350, 480, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F1_OFF.setFont(font)
        self.F1_OFF.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.F1_OFF.setObjectName("F1_OFF")
        self.F1_ON = QtWidgets.QPushButton(self.centralwidget)
        self.F1_ON.setGeometry(QtCore.QRect(280, 480, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.F1_ON.setFont(font)
        self.F1_ON.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.F1_ON.setObjectName("F1_ON")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 250, 91, 81))
        self.pushButton_7.setStyleSheet("border:0 px;")
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bulb_life.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 360, 91, 81))
        self.pushButton_8.setStyleSheet("border:0px;")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 470, 91, 81))
        self.pushButton_9.setStyleSheet("border:0px;")
        self.pushButton_9.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 260, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(193, 125, 17);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(193, 125, 17);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 480, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(193, 125, 17);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(193, 125, 17);")
        self.label_4.setObjectName("label_4")
        self.CONNECT = QtWidgets.QPushButton(self.centralwidget)
        self.CONNECT.setGeometry(QtCore.QRect(210, 120, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.CONNECT.setFont(font)
        self.CONNECT.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"selection-background-color: rgb(252, 233, 79);")
        self.CONNECT.setObjectName("CONNECT")
        self.setCentralWidget(self.centralwidget)



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.serialconn

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L1_ON.setText(_translate("MainWindow", "ON"))
        self.L1_OFF.setText(_translate("MainWindow", "OFF"))
        self.L2_OFF.setText(_translate("MainWindow", "OFF"))
        self.L2_ON.setText(_translate("MainWindow", "ON"))
        self.F1_OFF.setText(_translate("MainWindow", "OFF"))
        self.F1_ON.setText(_translate("MainWindow", "ON"))
        self.label.setText(_translate("MainWindow", "LAMP 1"))
        self.label_2.setText(_translate("MainWindow", "LAMP 2"))
        self.label_3.setText(_translate("MainWindow", "FAN"))
        self.label_4.setText(_translate("MainWindow", "SMART HOME"))
        self.CONNECT.setText(_translate("MainWindow", "CONNECT"))
        self.CONNECT.clicked.connect(self.serialconn)
        self.L1_ON.clicked.connect(self.send1)
        self.L1_OFF.clicked.connect(self.send2)
        self.L2_ON.clicked.connect(self.send3)
        self.L2_OFF.clicked.connect(self.send4)
        self.F1_ON.clicked.connect(self.send5)
        self.F1_OFF.clicked.connect(self.send6)


    def serialconn(self):
        #send('z')
        self.ser=serial.Serial('/dev/ttyACM0',9600)
        if self.ser.is_open>0:
            self.CONNECT.setStyleSheet("background-color: rgb(252, 233, 79);")
            self.ser.write(b'z')
        else:
            self.CONNECT.setStyleSheet("background-color: rgb(136, 138, 133);") 
    def send1(self):
        self.ser.write(b'a')
        pass
    def send2(self):
        self.ser.write(b'b')
        pass
    def send3(self):
        self.ser.write(b'c')
        pass
    def send4(self):
        self.ser.write(b'd')
        pass
    def send5(self):
        self.ser.write(b'e')
        pass
    def send6(self):
        self.ser.write(b'f')
        pass
