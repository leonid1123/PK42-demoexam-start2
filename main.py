from typing import Any
from PyQt6.QtWidgets import QApplication, QWidget,\
QFormLayout, QLabel, QLineEdit, QPushButton, QMainWindow, \
QMessageBox
import sys
from base_win import BaseWindow


class LoginWindow(QMainWindow):
    """Класс окна для авторизации"""
    def __init__(self) -> None:
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QFormLayout()
        central_widget.setLayout(layout)
        login_input = QLineEdit()
        pass_input = QLineEdit()
        pass_login_btn = QPushButton("Вход")
        pass_login_btn.clicked.connect(self.pass_login)
        guest_login_btn = QPushButton("Гостевой вход")
        guest_login_btn.clicked.connect(self.pass_login)
        layout.addRow("логин", login_input)
        layout.addRow("пароль", pass_input)
        layout.addRow(pass_login_btn)
        layout.addRow(guest_login_btn)
        self.show()

    def guest_login(self) -> None:
        """метод для входа по логину и паролю"""
        self.bw = BaseWindow("гость", "гость")
        self.bw.show()

    def pass_login(self) -> None:
        """метод для гостевого входа"""
        self.bw = BaseWindow("ФИО", "админ")
        self.bw.show()
        

app = QApplication(sys.argv)
login_win = LoginWindow()
sys.exit(app.exec())
