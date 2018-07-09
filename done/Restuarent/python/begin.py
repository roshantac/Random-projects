from PyQt5 import QtCore, QtGui, QtWidgets
import os
from welcom import Ui_MainWindow




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    home = Ui_MainWindow()
    home.show()
    sys.exit(app.exec_())

