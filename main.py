#https://github.com/leonid1123/PK42-demoexam-start2
# создать БД, импортировать таблицы tovar, user_import
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow,\
QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from db_manager import Db
from base_window import BaseWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Авторизация')
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QGridLayout()
        main_widget.setLayout(layout)
        layout.addWidget(QLabel("Логин"),0,0)
        layout.addWidget(QLabel("Пароль"),1,0)
        self.login_text = QLineEdit()
        self.pass_text = QLineEdit()
        layout.addWidget(self.login_text,0,1)
        layout.addWidget(self.pass_text,1,1)
        self.login_btn = QPushButton("Войти")
        self.login_btn.clicked.connect(self.login_handler)
        self.guest_btn = QPushButton("Гостевой вход")
        self.guest_btn.clicked.connect(self.guest_handler)
        layout.addWidget(self.login_btn,2,0,1,2)
        layout.addWidget(self.guest_btn,3,0,1,2)
        self.db = Db()
        if self.db.cnx is None:
            QMessageBox.critical(self,'Всё плохо!!!','Всё плохо с БД')
        self.show()

    def login_handler(self):
        pass

    def guest_handler(self):
        self.base_window = BaseWindow()
        self.base_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    