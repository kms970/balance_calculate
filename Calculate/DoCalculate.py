from DBConnect import connectDB
from RequestOrder import RequestOrderList
import pandas as pd


class Calculator:
    def __init__(self):
        self.orderItems = pd.DataFrame(columns=['orderId', 'vendorItemId', 'orderPrice', 'deliveryChargeTypeName'])

    def selectOrderItems(self, all_dataframe):
        self.orderItems['orderId'] = all_dataframe['orderId']
        vendorItemId=[]
        orderPrice=[]
        deliveryChargeTypeName=[]
        for i in all_dataframe['orderItems']:
            for data in i:
                vendorItemId.append(data['vendorItemId'])
                orderPrice.append(data['orderPrice'])
                deliveryChargeTypeName.append(data['deliveryChargeTypeName'])

        # print("가격: ", orderPrice)
        # print("옵션 번호: ", vendorItemId)

        self.orderItems['vendorItemId'] = vendorItemId
        self.orderItems['orderPrice'] = orderPrice
        self.orderItems['deliveryChargeTypeName'] = deliveryChargeTypeName

        #print(order_items)
        return self.orderItems

    # orderId,vendorItemId,orderPrice,deliveryChargeTypeName
    # deliveryChargeTypeName /유료배송은 택배비=410원 남음
    # 반품은 반품건에 대해서 따로 정산이 됨

    def calculate(self):
        request_order=RequestOrderList.RequestOrder()
        all_dataframe = request_order.allDatafromAPI()
        mainDataFrame = pd.DataFrame(connectDB.MyDataBase().ConnectDataBase())

        orderItems = self.selectOrderItems(all_dataframe)

        print(orderItems)
