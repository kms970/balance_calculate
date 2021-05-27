import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QScrollArea, \
    QTableWidget, QTableWidgetItem
from Calculate import DoCalculate
from PyQt5.QtCore import Qt
import pandas as pd


class MyApp(QWidget):
    dc = DoCalculate.Calculator()
    df = pd.DataFrame()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self)
        btn1.setText('정산')

        self.table = QTableWidget()
        scroll = QScrollArea()
        scroll.setWidget(self.table)

        self.label_calculate = QLabel("정산액표시", self)
        label_font = self.label_calculate.font()
        label_font.setPointSize(20)
        self.label_calculate.setFont(label_font)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(self.table)
        vbox.addWidget(self.label_calculate)

        btn1.clicked.connect(self.btn1_clicked)

        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.move(300, 300)
        self.resize(1000, 500)
        self.show()

    def btn1_clicked(self):
        MyApp.df = MyApp.dc.selectOrderItems()
        self.label_calculate.setText(str(MyApp.dc.calculate())+"원")

        print(MyApp.df)
        self.table.setColumnCount(len(MyApp.df.columns))
        self.table.setRowCount(len(MyApp.df.index))
        self.table.setHorizontalHeaderLabels(['주문번호', '결제날짜', '옵션ID', '판매가격', '배송비유무'])
        for i in range(len(MyApp.df.index)):
            for j in range(len(MyApp.df.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(MyApp.df.iloc[i, j])))
