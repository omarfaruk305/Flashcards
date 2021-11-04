import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from welcomescreen import Welcomescreen_window
from menuscreen import Menuscreen_window
from user import Users
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Welcomescreen_window()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
