# GUI Imports
import sys
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QMainWindow,
    QTextEdit
)
from functools import partial

from window_sort import WindowSort



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowSort()
    window.show()
    sys.exit(app.exec())



