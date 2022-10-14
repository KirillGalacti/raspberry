# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 606)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_page_2 = QPushButton(self.page)
        self.btn_page_2.setObjectName(u"btn_page_2")

        self.verticalLayout_2.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.page)
        self.btn_page_3.setObjectName(u"btn_page_3")

        self.verticalLayout_2.addWidget(self.btn_page_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font-size:20px;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 722, 586))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_3 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_3.setObjectName(u"btn_3")

        self.verticalLayout_3.addWidget(self.btn_3)

        self.btn_4 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_4.setObjectName(u"btn_4")

        self.verticalLayout_3.addWidget(self.btn_4)

        self.btn_5 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_5.setObjectName(u"btn_5")

        self.verticalLayout_3.addWidget(self.btn_5)

        self.btn_10 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_10.setObjectName(u"btn_10")

        self.verticalLayout_3.addWidget(self.btn_10)

        self.btn_12 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_12.setObjectName(u"btn_12")

        self.verticalLayout_3.addWidget(self.btn_12)

        self.btn_2 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_2.setObjectName(u"btn_2")

        self.verticalLayout_3.addWidget(self.btn_2)

        self.btn = QPushButton(self.scrollAreaWidgetContents)
        self.btn.setObjectName(u"btn")

        self.verticalLayout_3.addWidget(self.btn)

        self.btn_6 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_6.setObjectName(u"btn_6")

        self.verticalLayout_3.addWidget(self.btn_6)

        self.btn_9 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_9.setObjectName(u"btn_9")

        self.verticalLayout_3.addWidget(self.btn_9)

        self.btn_14 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_14.setObjectName(u"btn_14")

        self.verticalLayout_3.addWidget(self.btn_14)

        self.btn_13 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_13.setObjectName(u"btn_13")

        self.verticalLayout_3.addWidget(self.btn_13)

        self.btn_11 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_11.setObjectName(u"btn_11")

        self.verticalLayout_3.addWidget(self.btn_11)

        self.btn_7 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_7.setObjectName(u"btn_7")

        self.verticalLayout_3.addWidget(self.btn_7)

        self.btn_8 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_8.setObjectName(u"btn_8")

        self.verticalLayout_3.addWidget(self.btn_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 722, 586))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_19 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_19.setObjectName(u"btn_19")

        self.verticalLayout.addWidget(self.btn_19)

        self.btn_20 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_20.setObjectName(u"btn_20")

        self.verticalLayout.addWidget(self.btn_20)

        self.btn_18 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_18.setObjectName(u"btn_18")

        self.verticalLayout.addWidget(self.btn_18)

        self.btn_17 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_17.setObjectName(u"btn_17")

        self.verticalLayout.addWidget(self.btn_17)

        self.btn_15 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_15.setObjectName(u"btn_15")

        self.verticalLayout.addWidget(self.btn_15)

        self.btn_21 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_21.setObjectName(u"btn_21")

        self.verticalLayout.addWidget(self.btn_21)

        self.btn_22 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_22.setObjectName(u"btn_22")

        self.verticalLayout.addWidget(self.btn_22)

        self.btn_27 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_27.setObjectName(u"btn_27")

        self.verticalLayout.addWidget(self.btn_27)

        self.btn_28 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_28.setObjectName(u"btn_28")

        self.verticalLayout.addWidget(self.btn_28)

        self.btn_26 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_26.setObjectName(u"btn_26")

        self.verticalLayout.addWidget(self.btn_26)

        self.btn_25 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_25.setObjectName(u"btn_25")

        self.verticalLayout.addWidget(self.btn_25)

        self.btn_23 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_23.setObjectName(u"btn_23")

        self.verticalLayout.addWidget(self.btn_23)

        self.btn_16 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_16.setObjectName(u"btn_16")

        self.verticalLayout.addWidget(self.btn_16)

        self.btn_24 = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_24.setObjectName(u"btn_24")

        self.verticalLayout.addWidget(self.btn_24)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_page_1 = QPushButton(self.frame_3)
        self.btn_page_1.setObjectName(u"btn_page_1")

        self.horizontalLayout_2.addWidget(self.btn_page_1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLabel{\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: rgb(85, 170, 255);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_roll = QPushButton(self.frame_5)
        self.btn_roll.setObjectName(u"btn_roll")

        self.horizontalLayout.addWidget(self.btn_roll)

        self.btn_close = QPushButton(self.frame_5)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout_2.addWidget(self.frame_5, 0, 2, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u0449\u0438\u0439 \u0432\u0430\u0441 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0443\u043c", None))
        self.btn_roll.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

