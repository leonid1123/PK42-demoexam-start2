import pymysql.cursors


class DbHandler():
    """класс для работы с базой данных"""
    def __init__(self) -> None:
        self.conn = pymysql.connect(
            host="localhost",
            user="pk42",
            password="1234",
            database="demo_pk42_new"
        )
        self.cursor = self.conn.cursor()
