# _*_ coding:utf-8 _*_


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from uis.ui_webchatmain import *


class WidWebChatMain(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui_main = Ui_Form()
        self.ui_main.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui_main = WidWebChatMain()

    sys.exit(app.exec())   # 返回状态码
