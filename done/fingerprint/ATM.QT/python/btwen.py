

from PyQt5 import QtCore, QtGui, QtWidgets
import serial

class btween(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ser=serial.Serial('/dev/ttyACM0',9600)
                
        while  True:
                c=self.ser.read()
                if int(c)>0:
                	print ("greter than zero")
                	from accesgrntd import access
                	self.q=access()
                	self.q.show()
                	self.close()
                	break
                else:
                	print("its zero")
        self.setupUi()
    def setupUi(self):
        #self.setObjectName("self")
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        pass

