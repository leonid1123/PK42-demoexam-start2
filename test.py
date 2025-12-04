from PyQt6.QtWidgets import QApplication,\
QMainWindow, QWidget, QGridLayout,\
QPushButton
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("авторизация")
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QGridLayout()
        main_widget.setLayout(layout)
        self.btn = QPushButton("сигналоиздаватор")
        self.btn.clicked.connect(self.ubit_mishku)
        layout.addWidget(self.btn,0,0)
        self.show()

    def ubit_mishku(self):
        print("шлёп!")
        self.ne_main_win = NeMainWindow()
        self.ne_main_win.show()
        

class NeMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список товаров")
        layout = QGridLayout()
        self.setLayout(layout)
        self.btn = QPushButton("открыть окно")
        self.btn.clicked.connect(self.click2)
        layout.addWidget(self.btn,0,0)

    def click2(self):
        self.sub_window = SubWindow()
        self.sub_window.show()


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактор товаров")
        layout = QGridLayout()
        self.setLayout(layout)


app = QApplication(sys.argv)
login_window = LoginWindow()
sys.exit(app.exec())
