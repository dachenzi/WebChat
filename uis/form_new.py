# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_new.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_new(object):
    def setupUi(self, Form_new):
        Form_new.setObjectName("Form_new")
        Form_new.resize(280, 370)
        self.lineEdit = QtWidgets.QLineEdit(Form_new)
        self.lineEdit.setGeometry(QtCore.QRect(60, 260, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(Form_new)
        self.widget.setGeometry(QtCore.QRect(40, 40, 186, 186))
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setObjectName("widget")

        self.retranslateUi(Form_new)
        QtCore.QMetaObject.connectSlotsByName(Form_new)

    def retranslateUi(self, Form_new):
        _translate = QtCore.QCoreApplication.translate
        Form_new.setWindowTitle(_translate("Form_new", "Form"))
        self.lineEdit.setText(_translate("Form_new", "请使用微信扫一扫登录"))


