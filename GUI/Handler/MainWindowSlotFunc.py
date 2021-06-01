from GUI.CalculateDialog import *
from GUI.MainDialog import Ui_MainWindow

from PyQt5.QtCore import QDate


class MainWindowFunc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindowFunc, self).__init__(parent)
        self.setupUi(self)
        self.calculate_window = CalculateDialogFunc(self)
        self.at_to.dateChanged.connect(self.is_date_true)
        self.do_calculate.clicked.connect(self.do_calculate_button)

    def do_calculate_button(self):
        if self.at_from.date().daysTo(self.at_to.date()) < 0:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("날짜오류")
            msgBox.setText("날짜를 조정해주세요")
            self.at_from.setDate(self.at_to.date())
            msgBox.exec_()

        else:
            self.calculate_window.CalculateAtTo.setText(self.at_to.date().toString('yyyy-MM-dd'))
            self.calculate_window.CalculateAtFrom.setText(self.at_from.date().toString('yyyy-MM-dd'))
            print(self.at_from.date().daysTo(self.at_to.date()))
            #self.calculate_window.CalculateLabel.
            self.calculate_window.show()

    def is_date_true(self):
        if self.at_to.date().daysTo(QDate.currentDate()) < 0:
            self.at_to.setDate(QDate.currentDate())

class CalculateDialogFunc(QtWidgets.QDialog, Ui_CalculateDialog):
    def __init__(self, parent=None):
        super(CalculateDialogFunc, self).__init__(parent)
        self.setupUi(self)
