import sys
from data import functions as fun, classes as clss
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel  # all imports
from PIL import Image
from PyQt6.QtGui import QPixmap

# TODO: to fill in the requirements file


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = clss.MainWindow()
    ex.show()
    sys.exit(app.exec())

