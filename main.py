import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
import json


form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        price1 = pykorbit.get_current_price("BTC")
        price2 = pykorbit.get_current_price("ETH")
        price3 = pykorbit.get_current_price("FIL")
        order1 = pykorbit.get_orderbook("BTC")
        order2 = pykorbit.get_orderbook("ETH")
        order3 = pykorbit.get_orderbook("FIL")
        self.textBrowser.append(str(format(price1,",")))
        self.textBrowser.append(str(order1))
        self.textBrowser.append(" ")
        self.textBrowser.append(str(format(price2, ",")))
        self.textBrowser.append(str(order2))
        self.textBrowser.append(" ")
        self.textBrowser.append(str(format(price3, ",")))
        self.textBrowser.append(str(order3))
        self.textBrowser.append(" ")
        self.textBrowser.append("*************************************************")

    def btn2_clicked(self):
        self.textBrowser.clear()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




