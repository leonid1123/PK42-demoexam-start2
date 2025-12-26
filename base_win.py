from typing import Any

from PyQt6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QLineEdit,
    QListWidget,
    QPushButton,
    QWidget,
)

from db_handler import DbHandler


class BaseWindow(QWidget):
    """класс окна для списка товаров"""

    def __init__(self, fio: str, role: str) -> None:
        """Конструктор класса.
        Аргументы:
        fio -- ФИО пользователя
        role -- роль пользователя
        """
        super().__init__()
        self.my_db = DbHandler()  # объект для работы с БД
        self.setWindowTitle(f"{fio}, {role}")
        layout = QGridLayout()
        self.setLayout(layout)
        self.main_lst = QListWidget()
        self.search = QLineEdit()
        self.search.textChanged.connect(self.search_text_method)
        self.filter = QComboBox()
        self.filter.activated.connect(self.get_filter)
        self.sort_up_btn = QPushButton("по убыванию")
        self.sort_up_btn.clicked.connect(self.sort_up)
        self.sort_down_btn = QPushButton("по возрастанию")
        self.sort_down_btn.clicked.connect(self.sort_down)
        self.zakaz_btn = QPushButton("заказы")
        self.add_tovar = QPushButton("добавить товар")
        layout.addWidget(self.search, 0, 0, 1, 2)
        layout.addWidget(self.sort_up_btn, 1, 0)
        layout.addWidget(self.sort_down_btn, 1, 1)
        layout.addWidget(self.main_lst, 2, 0, 1, 2)
        layout.addWidget(self.add_tovar, 3, 0)
        layout.addWidget(self.zakaz_btn, 3, 1)
        layout.addWidget(self.filter, 4, 0, 1, 2)
        self.get_all_goods()  # вызов метода для заполнения списка товаров
        self.populate_filter()  # вызов метода для заполнения списка поставщиков
        # убрать элементы для Гостя
        if role not in ["Администратор", "Менеджер"]:
            self.search.setVisible(False)
            self.sort_down_btn.setVisible(False)
            self.sort_up_btn.setVisible(False)
            self.zakaz_btn.setVisible(False)
            self.add_tovar.setVisible(False)
            self.filter.setVisible(False)
        if (
            role == "Администратор"
        ):  # кнопка добавления товаров только для Администратора
            self.add_tovar.setVisible(True)

    def get_all_goods(self):
        """
        метод для заполнения списка товаров
        """
        sql = " SELECT * FROM tovar"
        self.my_db.cur.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        self.main_lst.clear()
        while ans:
            self.main_lst.addItem(
                f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[6]} {ans[7]} {ans[8]} {ans[9]}"
            )
            ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()

    def sort_up(self):
        """
        метод для сортировки списка товаров
        """
        sql = " SELECT * FROM tovar ORDER BY `Кол-во на складе` ASC"
        self.my_db.cur.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        self.main_lst.clear()
        while ans:
            self.main_lst.addItem(
                f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[6]} {ans[7]} {ans[8]} {ans[9]}"
            )
            ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()

    def sort_down(self):
        """
        метод для сортировки списка товаров
        """
        sql = " SELECT * FROM tovar ORDER BY `Кол-во на складе` DESC"
        self.my_db.cur.execute(sql)
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        self.main_lst.clear()
        while ans:
            self.main_lst.addItem(
                f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[6]} {ans[7]} {ans[8]} {ans[9]}"
            )
            ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()

    def search_text_method(self):
        """
        метод для поиска по описанию.
        переделать для поиска по всем текстовым полям
        """
        txt = self.search.text().strip()
        txt = "%" + txt + "%"
        sql = " SELECT * FROM tovar WHERE `Описание товара` LIKE %s"
        self.my_db.cur.execute(sql, (txt,))
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        self.main_lst.clear()
        while ans:
            self.main_lst.addItem(
                f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[6]} {ans[7]} {ans[8]} {ans[9]}"
            )
            ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()

    def populate_filter(self):
        """
        метод заполнения списка поставщиков
        """
        sql = "SELECT DISTINCT `Производитель` FROM tovar"
        self.my_db.cur.execute(sql)
        ans = self.my_db.cur.fetchone()
        while ans:
            self.filter.addItem(f"{ans[0]}")
            ans = self.my_db.cur.fetchone()

    def get_filter(self):
        """
        метод для отображения товаров по выбранному поставщику
        """
        sql = " SELECT * FROM tovar WHERE `Производитель`=%s"
        self.my_db.cur.execute(sql, (self.filter.currentText(),))
        ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
        self.main_lst.clear()
        while ans:
            self.main_lst.addItem(
                f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[6]} {ans[7]} {ans[8]} {ans[9]}"
            )
            ans: tuple[Any, ...] | None = self.my_db.cur.fetchone()
