from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.Handler.MainWindowSlotFunc import MainWindowFunc
from DBConnect.connectDB import MyDataBase

if __name__ == "__main__":
    import sys
    print(MyDataBase().ConnectDataBase())
    app = QApplication(sys.argv)
    MainWindow = MainWindowFunc()
    MainWindow.show()
    sys.exit(app.exec_())
