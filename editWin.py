from PyQt6.QtWidgets import QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton,\
QListWidget
from PyQt6.QtCore import pyqtSlot

class MainWindow(QWidget):
    """Класс окна для редактирования и добавления товаров"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Редактирование")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.set_ui()

    def set_ui(self):
        """метод для создания интерфейса"""
        self.artikul = QLineEdit()
        self.name = QLineEdit()
        self.izmerenie = QLineEdit()
        self.price = QLineEdit()
        self.postav = QLineEdit()
        self.proizv = QLineEdit()
        self.kategory = QLineEdit()
        self.skidka = QLineEdit()
        self.kolvo = QLineEdit()
        self.opisanie = QLineEdit()
        self.edit_btn = QPushButton("Изменить")
        self.add_btn = QPushButton("Добавить")
        self.layout.addWidget(QLabel("Артикул"),0,0)
        self.layout.addWidget(QLabel("Наименование товара"),1,0)
        self.layout.addWidget(QLabel("Единица измерения"),2,0)
        self.layout.addWidget(QLabel("Цена"),3,0)
        self.layout.addWidget(QLabel("Поставщик"),4,0)
        self.layout.addWidget(QLabel("Производитель"),5,0)
        self.layout.addWidget(QLabel("Категория"),6,0)
        self.layout.addWidget(QLabel("Действующая скидка"),7,0)
        self.layout.addWidget(QLabel("Количество на складе"),8,0)
        self.layout.addWidget(QLabel("Описание товара"),9,0)
        self.layout.addWidget(self.artikul,0,1)
        self.layout.addWidget(self.name,1,1)
        self.layout.addWidget(self.izmerenie,2,1)
        self.layout.addWidget(self.price,3,1)
        self.layout.addWidget(self.postav,4,1)
        self.layout.addWidget(self.proizv,5,1)
        self.layout.addWidget(self.kategory,6,1)
        self.layout.addWidget(self.skidka,7,1)
        self.layout.addWidget(self.kolvo,8,1)
        self.layout.addWidget(self.opisanie,9,1)
        self.layout.addWidget(self.edit_btn,10,0)
        self.layout.addWidget(self.add_btn,10,1)
        #сигналы
        self.edit_btn.clicked.connect(self.edit_tovar_slot)
        self.add_btn.clicked.connect(self.add_tovar_slot)
    
    @pyqtSlot()
    def edit_tovar_slot(self):
        """слот для редактирования товара"""
        pass

    @pyqtSlot()
    def add_tovar_slot(self):
        """слот для добавления товара"""
        pass
