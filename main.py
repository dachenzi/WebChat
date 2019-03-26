# _*_ coding:utf-8 _*_
from PyQt5.QtWidgets import *
import app.webchatapp
import sys

# 构建一个Qt application，通过命令行传递数据，注意它的参数是最少要是一个空列表
qt_app = QApplication(sys.argv)

# 启动webchatapp应用
webchat = app.webchatapp.WebChatApp()

# 启动qt application，退出时的状态码，交给sys退出时的状态码。
sys.exit(qt_app.exec())
