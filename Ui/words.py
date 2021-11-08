from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import sys


class Wordscreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("wordscreen.ui", self)

        self.green_button.clicked.connect(self.green)

    def green(self):
        print("hello")


app = QApplication(sys.argv)

window = Wordscreen()
window.show()
sys.exit(app.exec_())
