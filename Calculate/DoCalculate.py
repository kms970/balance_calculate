from DBConnect import connectDB
from RequestOrder import RequestOrderList
import pandas as pd


class Calculator:
    def __init__(self):
        self.orderItems = pd.DataFrame(columns=['orderId','paidAt', 'vendorItemId', 'orderPrice', 'deliveryChargeTypeName'])
        self.DBDataFrame = pd.DataFrame(connectDB.MyDataBase().ConnectDataBase())

    def selectOrderItems(self,date_to,date_from):
        #print(self.orderItems)
        all_order_dataframe = RequestOrderList.allDatafromAPI(date_to,date_from)
        print(all_order_dataframe)
        self.orderItems['orderId'] = all_order_dataframe['orderId']
        self.orderItems['paidAt'] = all_order_dataframe['paidAt']

        vendorItemId=[]
        orderPrice=[]
        deliveryChargeTypeName=[]
        for i in all_order_dataframe['orderItems']:
            for data in i:
                vendorItemId.append(data['vendorItemId'])
                orderPrice.append(data['orderPrice'])
                deliveryChargeTypeName.append(data['deliveryChargeTypeName'])

        # print("가격: ", orderPrice)
        # print("옵션 번호: ", vendorItemId)

        self.orderItems['vendorItemId'] = vendorItemId
        self.orderItems['orderPrice'] = orderPrice
        self.orderItems['deliveryChargeTypeName'] = deliveryChargeTypeName

        #print("정제쪽: ",self.orderItems)
        return self.orderItems

    # orderId,vendorItemId,orderPrice,deliveryChargeTypeName
    # deliveryChargeTypeName /유료배송은 택배비=410원 남음
    # 반품은 반품건에 대해서 따로 정산이 됨

    def calculate(self):
        calculate_sum=0
        orderItems = self.orderItems
        #print("정산쪽: ",self.orderItems)
        #print(self.DBDataFrame)
        for index, data in orderItems.iterrows():
            for db_index, db_data in self.DBDataFrame.iterrows():
                is_find_vendorid = str(db_data['option_id']) == str(data['vendorItemId'])
                # print("is_find: ", is_find_vendorid)
                if is_find_vendorid:
                    if data['deliveryChargeTypeName'] == '무료':
                        calculate_sum = calculate_sum + (((data['orderPrice'] * (1-db_data['coupang_fees'])) - db_data['delivery_fee']-db_data['purchase_price']) / db_data['sales_quantity'])
                    else:
                        calculate_sum = calculate_sum + ((data['orderPrice'] * (1-db_data['coupang_fees'])-db_data['purchase_price']) / db_data['sales_quantity'] + 410)

        return calculate_sum
