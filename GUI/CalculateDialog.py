# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\balance_calculate\GUI\CalculateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculateDialog(object):
    def setupUi(self, CalculateDialog):
        CalculateDialog.setWindowModality(QtCore.Qt.WindowModal)
        CalculateDialog.resize(591, 540)
        CalculateDialog.setStyleSheet("background-color: rgb(47, 49, 54);")
        self.label = QtWidgets.QLabel(CalculateDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(234, 234, 234);")
        self.CalculateLabel = QtWidgets.QLabel(CalculateDialog)
        self.CalculateLabel.setGeometry(QtCore.QRect(130, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CalculateLabel.setFont(font)
        self.CalculateLabel.setStyleSheet("color: rgb(234, 234, 234);")
        self.label_2 = QtWidgets.QLabel(CalculateDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(234, 234, 234);")
        self.label_3 = QtWidgets.QLabel(CalculateDialog)
        self.label_3.setGeometry(QtCore.QRect(290, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(234, 234, 234);")
        self.label_3.setObjectName("label_3")
        self.CalculateAtFrom = QtWidgets.QLabel(CalculateDialog)
        self.CalculateAtFrom.setGeometry(QtCore.QRect(120, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CalculateAtFrom.setFont(font)
        self.CalculateAtFrom.setStyleSheet("color: rgb(234, 234, 234);")
        self.CalculateAtTo = QtWidgets.QLabel(CalculateDialog)
        self.CalculateAtTo.setGeometry(QtCore.QRect(380, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CalculateAtTo.setFont(font)
        self.CalculateAtTo.setStyleSheet("color: rgb(234, 234, 234);")
        self.OrderTab = QtWidgets.QTabWidget(CalculateDialog)
        self.OrderTab.setEnabled(True)
        self.OrderTab.setGeometry(QtCore.QRect(30, 130, 541, 371))
        self.OrderTab.setStyleSheet("background-color: rgb(81, 86, 95);\n"
"color: rgb(65, 69, 76);")
        self.OrderTab.setElideMode(QtCore.Qt.ElideLeft)
        self.OrderTab.setTabsClosable(False)
        self.OrderTab.setTabBarAutoHide(True)
        self.OrderTab.setObjectName("OrderTab")
        self.orderListTab = QtWidgets.QWidget()
        self.orderListTab.setObjectName("orderListTab")
        self.OrderTab.addTab(self.orderListTab, "")
        self.returnListTab = QtWidgets.QWidget()
        self.returnListTab.setObjectName("returnListTab")
        self.OrderTab.addTab(self.returnListTab, "")

        self.retranslateUi(CalculateDialog)
        self.OrderTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CalculateDialog)

    def retranslateUi(self, CalculateDialog):
        _translate = QtCore.QCoreApplication.translate
        CalculateDialog.setWindowTitle(_translate("CalculateDialog", "정산화면"))
        self.label.setText(_translate("CalculateDialog", "정산금액"))
        self.CalculateLabel.setText(_translate("CalculateDialog", "TextLabel"))
        self.label_2.setText(_translate("CalculateDialog", "시작날짜"))
        self.label_3.setText(_translate("CalculateDialog", "종료날짜"))
        self.CalculateAtFrom.setText(_translate("CalculateDialog", "정산금액시작"))
        self.CalculateAtTo.setText(_translate("CalculateDialog", "정산금액"))
        self.OrderTab.setTabText(self.OrderTab.indexOf(self.orderListTab), _translate("CalculateDialog", "주문내역"))
        self.OrderTab.setTabText(self.OrderTab.indexOf(self.returnListTab), _translate("CalculateDialog", "반품내역"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculateDialog = QtWidgets.QDialog()
    ui = Ui_CalculateDialog()
    ui.setupUi(CalculateDialog)
    CalculateDialog.show()
    sys.exit(app.exec_())
