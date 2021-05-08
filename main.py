from DBConnect import connectDB
import pandas as pd
from RequestOrder import RequestOrderList
from Calculate import DoCalculate

if __name__ == '__main__':
    print("hello")
    dc=DoCalculate.Calculator()
    dc.calculate()