# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 818)
        Form.setStyleSheet(u"QPushButton{\n"
"	background-color: #0d6efd;\n"
"	color: #fff;\n"
"	width: 50px;\n"
"	height: 75px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	padding-left:10px ;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 40px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea()
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 864, 1065))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 13, 0, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 9, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 8, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 6, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 12, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 10, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 11, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 7, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0443\u043c", None))
    # retranslateUi

