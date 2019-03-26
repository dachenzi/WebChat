# _*_ coding:utf-8 _*_


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from uis.ui_webchatmain import *


class WidWebChatMain(QWidget):

    def __init__(self, chat_, parent=None):
        """

        :param chat_:  聚合关系(调用辅助类: webchathelper )
        :param parent:  依赖父窗口时，需要传递，不依赖时为None
                        (该参数默认就为None，如果明确没有父窗体可以不指定)
        """

        super().__init__(parent=parent)

        # 将传入的helper函数绑定给实例本身
        self.chat = chat_

        # 实例化一个Qt生成的主窗体
        self.ui_main = Ui_Form()

        # 将主窗体绑定给实例本身
        self.ui_main.setupUi(self)

        # self.setWindowFlags(Qt.CustomizeWindowHint)

        # 窗体是否显示，统一由app来控制
        # self.show()


if __name__ == '__main__':
    # 测试，需要打开窗体的show函数，来显示登录窗体
    app = QApplication(sys.argv)
    ui_main = WidWebChatMain()
    sys.exit(app.exec())  # 返回状态码
