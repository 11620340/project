import json, time, requests

from PyQt5 import QtWidgets, QtCore, uic


class LoginThread(QtCore.QThread):
    signal_login = QtCore.pyqtSignal(str)
    def __init__(self, dict_user_pawd):
        super().__init__()
        self.dict_user_pawd = dict_user_pawd



    def run(self):
        self.signal_login.emit('waiting login...')
        self.response = requests.get('https://97a7ea5e244c4a1d801166104cef719e.apig.cn-east-3.huaweicloudapis.com/test', params=self.dict_user_pawd)
        print(self.response.text)
        self.signal_login.emit(self.response.text)

