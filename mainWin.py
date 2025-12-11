from typing import Any
from PyQt6.QtWidgets import QWidget,\
QGridLayout, QLabel, QLineEdit, QPushButton,\
QListWidget, QComboBox
from PyQt6.QtCore import pyqtSlot
from db_handler import DbHandler

class MainWindow(QWidget):
    """Класс окна для отображения товаров и работы с товарами"""
    def __init__(self, fio, role, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.FIO = fio
        self.ROLE = role 
        self.setWindowTitle(f"{fio} {role}")
        self.setGeometry(50,50,1024,500)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.set_ui()
        self.my_db = DbHandler()
        self.get_all_goods()
        self.populate_filter()

    def set_ui(self) -> None:
        """метод создания интерфейса"""
        self.main_lst = QListWidget()
        self.search_txt = QLineEdit()
        self.search_txt.setFixedWidth(512)
        self.filter_box = QComboBox()
        self.sort_up_btn = QPushButton("вверх")
        self.sort_down_btn = QPushButton("вниз")
        self.layout.addWidget(self.main_lst,0,0,1,2)
        self.layout.addWidget(self.search_txt,1,0)
        self.layout.addWidget(self.filter_box,1,1)
        self.layout.addWidget(self.sort_up_btn,2,0)
        self.layout.addWidget(self.sort_down_btn,2,1)
        #сигналы
        if self.ROLE in ['Администратор','Менеджер']:
            self.sort_up_btn.clicked.connect(self.sort_up_slot)
            self.sort_down_btn.clicked.connect(self.sort_down_slot)
            self.filter_box.activated.connect(self.filter_slot)
            self.search_txt.textChanged.connect(self.search_slot)
            self.main_lst.itemClicked.connect(self.edit_entry_slot)
        else:
            self.sort_up_btn.setVisible(False)
            self.sort_down_btn.setVisible(False)
            self.search_txt.setVisible(False)
            self.filter_box.setVisible(False)


    def get_all_goods(self) -> None:
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar;'
        self.my_db.cursor.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
        while ans:
            txt: str = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]};"
            self.main_lst.addItem(txt)
            ans = self.my_db.cursor.fetchone()

    def populate_filter(self) -> None:
        self.filter_box.clear()
        self.filter_box.addItem('Все поставщики')
        sql = 'SELECT DISTINCT `Поставщик` FROM tovar;'
        self.my_db.cursor.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
        while ans:
            self.filter_box.addItem(str(ans[0]))
            ans = self.my_db.cursor.fetchone()



    @pyqtSlot()
    def sort_up_slot(self) -> None:
        """слот для сортировки по возрастанию"""
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar ORDER BY `Кол-во на складе` ASC;'
        self.my_db.cursor.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
        while ans:
            txt: str = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]};"
            self.main_lst.addItem(txt)
            ans = self.my_db.cursor.fetchone()

    @pyqtSlot()
    def sort_down_slot(self) -> None:
        """слот для сортировки по убыванию"""
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar ORDER BY `Кол-во на складе` DESC;'
        self.my_db.cursor.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
        while ans:
            txt: str = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]};"
            self.main_lst.addItem(txt)
            ans = self.my_db.cursor.fetchone()

    @pyqtSlot()
    def filter_slot(self):
        """слот для фильтрации по поставщикам"""
        sql = 'SELECT * FROM tovar WHERE `Поставщик` = %s;'
        if self.filter_box.currentText() == 'Все поставщики':
            self.get_all_goods()
        else:
            self.main_lst.clear()
            self.my_db.cursor.execute(sql,(self.filter_box.currentText(),))
            ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
            while ans:
                txt: str = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]};"
                self.main_lst.addItem(txt)
                ans = self.my_db.cursor.fetchone()



    @pyqtSlot()
    def search_slot(self) -> None:
        """слот для поиска по введенным словам"""
        txt: str = "%" + self.search_txt.text() + "%"
        sql = 'SELECT * from tovar WHERE `Наименование товара` LIKE %s'
        self.my_db.cursor.execute(sql,(txt,))
        ans: tuple[Any, ...] | None = self.my_db.cursor.fetchone()
        self.main_lst.clear()
        while ans:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]};"
            self.main_lst.addItem(txt)
            ans = self.my_db.cursor.fetchone()


    @pyqtSlot()
    def edit_entry_slot(self) -> None:
        """слот для перехода в окно редактирования записей"""
        pass

