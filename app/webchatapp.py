# _*_ coding:utf-8 _*_

from PyQt5.QtCore import *
from uis.dlgqrlogin import *
from uis.widwebchatmain import *
from tencents.webchathelper import *


class WebChatApp(QObject):

    def __init__(self, parent=None):
        """

        :param chat_:  聚合关系(调用辅助类: webchathelper )
        :param parent:  依赖父窗口时，需要传递，不依赖时为None
                        (该参数默认就为None，如果明确没有父窗体可以不指定)
        """
        super().__init__(parent=parent)  # 是否添加父组件

        # 聚合关系(将使用的二个窗体(登录和主页)和服务组件聚合进行聚合)
        self.chat = WebChatHelper()  # 聚合helper类
        self.ui_login = DlgQRLogin(self.chat)     # 聚合登录窗体，通过聚合关系将辅助类，注入给登录窗体
        self.ui_main = WidWebChatMain(self.chat)  # 聚合主窗体，通过聚合关系将辅助类，注入给主窗体

        # 应用程序运行时，启动登录窗口
        self.ui_login.show()

        # 主窗口此时是隐藏状态,登录成功后交换状态(login hide,main show)
        self.ui_main.hide()
