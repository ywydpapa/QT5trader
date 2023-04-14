import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
import datetime
import threading


form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCombo()
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.pushButton_3.clicked.connect(self.comboSelect)

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
            self.textBrowser.append("**** BIDS ********")
            for bidlist in bids:
                self.textBrowser.append(str(bidlist))
            self.textBrowser.append("******************")
            self.textBrowser_2.append("******ASKS ********")
            for asklist in asks:
                self.textBrowser_2.append(str(asklist))
            self.textBrowser_2.append(" ")
            self.textBrowser_2.append("***********************")

    def btn2_clicked(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()

    def setCombo(self):
        self.comboBox.clear()
        coinlist = pykorbit.get_tickers()
        for coins in coinlist:
            self.comboBox.addItem(str(coins))

    def comboSelect(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        coins = self.comboBox.currentText()
        self.textBrowser.append(str(coins))
        price3 = pykorbit.get_current_price(str(coins))
        order3 = pykorbit.get_orderbook(str(coins))
        self.textBrowser.append(str(format(price3, ",")))
        bids = order3["bids"]
        asks = order3["asks"]
        timestmp = order3["timestamp"]
        self.textBrowser.append(str(datetime.datetime.fromtimestamp(timestmp / 1000)))
        self.textBrowser.append("*** BIDS ******")
        bidamt = 0.0
        for bidlist in bids:
            self.textBrowser.append(str(bidlist))
            bidamt = bidamt + float(bidlist[1])
        self.textBrowser.append("Bid Amount")
        self.textBrowser.append(str(bidamt))
        self.textBrowser.append("**************************")
        self.textBrowser_2.append("**** ASKS ****")
        askamt =0.0
        for asklist in asks:
            self.textBrowser_2.append(str(asklist))
            askamt = askamt + float(asklist[1])
        self.textBrowser_2.append("ASK Amount")
        self.textBrowser_2.append(str(askamt))
        self.textBrowser_2.append("************************")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




