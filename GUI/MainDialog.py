# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\balance_calculate\GUI\MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from GUI.CalculateDialog import Ui_CalculateDialog
from RequestOrder import RequestOrderList


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(618, 374)
        MainWindow.setStyleSheet("background-color: rgb(47, 49, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(185, 187, 190);")
        self.today_time = QtWidgets.QLabel(self.centralwidget)
        self.today_time.setGeometry(QtCore.QRect(120, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.today_time.setFont(font)
        self.today_time.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 581, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(116, 124, 136);\n"
"color: rgb(234, 234, 234);\n"
"background-color: rgb(81, 86, 95);")
        self.first_sales_name = QtWidgets.QLabel(self.groupBox)
        self.first_sales_name.setGeometry(QtCore.QRect(10, 20, 441, 16))
        self.second_sales_name = QtWidgets.QLabel(self.groupBox)
        self.second_sales_name.setGeometry(QtCore.QRect(10, 50, 441, 16))
        self.third_sales_name = QtWidgets.QLabel(self.groupBox)
        self.third_sales_name.setGeometry(QtCore.QRect(10, 80, 441, 16))
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(460, 20, 41, 20))
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(460, 50, 41, 20))
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(460, 80, 41, 20))
        self.first_sales = QtWidgets.QLabel(self.groupBox)
        self.first_sales.setGeometry(QtCore.QRect(510, 20, 56, 21))
        self.second_sales = QtWidgets.QLabel(self.groupBox)
        self.second_sales.setGeometry(QtCore.QRect(510, 50, 56, 21))
        self.third_sales = QtWidgets.QLabel(self.groupBox)
        self.third_sales.setGeometry(QtCore.QRect(510, 80, 56, 21))
        self.show_graph = QtWidgets.QPushButton(self.centralwidget)
        self.show_graph.setGeometry(QtCore.QRect(180, 290, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_graph.setFont(font)
        self.show_graph.setStyleSheet("background-color: rgb(81, 86, 95);\n"
"color: rgb(234, 234, 234);\n"
"")
        self.show_table = QtWidgets.QPushButton(self.centralwidget)
        self.show_table.setGeometry(QtCore.QRect(340, 290, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_table.setFont(font)
        self.show_table.setStyleSheet("background-color: rgb(81, 86, 95);\n"
"color: rgb(234, 234, 234);\n"
"")
        self.show_orderlist = QtWidgets.QPushButton(self.centralwidget)
        self.show_orderlist.setGeometry(QtCore.QRect(500, 290, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_orderlist.setFont(font)
        self.show_orderlist.setStyleSheet("background-color: rgb(81, 86, 95);\n"
"color: rgb(234, 234, 234);")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 180, 581, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(234, 234, 234);\n"
"background-color: rgb(81, 86, 95);")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.at_from = QtWidgets.QDateEdit(self.groupBox_2)
        self.at_from.setGeometry(QtCore.QRect(90, 30, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.at_from.setFont(font)
        self.at_from.setStyleSheet("color: rgb(255, 255, 255);")
        self.at_from.setFrame(False)
        self.at_from.setCalendarPopup(True)
        self.at_from.setDate(QDate.currentDate())
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.at_to = QtWidgets.QDateEdit(self.groupBox_2)
        self.at_to.setGeometry(QtCore.QRect(340, 30, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.at_to.setFont(font)
        self.at_to.setStyleSheet("color: rgb(255, 255, 255);")
        self.at_to.setFrame(False)
        self.at_to.setCalendarPopup(True)
        self.at_to.setDate(QDate.currentDate())
        self.do_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.do_calculate.setGeometry(QtCore.QRect(20, 290, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.do_calculate.setFont(font)
        self.do_calculate.setStyleSheet("color: rgb(234, 234, 234);\n"
"background-color: rgb(81, 86, 95);\n"
"background-color: rgb(81, 86, 95);")
        self.do_calculate.setObjectName("do_calculate")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.do_calculate.clicked.connect(self.button1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "정산프로그램"))
        self.label_3.setText(_translate("MainWindow", "현재날짜"))
        self.today_time.setText(_translate("MainWindow", str(QDate.currentDate().toString('yyyy-MM-dd'))))
        self.groupBox.setTitle(_translate("MainWindow", "판매순위"))
        self.first_sales_name.setText(_translate("MainWindow", "TextLabel"))
        self.second_sales_name.setText(_translate("MainWindow", "TextLabel"))
        self.third_sales_name.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "판매량"))
        self.label_8.setText(_translate("MainWindow", "판매량"))
        self.label_9.setText(_translate("MainWindow", "판매량"))
        self.first_sales.setText(_translate("MainWindow", "TextLabel"))
        self.second_sales.setText(_translate("MainWindow", "TextLabel"))
        self.third_sales.setText(_translate("MainWindow", "TextLabel"))
        self.show_graph.setText(_translate("MainWindow", "정산그래프보기"))
        self.show_table.setText(_translate("MainWindow", "물품목록보기"))
        self.show_orderlist.setText(_translate("MainWindow", "물품추가하기"))
        self.groupBox_2.setTitle(_translate("MainWindow", "정산 날짜 선택"))
        self.label.setText(_translate("MainWindow", "시작일"))
        self.label_2.setText(_translate("MainWindow", "종료일"))
        self.do_calculate.setText(_translate("MainWindow", "정산하기"))


    def button1(self):
        date_to=self.at_to.date().toString("yyyy-MM-dd")
        date_from=self.at_from.date().toString("yyyy-MM-dd")
        # a=RequestOrderList.RequestOrder()
        # b=a.RequestOrderVendorId(1,date_to,date_from)
        # print(b)
        CalculateDialog = QtWidgets.QDialog()
        ui = Ui_CalculateDialog()
        ui.setupUi(CalculateDialog)
        CalculateDialog.show()
        CalculateDialog.exec_()