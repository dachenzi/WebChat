# _*_ coding:utf-8 _*_
"""

"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import uis.ui_login


# 对话框窗体
class DlgQRLogin(QDialog):
    """
    二维码登录对话框
    """

    def __init__(self, char_, parent=None):
        """

        :param chat_:  聚合关系(调用辅助类: webchathelper )
        :param parent:  依赖父窗口时，需要传递，不依赖时为None
                        (该参数默认就为None，如果明确没有父窗体可以不指定)
        """

        super().__init__(parent=parent)

        # 窗体的位置数据
        # self.setGeometry(100, 100, 400, 300)

        # 窗体的标题
        # self.setWindowTitle('登录')

        self.chat = char_

        # 利用QT生成的窗体的实体对象，创建一个登录窗体
        self.ui_login = uis.ui_login.Ui_ui_login()

        # 将当前对话框和QT构建的窗体绑定在一起
        self.ui_login.setupUi(self)

        # 隐藏状态栏的头部信息
        # self.setWindowFlags(Qt.CustomizeWindowHint)

        # 是否显示，由应用统一控制显示
        # self.show()  # 显示窗体

        # 将辅助类中注册的sign_qr信号绑定给show_qr函数，这个函数叫做槽
        self.chat.sign_qr.connect(self.show_qr)

    # 当sign_qr被触发时，会调用该槽函数
    def show_qr(self, qrcode):
        img_qr = QImage.fromData(qrcode)  # 转换成图片文件
        pix_qr = QPixmap.fromImage(img_qr)  # 把图片转换为像素
        self.ui_login.lbl_qr.setPixmap(pix_qr)  # 设置登录框，加载二维码（像素）
        self.ui_login.lbl_qr.setScaledContents(True)  # Qt图片自适应窗口大小


if __name__ == '__main__':
    # 测试，需要打开窗体的show函数，来显示登录窗体
    app = QApplication([])  # QApplication(sys.argv) 传递命令行参数
    dlg = DlgQRLogin()
    app.exec()
