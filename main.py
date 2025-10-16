import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow,\
QGridLayout, QLabel, QLineEdit, QPushButton


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



        self.show()

    def login_handler(self):
        pass

    def guest_handler(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())