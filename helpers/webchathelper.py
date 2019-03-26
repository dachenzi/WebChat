# _*_ coding:utf-8 _*_


import itchat
from PyQt5.QtCore import *


class WebChatHelper(QThread):
    # 二维码获取成功的信号，通过信号来传递信息（信号与槽函数）
    sign_qr = pyqtSignal(bytes)  # 定义信号，字节流为bytes格式

    # 登录成功的信号
    sign_login_ok = pyqtSignal()  # 没有数据，就可以不用传递参数

    # 接受消息信号
    sign_coming_msg = pyqtSignal(str)


    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def run(self):

        @itchat.msg_register(msgType=itchat.content.TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
        def recv_msg(msg):   # 嵌套函数
            if msg['MsgType'] == 1:
                self.sign_coming_msg.emit(msg['Content'])
            print(type(msg))

        # 登录
        itchat.login(
            qrCallback=self.qr_callback,  # 获取二维码后回调的函数，传递uuid,status,qr_code三个参数
            loginCallback=self.login_callback,  # 登录成功后的回调函数
        )

        # 死循环
        itchat.run()

    def qr_callback(self, uuid, status, qrcode):
        """

        :param uuid: wechat 返回的uuid
        :param status: 访问的状态码,状态为0，表示UUID生成成功
        :param qrcode:  返回的二维码图片
        :return:
        """
        # 信号发射器，将收到的二维码进行发送(图片为bytes格式)
        self.sign_qr.emit(qrcode)

    def login_callback(self):
        print('登录成功')
        # 发射登录成功信号
        self.sign_login_ok.emit()

    def get_friends(self):
        lst_user = []
        friends = itchat.get_friends()  # 获取用户列表

        for friend_ in friends:  # 每个元素是一个用户对象
            user = dict()
            user['NickName'] = friend_['NickName']
            user['UserName'] = friend_['UserName']
            lst_user.append(user)  # 构建用户列表信息

        return lst_user

    def send_msg(self, user_, msg_):
        itchat.send_msg(msg=msg_, toUserName=user_)

