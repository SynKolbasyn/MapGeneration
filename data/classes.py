import sys
from random import randint

from data import functions as fun
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel  # all imports
from PIL import Image
from PyQt6.QtGui import QPixmap
id_name = 0

class ShowWindow(QMainWindow):
    def __init__(self, name, size):
        super().__init__()
        x, y = size  # we need to create the window dynamically cuz we cant know its sizes
        self.setGeometry(200, 300, x + 50, y + 50)
        self.setWindowTitle('Result')
        self.pixmap = QPixmap(f'generated/{name}.png')
        self.image = QLabel(self)
        self.image.move(50, 50)
        self.image.setPixmap(self.pixmap)


class MainWindow(QMainWindow):
    global id_name
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/main_wind.ui', self)
        self.create.clicked.connect(self.creating)
        self.open_b.clicked.connect(self.opening)

    def creating(self) -> None:
        palette = list()
        palette.append(fun.colors(self.color1))
        palette.append(fun.colors(self.color2))
        palette.append(fun.colors(self.color3))
        palette.append(fun.colors(self.color4))
        palette.append(fun.colors(self.color5))
        palette.append(fun.colors(self.color6))
        palette = [palette[i] for i in range(6) if palette[i] is not None]
        try:
            file_name = self.filename.text()
        except Exception as _:
            file_name = str(randint(0, 100)) + str(id_name)

        try:
            size = tuple(map(int, self.size.text().split('*')))
        except Exception as _:
            size = (40, 40)
        fun.creating_func(size, file_name, palette)
        ap = QApplication(sys.argv)
        exi = ShowWindow(file_name, size)
        exi.show()
        sys.exit(ap.exec())  # I have troubles here - it is closing and I dont understand why :(

    def opening(self):
        name = self.name_db.text()
        img = fun.db_request(name)
