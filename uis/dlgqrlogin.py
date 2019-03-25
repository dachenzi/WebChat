# _*_ coding:utf-8 _*_


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import uis.ui_login
import sys


# 对话框窗体
class DlgQRLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)  # 父窗体,有可能显示不出来

        self.ui_login = uis.ui_login.Ui_ui_login()  # 创建一个窗体
        self.ui_login.setupUi(self)  # 对话框和窗体绑定在一起

        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.show()  # 显示窗体


if __name__ == '__main__':

    # 监听每一个窗体的事件
    app = QApplication([])    #  QApplication(sys.argv) 传递命令行参数

    dlg = DlgQRLogin()

    app.exec()