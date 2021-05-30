import pymysql
import pandas as pd

HOST = 'dalogisdb.cn1pvuxm8ev6.us-east-2.rds.amazonaws.com'
PORT = 3306
USER = 'kkhan97'
PASSWORD = 'grandmaster1'

class MyDataBase:
    def __init__(self):
       self.DataBaseDataFrame = pd.DataFrame()

    def ConnectDataBase(self):
        DBconnection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)

        try:
            with DBconnection.cursor() as curs:
                curs = DBconnection.cursor(pymysql.cursors.DictCursor)
                connectSql = "select * from List.PurchaseList"
                curs.execute(connectSql)
                data = curs.fetchall()
                self.DataBaseDataFrame = pd.DataFrame(data)
                #print(self.DataBaseDataFrame)

                return self.DataBaseDataFrame
        finally:
            DBconnection.close()
