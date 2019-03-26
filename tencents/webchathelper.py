# _*_ coding:utf-8 _*_


from PyQt5.QtCore import *
import requests
import datetime
import re


class WebChatHelper(QThread):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.api_login = 'https://login.wx.qq.com/jslogin'
        self.redirect_uri = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage'
        self.appid = 'wx782c26e4c19acffb'
        self.fun = 'new'
        self.lang = 'zh_CN'
        self.timestamp = int(datetime.datetime.now().timestamp() * 1000)

    def get_qr(self):
        res = requests.get(self.api_login,
                           params={'appid': self.appid, 'redirect_uri': self.redirect_uri, 'func': self.fun,
                                   'lang': self.lang, '_': self.timestamp})

        self.qr_code = re.search(r'.*"(.*)".*', res.text).group(1)






app = WebChatHelper()
app.get_qr()
