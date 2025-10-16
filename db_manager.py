import mysql.connector

class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user='pk-42',
            password='1234',
            database='pupsik64'
        )
        self.cur = self.cnx.cursor()