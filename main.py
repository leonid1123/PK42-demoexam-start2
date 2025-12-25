from typing import Any
from PyQt6.QtWidgets import QApplication, QWidget,\
QFormLayout, QLabel, QLineEdit, QPushButton, QMainWindow, \
QMessageBox
import sys
from base_win import BaseWindow
from db_handler import DbHandler


class LoginWindow(QMainWindow):
    """Класс окна для авторизации"""
    def __init__(self) -> None:
        super().__init__()
        self.my_db = DbHandler()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QFormLayout()
        central_widget.setLayout(layout)
        self.login_input = QLineEdit()
        self.pass_input = QLineEdit()
        pass_login_btn = QPushButton("Вход")
        pass_login_btn.clicked.connect(self.pass_login)
        guest_login_btn = QPushButton("Гостевой вход")
        guest_login_btn.clicked.connect(self.guest_login)
        layout.addRow("логин", self.login_input)
        layout.addRow("пароль", self.pass_input)
        layout.addRow(pass_login_btn)
        layout.addRow(guest_login_btn)
        self.show()

    def pass_login(self) -> None:
        """метод для входа по логину и паролю"""
        login: str = self.login_input.text()
        password:str = self.pass_input.text()
        sql = "SELECT * from user_import WHERE Логин=%s"
        self.my_db.cur.execute(sql, (login,))
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        if ans:
            if password == ans[3]:
                self.bw = BaseWindow(ans[1], ans[0])
                self.bw.show()
            else:
                print("ошибка входа")
        else:
            print("ошибка входа")

    def guest_login(self) -> None:
        """метод для гостевого входа"""
        self.bw = BaseWindow("гость", "гость")
        self.bw.show()
        

app = QApplication(sys.argv)
login_win = LoginWindow()
sys.exit(app.exec())
