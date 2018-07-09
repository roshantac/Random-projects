
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
class menu_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.ser=serial.Serial('/dev/ttyACM0',9600)
        except:
            print('not connected')

        
        self.setupUi()
    def setupUi(self):
        self.list=""
        self.bill=0
        self.resize(1000, 650)
        self.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.tea = QtWidgets.QLabel(self.centralWidget)
        self.tea.setGeometry(QtCore.QRect(160, 120, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tea.setFont(font)
        self.tea.setObjectName("tea")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(160, 320, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.coffee = QtWidgets.QLabel(self.centralWidget)
        self.coffee.setGeometry(QtCore.QRect(160, 170, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.coffee.setFont(font)
        self.coffee.setObjectName("coffee")
        self.Limejuice = QtWidgets.QLabel(self.centralWidget)
        self.Limejuice.setGeometry(QtCore.QRect(160, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Limejuice.setFont(font)
        self.Limejuice.setObjectName("Limejuice")
        self.banafry = QtWidgets.QLabel(self.centralWidget)
        self.banafry.setGeometry(QtCore.QRect(160, 260, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.banafry.setFont(font)
        self.banafry.setObjectName("banafry")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(570, 110, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(570, 210, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(570, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(570, 260, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(570, 320, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.spintea = QtWidgets.QSpinBox(self.centralWidget)
        self.spintea.setGeometry(QtCore.QRect(420, 110, 49, 29))
        self.spintea.setObjectName("spintea")
        self.spincofee = QtWidgets.QSpinBox(self.centralWidget)
        self.spincofee.setGeometry(QtCore.QRect(420, 160, 49, 29))
        self.spincofee.setObjectName("spincofee")
        self.spinlime = QtWidgets.QSpinBox(self.centralWidget)
        self.spinlime.setGeometry(QtCore.QRect(420, 210, 49, 29))
        self.spinlime.setObjectName("spinlime")
        self.spinbanana = QtWidgets.QSpinBox(self.centralWidget)
        self.spinbanana.setGeometry(QtCore.QRect(420, 260, 49, 29))
        self.spinbanana.setObjectName("spinbanana")
        self.spinbonda = QtWidgets.QSpinBox(self.centralWidget)
        self.spinbonda.setGeometry(QtCore.QRect(420, 310, 49, 29))
        self.spinbonda.setObjectName("spinbonda")
        self.spindosa = QtWidgets.QSpinBox(self.centralWidget)
        self.spindosa.setGeometry(QtCore.QRect(810, 100, 49, 29))
        self.spindosa.setObjectName("spindosa")
        self.spinidiapm = QtWidgets.QSpinBox(self.centralWidget)
        self.spinidiapm.setGeometry(QtCore.QRect(810, 150, 49, 29))
        self.spinidiapm.setObjectName("spinidiapm")
        self.spinputtu = QtWidgets.QSpinBox(self.centralWidget)
        self.spinputtu.setGeometry(QtCore.QRect(810, 210, 49, 29))
        self.spinputtu.setObjectName("spinputtu")
        self.spin_icecream = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_icecream.setGeometry(QtCore.QRect(810, 260, 49, 29))
        self.spin_icecream.setObjectName("spin_icecream")
        self.spin_faluda = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_faluda.setGeometry(QtCore.QRect(810, 310, 49, 29))
        self.spin_faluda.setObjectName("spin_faluda")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(410, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(570, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(700, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(800, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        
        self.total = QtWidgets.QPushButton(self.centralWidget)
        self.total.setGeometry(QtCore.QRect(400, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.total.setFont(font)
        self.total.setObjectName("total")

        
        self.totald = QtWidgets.QLCDNumber(self.centralWidget)
        self.totald.setGeometry(QtCore.QRect(530, 420, 151, 51))
        self.totald.setObjectName("total")

        self.ORDER = QtWidgets.QPushButton(self.centralWidget)
        self.ORDER.setGeometry(QtCore.QRect(780, 460, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ORDER.setFont(font)
        self.ORDER.setObjectName("ORDER")
        self.setCentralWidget(self.centralWidget)
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Table-1", "Table-1"))
        self.tea.setText(_translate("MainWindow", "Tea                  7"))
        self.label_2.setText(_translate("MainWindow", "Bonda              8"))
        self.coffee.setText(_translate("MainWindow", "Coffee             8"))
        self.Limejuice.setText(_translate("MainWindow", "Lime Juice       10"))
        self.banafry.setText(_translate("MainWindow", "Banana fry       9"))
        self.label_6.setText(_translate("MainWindow", "Dosai              8"))
        self.label_7.setText(_translate("MainWindow", "Puttu              15"))
        self.label_8.setText(_translate("MainWindow", "Idiyappam       7"))
        self.label_9.setText(_translate("MainWindow", "Ice cream       15"))
        self.label_10.setText(_translate("MainWindow", "Faluda            35"))
        self.label.setText(_translate("MainWindow", "ITEM"))
        self.label_3.setText(_translate("MainWindow", "PRICE"))
        self.label_4.setText(_translate("MainWindow", "COUNT"))
        self.label_5.setText(_translate("MainWindow", "ITEM"))
        self.label_11.setText(_translate("MainWindow", "PRICE"))
        self.label_12.setText(_translate("MainWindow", "COUNT"))
        self.total.setText(_translate("MainWindow", "TOTAL"))
        self.ORDER.setText(_translate("MainWindow", "ORDER"))
        self.ORDER.clicked.connect(self.order)
        self.total.clicked.connect(self.Totl)

    def order(self):
        if self.spintea.value()>0:
            self.list=self.list+"Tea:"+str(self.spintea.value())+","
        if self.spincofee.value()>0:
            self.list=self.list+"cofee:"+str(self.spincofee.value())+","
        if self.spinlime.value()>0:
            self.list=self.list+"Lime:"+str(self.spinlime.value())+","
        if self.spinbanana.value()>0:
            self.list=self.list+"Bananafry:"+str(self.spinbanana.value())+","
        if self.spinbonda.value()>0:
            self.list=self.list+"Bonda:"+str(self.spinbonda.value())+","
        if self.spindosa.value()>0:
            self.list=self.list+"Dosa:"+str(self.spindosa.value())+","
        if self.spinidiapm.value()>0:
            self.list=self.list+"Idiapm:"+str(self.spinidiapm.value())+","
        if self.spinputtu.value()>0:
            self.list=self.list+"Puttu:"+str(self.spinputtu.value())+","
        if self.spin_icecream.value()>0:
            self.list=self.list+"Icecream:"+str(self.spin_icecream.value())+","
        if self.spin_faluda.value()>0:
            self.list=self.list+"Faluda:"+str(self.spin_faluda.value())

        print(self.list)
        try:
        	self.ser=serial.Serial('/dev/ttyACM0',9600)

        	data=self.list.encode('utf-8')
        	self.ser.write(data)
        except:
        	print("arduino not connected")

        from thankyou import Message
        self.msg=Message()
        self.close()
        self.msg.show()

    def Totl(self):
        self.bill=(self.spintea.value()*7)+(self.spincofee.value()*8)+(self.spinlime.value()*10)+(self.spinputtu.value()*15)+(self.spinidiapm.value()*7)+(self.spindosa.value()*8)+(self.spinbonda.value()*8)+(self.spinbanana.value()*9)+(self.spin_faluda.value()*35)+(self.spin_icecream.value()*15)
        print(self.bill)
        self.totald.display(self.bill)
