from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, \
    QPushButton, QMessageBox, QListWidget
from PyQt6.QtGui import QColor
from db_manager import Db

class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Основное окно')
        self.setGeometry(10,50,1280,720)
        layout = QGridLayout()
        self.setLayout(layout)
        self.user_role = QLabel('гость')
        layout.addWidget(self.user_role,0,0)
        self.goods_lst = QListWidget()
        layout.addWidget(self.goods_lst,1,0)
        self.exit_btn = QPushButton('Выход')
        self.exit_btn.clicked.connect(self.close_window)
        layout.addWidget(self.exit_btn,2,0)
        self.db = Db()
        self.get_all_boots()

    def close_window(self):
        self.close()

    def get_all_boots(self):
        sql = 'SELECT * FROM tovar;'
        self.db.cur.execute(sql)
        ans = self.db.cur.fetchone()
        k=0
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item +', ')
            self.goods_lst.addItem(tmp_str)
            if str(ans[7]).isdigit():
                if int(ans[7]) >15:
                    self.goods_lst.item(k).setBackground(QColor("red"))
            if str(ans[8]).isdigit():
                if int(ans[8]) == 0:
                    self.goods_lst.item(k).setBackground(QColor("lightGray"))
            ans = self.db.cur.fetchone()
            k+=1
        