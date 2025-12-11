from typing import Any
from PyQt6.QtWidgets import QApplication, QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, \
QMessageBox
from PyQt6.QtCore import pyqtSlot
import sys


class LoginWin(QMainWindow):
    """Класс окна для авторизации"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
app = QApplication(sys.argv)
login_win = LoginWin()
sys.exit(app.exec())
