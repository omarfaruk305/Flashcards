
from PyQt5 import QtCore, QtGui, QtWidgets
from menuscreen import Menuscreen_window
from user import Users


class Welcomescreen_window(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 380)
        MainWindow.setMinimumSize(QtCore.QSize(591, 380))
        MainWindow.setMaximumSize(QtCore.QSize(591, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_widget = QtWidgets.QWidget(self.centralwidget)
        self.welcome_widget.setGeometry(QtCore.QRect(-20, -10, 641, 481))
        self.welcome_widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.welcome_widget.setStyleSheet(
            "background-color: rgb(85, 85, 255);")
        self.welcome_widget.setObjectName("welcome_widget")
        self.welcome_label = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label.setGeometry(QtCore.QRect(230, 50, 221, 41))
        self.welcome_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                         "color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.username_label = QtWidgets.QLabel(self.welcome_widget)
        self.username_label.setGeometry(QtCore.QRect(140, 180, 111, 21))
        self.username_label.setStyleSheet("font: 14pt \"Berlin Sans FB\";\n"
                                          "color: rgb(255, 255, 255);")
        self.username_label.setObjectName("username_label")
        self.login_button = QtWidgets.QPushButton(self.welcome_widget)
        self.login_button.setGeometry(QtCore.QRect(340, 250, 131, 41))
        self.login_button.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color :rgb(0, 0, 127);\n"
                                        "border-radius:20px")
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(self.welcome_widget)
        self.signup_button.setGeometry(QtCore.QRect(150, 250, 141, 41))
        self.signup_button.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "color :rgb(0, 0, 127);\n"
                                         "border-radius:20px")
        self.signup_button.setObjectName("signup_button")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.welcome_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 180, 191, 22))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Berlin Sans FB\" ; color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.error_label = QtWidgets.QLabel(self.welcome_widget)
        self.error_label.setGeometry(QtCore.QRect(260, 210, 341, 31))
        self.error_label.setStyleSheet(
            "color: rgb(255, 255, 0);font: 12pt \"Berlin Sans FB;\"\n")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome"))
        self.username_label.setText(
            _translate("MainWindow", "Username : "))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.signup_button.setText(_translate("MainWindow", "Sign in"))
        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def signup(self):
        _translate = QtCore.QCoreApplication.translate
        self.user = Users(self.lineEdit_2.text())
        Users.readjson_user()
        if self.user.checkname():
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 12pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You have account . Try login"))
        else:
            self.user.save_to_json(self.user)
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 12pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Congrats ! Try login now"))

    def login(self):
        _translate = QtCore.QCoreApplication.translate
        self.user = Users(self.lineEdit_2.text())
        Users.readjson_user()
        if self.user.checkname():
            self.menuscreen = Menuscreen_window()
            self.menuscreen.setupUi(MainWindow)
            self.menuscreen.username_label.setText(self.user.name.upper())
            self.menuscreen.level_label.setText(
                "Level : {}".format(self.user.level))
        else:
            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 12pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You Dont Have Account , Signin first."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Welcomescreen_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
