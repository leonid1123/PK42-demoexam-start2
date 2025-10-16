#USE PyMySQL!!!
import pymysql.cursors

class Db:
    def __init__(self):
        try:
            self.cnx = pymysql.connect(
            host="localhost",
            user='pk42',
            password='1234',
            database='demo_pk42_new'
            )
            self.cur = self.cnx.cursor()
        except pymysql.Error as e:
            print("Ошибка БД", e)
            self.cnx = None
            self.cur = None
