from DBConnect import connectDB
from RequestOrder import RequestOrderList
import pandas as pd

class Calculator:
    mainDataFrame = pd.DataFrame(connectDB.MyDataBase().ConnectDataBase())
    #print(mainDataFrame)
    all_dataframe = RequestOrderList.allDatafromAPI()

    #print(all_dataframe)

    #print(all_dataframe['orderItems'])
    def selectOrderItems(self, all_dataframe):
        for i in all_dataframe['orderItems']:
            for data in i:
                print("data =", data['vendorItemId'])

    # vendorItemId
    # deliveryChargeTypeName /유료배송은 택배비=410원 남음
    # 반품은 반품건에 대해서 따로 정산이 됨

    def calculate(self):
        print('hello')