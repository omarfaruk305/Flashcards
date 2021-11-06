import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from user import Users

user = Users()


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
        self.login_button.setGeometry(QtCore.QRect(350, 250, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("font: 19pt \"Berlin Sans FB\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color :rgb(0, 0, 127);\n"
                                        "border-radius:20px")
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(self.welcome_widget)
        self.signup_button.setGeometry(QtCore.QRect(150, 250, 141, 41))
        self.signup_button.setStyleSheet("font: 19pt \"Berlin Sans FB\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "color :rgb(0, 0, 127);\n"
                                         "border-radius:20px")
        self.signup_button.setObjectName("signup_button")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.welcome_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 180, 191, 31))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Berlin Sans FB\";\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.error_label = QtWidgets.QLabel(self.welcome_widget)
        self.error_label.setGeometry(QtCore.QRect(260, 210, 311, 16))
        self.error_label.setStyleSheet("color: rgb(255, 255, 0);\n"
                                       "border-radius:20px")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome"))
        self.username_label.setText(_translate("MainWindow", "Username : "))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.signup_button.setText(_translate("MainWindow", "Sign in"))
        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def setmenuscreenforuser(self):
        menuscreenui.setupUi(MainWindow)
        menuscreenui.username_label.setText(user.name.upper())
        menuscreenui.level_label.setText(
            "Level : {}".format(user.level))
        menuscreenui.progress_progressBar.setProperty(
            "value", user.totalprogress())

    def signup(self):
        _translate = QtCore.QCoreApplication.translate
        self.user = Users(self.lineEdit_2.text())
        Users.readjson_user()
        if self.user.checkname():
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You have an account already.Login"))
        else:
            self.user.save_to_json(self.user)
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Congrats ! Try login now"))

    def login(self):
        _translate = QtCore.QCoreApplication.translate
        user.readjson_user()
        name = self.lineEdit_2.text()
        for i, j in user.users_dict.items():
            if name == i:
                level = j["level"]
                user.name = name
                user.level = level
                break

        if user.checkname():
            self.setmenuscreenforuser()

        else:
            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You Dont Have Account , Signin first."))


