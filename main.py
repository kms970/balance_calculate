from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from DBConnect import connectDB
import pandas as pd

from GUI.MainDialog import Ui_MainWindow
from RequestOrder import RequestOrderList
from Calculate import DoCalculate
from GUI import MainDialog

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())