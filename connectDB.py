import pymysql

HOST = 'dalogisdb.cn1pvuxm8ev6.us-east-2.rds.amazonaws.com'
PORT = 3306
USER = 'kkhan97'
PASSWORD = 'grandmaster1'

def ConnectDataBase():
    DBconnection = pymysql.connect(host=HOST,port=PORT,user=USER,password=PASSWORD)

    try:
        with DBconnection.cursor() as curs:
            curs=DBconnection.cursor()
            sql="select * from List.CoupangList"
            curs.execute(sql)
            data=curs.fetchall()
            for row in data:
                print(row)
    finally:
        DBconnection.close()