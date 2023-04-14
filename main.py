import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
import datetime


form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        coinlist = pykorbit.get_tickers()
        for coins in coinlist:
            self.textBrowser.append(str(coins))
            price3 = pykorbit.get_current_price(str(coins))
            order3 = pykorbit.get_orderbook(str(coins))
            self.textBrowser.append(str(format(price3, ",")))
            bids = order3["bids"]
            asks = order3["asks"]
            timestmp = order3["timestamp"]
            self.textBrowser.append(str(datetime.datetime.fromtimestamp(timestmp / 1000)))
            self.textBrowser.append("**************** BIDS ****************************")
            for bidlist in bids:
                self.textBrowser.append(str(bidlist))
            self.textBrowser.append("***************** ASKS **************************")
            for asklist in asks:
                self.textBrowser.append(str(asklist))
            self.textBrowser.append(" ")
            self.textBrowser.append("*************************************************")

    def btn2_clicked(self):
        self.textBrowser.clear()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




