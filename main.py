from PyQt5.QtWidgets import QApplication
import sys
from DBConnect import connectDB
import pandas as pd
from RequestOrder import RequestOrderList
from Calculate import DoCalculate
from GUI import MainGUI

if __name__ == '__main__':
    print("hello")
    dc=DoCalculate.Calculator()
    dc.calculate()
    app = QApplication(sys.argv)
    ex = MainGUI.MyApp()
    sys.exit(app.exec_())