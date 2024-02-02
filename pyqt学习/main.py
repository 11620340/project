import json, time, requests

from PyQt5 import QtWidgets, QtCore, uic

import login_modle

class login(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi(r'.\ui\login.ui', self)
        self.pushButton_login.clicked.connect(self.login)


    def login(self):
        self.dict_user_pawd = {"username":self.lineEdit_user.text(),"password":self.lineEdit_password.text()}


        self.thread_login = login_modle.LoginThread(self.dict_user_pawd)
        self.thread_login.signal_login.connect(self.set_text)
        self.thread_login.start()

    def set_text(self, main_signal_login):
        self.textBrowser.setText(main_signal_login)


app = QtWidgets.QApplication([])
login_window = login()
login_window.show()
app.exec_()