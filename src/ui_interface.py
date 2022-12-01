# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 612)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.btn_page_1 = QPushButton(self.frame_3)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_page_1.sizePolicy().hasHeightForWidth())
        self.btn_page_1.setSizePolicy(sizePolicy1)
        self.btn_page_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(185, 0, 3);\n"
"border-raduis: 10px\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon)
        self.btn_page_1.setCheckable(False)
        self.btn_page_1.setAutoRepeatDelay(300)

        self.horizontalLayout_5.addWidget(self.btn_page_1)

        self.btn_page_robot_hand = QPushButton(self.frame_3)
        self.btn_page_robot_hand.setObjectName(u"btn_page_robot_hand")
        sizePolicy1.setHeightForWidth(self.btn_page_robot_hand.sizePolicy().hasHeightForWidth())
        self.btn_page_robot_hand.setSizePolicy(sizePolicy1)
        self.btn_page_robot_hand.setStyleSheet(u"background-color:rgb(255, 255, 255) ")

        self.horizontalLayout_5.addWidget(self.btn_page_robot_hand)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	font-size: 20px;\n"
"	color: rgb(85, 170, 255)\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy3)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.main_body_contents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 772, 586))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_23 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout_4.addWidget(self.pushButton_23)

        self.pushButton_22 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout_4.addWidget(self.pushButton_22)

        self.pushButton_24 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_4.addWidget(self.pushButton_24)

        self.pushButton_20 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_4.addWidget(self.pushButton_20)

        self.pushButton_19 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_4.addWidget(self.pushButton_19)

        self.pushButton_25 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_4.addWidget(self.pushButton_25)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_4.addWidget(self.pushButton_26)

        self.pushButton_18 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_4.addWidget(self.pushButton_18)

        self.pushButton_21 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_4.addWidget(self.pushButton_21)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_4.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.verticalLayout_4.addWidget(self.pushButton_28)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 772, 586))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_3.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_17 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_16 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_3.addWidget(self.pushButton_16)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_3.addWidget(self.pushButton_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.btn_page_3 = QPushButton(self.page_1)
        self.btn_page_3.setObjectName(u"btn_page_3")

        self.verticalLayout_2.addWidget(self.btn_page_3)

        self.btn_page_2 = QPushButton(self.page_1)
        self.btn_page_2.setObjectName(u"btn_page_2")

        self.verticalLayout_2.addWidget(self.btn_page_2)

        self.stackedWidget.addWidget(self.page_1)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.main_body_contents)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_page_1, self.btn_page_robot_hand)
        QWidget.setTabOrder(self.btn_page_robot_hand, self.minimize_window_button)
        QWidget.setTabOrder(self.minimize_window_button, self.restore_window_button)
        QWidget.setTabOrder(self.restore_window_button, self.close_window_button)
        QWidget.setTabOrder(self.close_window_button, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_25)
        QWidget.setTabOrder(self.pushButton_25, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_26)
        QWidget.setTabOrder(self.pushButton_26, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_27)
        QWidget.setTabOrder(self.pushButton_27, self.pushButton_28)
        QWidget.setTabOrder(self.pushButton_28, self.btn_page_3)
        QWidget.setTabOrder(self.btn_page_3, self.btn_page_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_1.setText("")
        self.btn_page_robot_hand.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0443\u043c", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.pushButton_23.setText("")
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"1. ", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0438\u0439 \u0432\u0430\u0441 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
    # retranslateUi

