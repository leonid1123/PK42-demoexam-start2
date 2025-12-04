import pymysql.cursors


class DbHandler():
    """класс для работы с базой данных"""
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="pk42",
            password="1234",
            database="pk42_demo"
        )
        self.cursor = self.conn.cursor()
