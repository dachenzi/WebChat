# _*_ coding:utf-8 _*_

"""
作用： 组合界面，业务封装，形成独立的应用逻辑
"""

from helpers.webchathelper import *
from uis.dlgqrlogin import *
from uis.widwebchatmain import *


class WebChatApp(QObject):
    """
    负责组合登录界面，聊天界面,微信访问模块，形成微信聊天的功能
    """

    def __init__(self, parent=None):
        """

        :param chat_:  聚合关系(调用辅助类: webchathelper )
        :param parent:  依赖父窗口时，需要传递，不依赖时为None
                        (该参数默认就为None，如果明确没有父窗体可以不指定)
        """
        super().__init__(parent=parent)  # 是否添加父组件

        # 聚合关系(将使用的二个窗体(登录和主页)和服务组件聚合进行聚合)
        self.chat = WebChatHelper()  # 聚合helper类
        self.ui_login = DlgQRLogin(self.chat)  # 聚合登录窗体，通过聚合关系将辅助类，注入给登录窗体
        self.ui_main = WidWebChatMain(self.chat)  # 聚合主窗体，通过聚合关系将辅助类，注入给主窗体

        # 应用程序运行时，启动登录窗口
        self.ui_login.show()

        # 主窗口此时是隐藏状态,登录成功后交换状态(login hide,main show)
        # self.ui_main.hide()

        # 把信号注册给show_chat_main
        self.chat.sign_login_ok.connect(self.show_chat_main)

        # 启动辅助类
        self.chat.start()

    def show_chat_main(self):
        # 隐藏登录
        self.ui_login.hide()
        # 释放登录
        self.ui_login.destroy()
        # 发起主窗体的用户列表
        self.ui_main.show_user_list()

        # 显示主窗体
        self.ui_main.show()
