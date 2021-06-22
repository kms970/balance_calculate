import pymysql
import pandas as pd

HOST = '************'
PORT = 3306
USER = '************'
PASSWORD = '*********'


class MyDataBase:
    def __init__(self):
        self.DataBaseDataFrame = pd.DataFrame()

    def ConnectDataBase(self):
        DBconnection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)

        try:
            with DBconnection.cursor() as curs:
                curs = DBconnection.cursor(pymysql.cursors.DictCursor)
                connectSql = "select * from List.purchaseList;"
                curs.execute(connectSql)
                data = curs.fetchall()
                self.DataBaseDataFrame = pd.DataFrame(data)
                # print(self.DataBaseDataFrame)

                return self.DataBaseDataFrame
        finally:
            DBconnection.close()
