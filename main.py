from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.Handler.MainWindowSlotFunc import MainWindowFunc
from DBConnect.connectDB import MyDataBase
from Calculate.DoCalculate import Calculator

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindowFunc()
    MainWindow.show()
    sys.exit(app.exec_())
