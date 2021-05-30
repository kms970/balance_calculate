from typing import Type

from PyQt5.QtWidgets import QDialog

from GUI.CalculateDialog import *
from GUI.MainDialog import Ui_MainWindow


class MainWindowFunc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindowFunc, self).__init__(parent)
        self.setupUi(self)
        self.calculate_window = CalculateDialogFunc(self)
        self.do_calculate.clicked.connect(self.do_calculate_button)

    def do_calculate_button(self):
        self.calculate_window.CalculateAtTo.setText(self.at_to.date().toString('yyyy-MM-dd'))
        self.calculate_window.CalculateAtFrom.setText(self.at_from.date().toString('yyyy-MM-dd'))
        #self.calculate_window.CalculateLabel.
        self.calculate_window.show()

class CalculateDialogFunc(QtWidgets.QDialog,Ui_CalculateDialog):
    def __init__(self, parent=None):
        super(CalculateDialogFunc, self).__init__(parent)
        self.setupUi(self)
