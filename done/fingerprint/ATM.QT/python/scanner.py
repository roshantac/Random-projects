

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import sqlite3
class Scanner(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

        try:
            self.ser=serial.Serial('/dev/ttyACM0',9600)
        except:
        	self.ser=serial.Serial('/dev/ttyACM1',9600)
            #print("no devices connected")
        self.id='0'
        while  True:
                k=self.ser.readline()
                d=k.decode("utf-8", "ignore")
                if(int(d)>0) and (int(d)<6):
                	self.c=int(d)
                else:
                	self.c=int(int(d)/10)


                print(self.c)
                
                print(self.c)
                if self.c>0:
                	self.conn=sqlite3.connect("data.db")
                	self.con=self.conn.cursor()
                	self.idno=self.con.execute("UPDATE ID SET NUM=? WHERE SINO=1",(self.c,))
                	self.conn.commit()
                	print ("greter than zero")
                	from accesgrntd import access
                	self.q=access()
                	self.q.show()
                	self.close()
                	break
                else:
                	print("its zero")
        self.close()
        
        


    def setupUi(self):
        #self.setObjectName("self")
        self.resize(1000, 600)
        self.setStyleSheet("background-image:url(\"biometria-123.jpg\");")
        self.setIconSize(QtCore.QSize(80, 80))
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(150, -10, 791, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Roman No9 L")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(239, 41, 41);\n"
"background:transparent;\n"
"")
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 490, 701, 81))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 600, 85, 61))
        self.pushButton.setText("Continue")
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main", "window"))
        self.label.setText(_translate("MainWindow", "TOUCH FINGER-PRINT SCANNER"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.close()
    
        

