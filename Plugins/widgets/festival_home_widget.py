from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout


class FestivalHomeWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_layout()

    def set_layout(self):
        title = QLabel('Browse All Festivals')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 1)

        self.setLayout(grid)
