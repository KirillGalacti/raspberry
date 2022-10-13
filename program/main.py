from PyQt6.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui import Ui_Form
import sys

class MainWindow:
    def __init__(self):
        self.window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        
    
    def show(self):
        self.window.show()

        


if __name__ == '__main__':
    # Приложению нужен один (и только один) экземпляр QApplication.
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
    # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
    app = QApplication([])
    # Создаём виджет Qt — окно.
    window = MainWindow()
    window.show()  
    # Важно: окно по умолчанию скрыто.
    # Запускаем цикл событий.
    sys.exit(app.exec_())  
    # Приложение не доберётся сюда, пока вы не выйдете и цикл
    # событий не остановится.