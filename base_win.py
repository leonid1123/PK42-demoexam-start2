from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QListWidget
from typing import Any
from PyQt6.QtWidgets import QApplication, QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, \
QMessageBox, QListWidget, QComboBox

class BaseWindow(QWidget):
    """класс окна для списка товаров"""
    def __init__(self, fio:str, role:str) -> None:
        """Конструктор класса.
        Аргументы:
        fio -- ФИО пользователя
        role -- роль пользователя
        """
        super().__init__()
        self.setWindowTitle(f"{fio}, {role}")
        layout = QGridLayout()
        self.setLayout(layout)
        self.main_lst = QListWidget()
        self.search = QLineEdit()
        self.filter = QComboBox()
        self.sort_up_btn = QPushButton("по убыванию")
        self.sort_down_btn = QPushButton("по возрастанию")
        self.zakaz_btn = QPushButton("заказы")
