import pymysql.cursors

class DbHandler:
    def __init__(self) -> None:
        """
        класс для работы с базой данных
        Параметры:
        conn -- подключение к БД
        cur -- курсор, для создания запросов
        """
        self.conn = pymysql.connect(
            host="localhost",
            user="",
            password="",
            database=""
        )
        self.cur = self.conn.cursor()


