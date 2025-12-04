from PyQt6.QtWidgets import QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton,\
QListWidget, QComboBox
from PyQt6.QtCore import pyqtSlot

class MainWindow(QWidget):
    """Класс окна для отображения товаров и работы с товарами"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Товары")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.set_ui()

    def set_ui(self):
        """метод создания интерфейса"""
        self.main_lst = QListWidget()
        self.search_txt = QLineEdit()
        self.filter_box = QComboBox()
        self.sort_up_btn = QPushButton("вверх")
        self.sort_down_btn = QPushButton("вниз")
        self.layout.addWidget(self.main_lst,0,0,1,2)
        self.layout.addWidget(self.search_txt,1,0)
        self.layout.addWidget(self.filter_box,1,1)
        self.layout.addWidget(self.sort_up_btn,2,0)
        self.layout.addWidget(self.sort_down_btn,2,1)
        #сигналы
        self.sort_up_btn.clicked.connect(self.sort_up_slot)
        self.sort_down_btn.clicked.connect(self.sort_down_slot)
        self.filter_box.activated.connect(self.filter_slot)
        self.search_txt.textChanged.connect(self.search_slot)
        self.main_lst.itemClicked.connect(self.edit_entry_slot)

    @pyqtSlot()
    def sort_up_slot(self):
        """слот для сортировки по возрастанию"""
        pass

    @pyqtSlot()
    def sort_down_slot(self):
        """слот для сортировки по убыванию"""
        pass

    @pyqtSlot()
    def filter_slot(self):
        """слот для фильтрации по поставщикам"""
        pass

    @pyqtSlot()
    def search_slot(self):
        """слот для поиска по введенным словам"""
        pass

    @pyqtSlot()
    def edit_entry_slot(self):
        """слот для перехода в окно редактирования записей"""
        pass

