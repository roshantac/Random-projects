from PyQt5 import QtCore, QtGui, QtWidgets
import os
from welcom import welcome




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    home = welcome()
    home.show()
    sys.exit(app.exec_())

