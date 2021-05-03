from DBConnect import connectDB
import pandas as pd
from RequestOrder import RequestOrderList

if __name__ == '__main__':
    mainDataFrame = pd.DataFrame(connectDB.MyDataBase().ConnectDataBase())
    #print(mainDataFrame)
    nextPage=1
    while True:
        df=RequestOrderList.RequestOrderVendorId(nextPage)
        nextPage=df['nextToken']
        print(df)
        if(nextPage==''):
            break

