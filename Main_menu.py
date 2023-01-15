import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush, QPixmap


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main_menu.ui', self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/MainFon.jpg")))
        self.setPalette(pal)
        self.logo.resize(300, 300)
        self.pixmap = QPixmap('./data/Logo_comp.png')
        self.logo.setPixmap(self.pixmap)
        self.exit.clicked.connect(self.Exit)

    def Exit(self):
        uic.loadUi("Exit.ui", self)
        self.Yes.clicked.connect(self.Yes_Exit)
        self.pushButton_2.clicked.connect(self.No_Exit)

    def No_Exit(self):
        print('Завершение')

    def Yes_Exit(self):
        print('назад')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
