########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *

import RPi.GPIO as GPIO
import time
import smbus

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################
#SLAVE ADDRESS
bus = smbus.SMBus(1)

SLAVE_ADDRESS_1 = 0x08
SLAVE_ADDRESS_2 = 0x09
SLAVE_ADDRESS_3 = 0x0a
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################

        ## PAGES
        ########################################################################
        self.ui.btn_page_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))

        # PAGE LEARN
        ########################################################################
        self.ui.one_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_one_learn))

        self.ui.two_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_two_learn))

        self.ui.three_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_three_learn))

        self.ui.four_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_four_learn))

        self.ui.five_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_five_learn))

        self.ui.six_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_six_learn))

        self.ui.seven_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_seven_learn))

        self.ui.eight_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eight_learn))

        self.ui.nine_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_nine_learn))

        self.ui.ten_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ten_learn))

        self.ui.eleven_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eleven_learn))

        self.ui.twelve_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_twelve_learn))

        self.ui.theerteen_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_theerteen_learn))

        self.ui.fourteen_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fourteen_learn))

        #PAGES ROBOT ARMS

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  