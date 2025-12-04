from PyQt6.QtWidgets import QApplication, QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt6.QtCore import pyqtSlot
import sys
from mainWin import MainWindow

class LoginWin(QMainWindow):
    """Класс окна для авторизации"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Вход")
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QGridLayout()
        main_widget.setLayout(self.layout)
        self.set_ui()
        self.show()


    def set_ui(self):
        """метод для создания интерфейса"""
        self.login_entry = QLineEdit()
        self.pass_entry = QLineEdit()
        self.login_btn = QPushButton("Вход")
        self.guest_btn = QPushButton("Гость")
        self.layout.addWidget(QLabel("Логин"),0,0)
        self.layout.addWidget(QLabel("Пароль"),1,0)
        self.layout.addWidget(self.login_entry,0,1)
        self.layout.addWidget(self.pass_entry,1,1)
        self.layout.addWidget(self.login_btn,2,0,1,2)
        self.layout.addWidget(self.guest_btn,3,0,1,2)
        #сигналы
        self.login_btn.clicked.connect(self.user_login_slot)
        self.guest_btn.clicked.connect(self.guest_login_slot)

    @pyqtSlot()
    def user_login_slot(self):
        """слот для входа по логину и паролю"""
        pass

    @pyqtSlot()
    def guest_login_slot(self):
        """слот для гостевого входа"""
        self.main_window = MainWindow()
        self.main_window.show()

app = QApplication(sys.argv)
login_win = LoginWin()
sys.exit(app.exec())
