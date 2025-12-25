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
        self.add_tovar = QPushButton("добавить товар")
        layout.addWidget(self.search,0,0,1,2)
        layout.addWidget(self.sort_up_btn,1,0)
        layout.addWidget(self.sort_down_btn,1,1)
        layout.addWidget(self.main_lst,2,0,1,2)
        layout.addWidget(self.add_tovar,3,0)
        layout.addWidget(self.zakaz_btn,3,1)
        if role not in ["Администратор", "Менеджер"]:
            self.search.setVisible(False)
            self.sort_down_btn.setVisible(False)
            self.sort_up_btn.setVisible(False)
            self.zakaz_btn.setVisible(False)
            self.add_tovar.setVisible(False)
        if role == "Администратор":
            self.add_tovar.setVisible(True)