class Menuscreen_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 637)
        MainWindow.setMinimumSize(QtCore.QSize(789, 637))
        MainWindow.setMaximumSize(QtCore.QSize(789, 637))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(789, 637))
        self.centralwidget.setMaximumSize(QtCore.QSize(789, 637))
        self.centralwidget.setObjectName("centralwidget")
        self.mainmenu_widget = QtWidgets.QWidget(self.centralwidget)
        self.mainmenu_widget.setGeometry(QtCore.QRect(0, 0, 881, 721))
        self.mainmenu_widget.setMinimumSize(QtCore.QSize(881, 721))
        self.mainmenu_widget.setMaximumSize(QtCore.QSize(881, 721))
        self.mainmenu_widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mainmenu_widget.setToolTipDuration(0)
        self.mainmenu_widget.setAutoFillBackground(False)
        self.mainmenu_widget.setStyleSheet(
            "background-color: rgb(85, 85, 255);")
        self.mainmenu_widget.setObjectName("mainmenu_widget")
        self.mainmenu_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.mainmenu_label.setGeometry(QtCore.QRect(260, 40, 301, 54))
        self.mainmenu_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainmenu_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                          "\n"
                                          "color: rgb(255, 255, 255);")
        self.mainmenu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainmenu_label.setObjectName("mainmenu_label")
        self.playbutton = QtWidgets.QPushButton(self.mainmenu_widget)
        self.playbutton.setGeometry(QtCore.QRect(410, 380, 231, 71))
        self.playbutton.setStyleSheet("border-radius:20px;\n"
                                      "font: 34pt \"Berlin Sans FB\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "color :rgb(0, 0, 127)")
        self.playbutton.setObjectName("playbutton")
        self.username_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.username_label.setGeometry(QtCore.QRect(310, 130, 201, 31))
        self.username_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                          "\n"
                                          "color: rgb(255, 255, 255);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.quitbutton = QtWidgets.QPushButton(self.mainmenu_widget)
        self.quitbutton.setGeometry(QtCore.QRect(160, 380, 231, 71))
        self.quitbutton.setStyleSheet("border-radius:20px;font: 34pt \"Berlin Sans FB\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "color :rgb(0, 0, 127)")
        self.quitbutton.setObjectName("quitbutton")
        self.progress_progressBar = QtWidgets.QProgressBar(
            self.mainmenu_widget)
        self.progress_progressBar.setGeometry(QtCore.QRect(350, 220, 141, 41))
        self.progress_progressBar.setProperty("value", 24)
        self.progress_progressBar.setObjectName("progress_progressBar")
        self.level_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.level_label.setGeometry(QtCore.QRect(330, 290, 161, 51))
        self.level_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "color :rgb(0, 0, 127)")
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.setObjectName("level_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.mainmenu_label.setText(_translate("MainWindow", "Main Menu"))
        self.playbutton.setText(_translate("MainWindow", "Play"))
        self.username_label.setText(_translate("MainWindow", "User Name"))
        self.quitbutton.setText(_translate("MainWindow", "Quit"))
        self.level_label.setText(_translate("MainWindow", "Level :"))
        self.playbutton.clicked.connect(self.play)
        self.quitbutton.clicked.connect(self.quit)

    def play(self):
        wordscreenui.setupUi(MainWindow)

    def quit(self):
        Users.save_to_json(user)
        sys.exit(app.exec_)


class Wordscreen_window(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 637)
        MainWindow.setMinimumSize(QtCore.QSize(789, 637))
        MainWindow.setMaximumSize(QtCore.QSize(789, 637))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.game_widget = QtWidgets.QWidget(self.centralwidget)
        self.game_widget.setGeometry(QtCore.QRect(-10, -20, 861, 711))
        self.game_widget.setStyleSheet("background-color:rgb(255, 253, 251)")
        self.game_widget.setObjectName("game_widget")
        self.wordcard_label = QtWidgets.QLabel(self.game_widget)
        self.wordcard_label.setEnabled(True)
        self.wordcard_label.setGeometry(QtCore.QRect(130, 180, 531, 301))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wordcard_label.setFont(font)
        self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                          "color:rgb(255, 255, 255) ;\n"
                                          "background-color: rgb(85, 85, 255);")
        self.wordcard_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wordcard_label.setObjectName("wordcard_label")
        self.green_button = QtWidgets.QPushButton(self.game_widget)
        self.green_button.setGeometry(QtCore.QRect(480, 520, 81, 51))
        self.green_button.setStyleSheet("border-radius:20px;\n"
                                        "background-color: rgb(255, 255, 255)")
        self.green_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("check.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("check.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("check.png"),
                       QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("check.png"),
                       QtGui.QIcon.Active, QtGui.QIcon.On)
        self.green_button.setIcon(icon)
        self.green_button.setIconSize(QtCore.QSize(80, 80))
        self.green_button.setObjectName("green_button")
        self.red_button = QtWidgets.QPushButton(self.game_widget)
        self.red_button.setGeometry(QtCore.QRect(250, 520, 81, 51))
        self.red_button.setStyleSheet("border-radius:20px;\n"
                                      "background-color: rgb(255, 255, 255)")
        self.red_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cancel (2).png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.red_button.setIcon(icon1)
        self.red_button.setIconSize(QtCore.QSize(80, 80))
        self.red_button.setObjectName("red_button")
        self.level_label = QtWidgets.QLabel(self.game_widget)
        self.level_label.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.level_label.setStyleSheet("font: 14pt \"Berlin Sans FB\";\n"
                                       "\n"
                                       "background-color: rgb(85, 85, 255);\n"
                                       "color: rgb(255, 255, 255);")
        self.level_label.setObjectName("level_label")
        self.total_time_label = QtWidgets.QLabel(self.game_widget)
        self.total_time_label.setGeometry(QtCore.QRect(310, 30, 191, 31))
        self.total_time_label.setStyleSheet("font: 14pt \"Berlin Sans FB\";\n"
                                            "\n"
                                            "background-color: rgb(85, 85, 255);\n"
                                            "color: rgb(255, 255, 255);")
        self.total_time_label.setObjectName("total_time_label")
        self.remaining_word_label = QtWidgets.QLabel(self.game_widget)
        self.remaining_word_label.setGeometry(QtCore.QRect(20, 70, 251, 31))
        self.remaining_word_label.setStyleSheet("font: 14pt \"Berlin Sans FB\";\n"
                                                "\n"
                                                "background-color: rgb(85, 85, 255);\n"
                                                "color: rgb(255, 255, 255);")
        self.remaining_word_label.setObjectName("remaining_word_label")
        self.pushButton = QtWidgets.QPushButton(self.game_widget)
        self.pushButton.setGeometry(QtCore.QRect(730, 40, 51, 51))
        self.pushButton.setStyleSheet("font: 20pt \"Berlin Sans FB\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      ";border-radius:20px;\n"
                                      "background-color: rgb(255, 0, 0);")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(55, 55))
        self.pushButton.setObjectName("pushButton")
        self.timer = QtWidgets.QLabel(self.game_widget)
        self.timer.setGeometry(QtCore.QRect(370, 120, 51, 51))
        self.timer.setStyleSheet("font: 30pt \"Berlin Sans FB\";\n"
                                 "color: rgb(0, 0, 127);\n"
                                 ";border-radius:20px;\n"
                                 "background-color: rgb(255, 255, 255);")
        self.timer.setObjectName("timer")
        self.label = QtWidgets.QLabel(self.game_widget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 851, 91))
        self.label.setStyleSheet("\n"
                                 "background-color: rgb(85, 85, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.wordcard_label.raise_()
        self.green_button.raise_()
        self.red_button.raise_()
        self.level_label.raise_()
        self.total_time_label.raise_()
        self.remaining_word_label.raise_()
        self.pushButton.raise_()
        self.timer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Words game"))
        self.wordcard_label.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>asd</p></body></html>"))
        self.wordcard_label.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p>English word</p></body></html>"))
        self.wordcard_label.setText(_translate("MainWindow", "Dutch\n"
                                               "\n"
                                               "Word"))
        self.level_label.setText(_translate("MainWindow", "Level : "))
        self.total_time_label.setText(
            _translate("MainWindow", "Total Time : "))
        self.remaining_word_label.setText(
            _translate("MainWindow", "Remaining  word : "))
        self.timer.setText(_translate("MainWindow", " 3"))
        self.pushButton.clicked.connect(self.back)

        for id in user.get_level_words():
            self.wordcard_label.setText(_translate(
                "MainWindow", {user.wordsdata[id]["Dutch"]}))

    def back(self):
        self.menuscreenui = Menuscreen_window()
        self.menuscreenui.setupUi(MainWindow)
        Users.save_to_json(user)
        welcomescreenui.setmenuscreenforuser()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
welcomescreenui = Welcomescreen_window()
menuscreenui = Menuscreen_window()
wordscreenui = Wordscreen_window()
welcomescreenui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
