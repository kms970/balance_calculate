import pymysql

HOST = 'dalogisdb.cn1pvuxm8ev6.us-east-2.rds.amazonaws.com'
PORT = 3306
USER = 'kkhan97'
PASSWORD = 'grandmaster1'

DBconnection = pymysql.connect(host=HOST,port=PORT,user=USER,password=PASSWORD)

if DBconnection.open:
    with DBconnection.cursor() as curs:
        print("connected")

DBconnection.close()