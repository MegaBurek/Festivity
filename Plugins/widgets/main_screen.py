from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget

from Plugins.widgets.festival_home_widget import FestivalHomeWidget

from API.usersAPI import login


class MainScreen(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_layout()

    def set_layout(self):

        title = QLabel('Festival Ticket Program')
        company_logo = QLabel(self)

        username_label = QLabel('Username: ')
        password_label = QLabel('Password: ')

        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()

        self.festivalHomeWidget = FestivalHomeWidget()

        self.window = QWidget()

        self.logIn_button = QPushButton()
        self.logIn_button.setObjectName("login")
        self.logIn_button.setText("Login")
        self.connect(self.logIn_button, SIGNAL(
            "clicked()"), self.login_attempt)

        self.register_button = QPushButton()
        self.register_button.setObjectName("register")
        self.register_button.setText("Register")

        pixmap = QPixmap('resources/festivity_logo.png')
        company_logo.setPixmap(pixmap)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.logIn_button)
        hbox.addWidget(self.register_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 1)

        grid.addWidget(company_logo, 2, 1)

        grid.addWidget(username_label, 3, 0)
        grid.addWidget(self.username_edit, 3, 1)

        grid.addWidget(password_label, 4, 0)
        grid.addWidget(self.password_edit, 4, 1)

        grid.addLayout(vbox, 5, 1)

        self.setLayout(grid)
        self.window.show()

    def login_attempt(self):
        username_attempt = self.username_edit.text()
        password_attempt = self.password_edit.text()
        if(login(username_attempt, password_attempt)):
            self.window.setParent(None)
            self.window.setParent(self.festivalHomeWidget)
        else:
            print("False")
