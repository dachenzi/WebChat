# _*_ coding:utf-8 _*_


import sys
from PyQt5.QtWidgets import *
from uis.ui_webchatmain import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WidWebChatMain(QWidget):  # QWidget不带菜单的窗体

    def __init__(self, chat_, parent=None):
        """

        :param chat_:  聚合关系(调用辅助类: webchathelper )
        :param parent:  依赖父窗口时，需要传递，不依赖时为None
                        (该参数默认就为None，如果明确没有父窗体可以不指定)
        """

        super().__init__(parent=parent)

        # 窗体的大小
        # self.setGeometry(100, 100, 800, 600)

        # 窗体的titil
        # self.setWindowTitle('尽情聊天吧')

        # 将传入的helper函数绑定给实例本身
        self.chat = chat_

        # 实例化一个Qt生成的主窗体
        self.ui_main = Ui_Form()

        # 将主窗体绑定给实例本身
        self.ui_main.setupUi(self)

        # self.setWindowFlags(Qt.CustomizeWindowHint)

        # 窗体是否显示，统一由app来控制
        # self.show()

        # 处理chat发送过来的信号
        self.chat.sign_comming_msg.connect(self.show_msg)

        # 创建一个数据模型
        self.model = QStandardItemModel()
        self.ui_main.listView.setModel(self.model)

        # 绑定信号处理
        self.ui_main.listView.clicked.connect(self.select_user)
        # 点击信号(事件)
        self.ui_main.pushButton.clicked.connect(self.send_msg)

    def show_msg(self, msg):
        self.setWindowTitle(msg)

    def select_user(self, index):
        # 获取当前用户
        row = index.row()

        # 得到点击的用户的ID
        self.current_user = self.model.item(row).data()

    def send_msg(self):
        # 获取文本消息
        msg = self.ui_main.lineEdit.text()
        # 发送（辅助类）
        self.chat.send_msg(self.current_user, msg)

    def show_user_list(self):
        # 调用辅助类获取列表
        lst_users = self.chat.get_friends()
        # 显示列表到列表框
        for user_ in lst_users:
            user_name = user_['UserName']  # 发送时使用的用户ID
            nick_name = user_['NickName']  # 显示用户的昵称
            icon_head = QIcon('images/user.png')
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.model.appendRow(item_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_main = WidWebChatMain()
    sys.exit(app.exec())  # 返回状态码
