import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
import datetime
import pymysql
from dotenv import load_dotenv


form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCombo()
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.pushButton_3.clicked.connect(self.comboSelect)
        self.actionExit.triggered.connect(self.appExit)

    def btn_clicked(self):
        coinlist = pykorbit.get_tickers()
        for coins in coinlist:
            self.textBrowser.append(str(coins))
            self.textBrowser_2.append(str(coins))
            price3 = pykorbit.get_current_price(str(coins))
            order3 = pykorbit.get_orderbook(str(coins))
            self.textBrowser.append(str(format(price3, ",")))
            self.textBrowser_2.append(str(format(price3, ",")))
            bids = order3["bids"]
            asks = order3["asks"]
            timestmp = order3["timestamp"]
            self.textBrowser.append(str(datetime.datetime.fromtimestamp(timestmp / 1000)))
            self.textBrowser_2.append(str(datetime.datetime.fromtimestamp(timestmp / 1000)))
            self.textBrowser.append("**** BIDS ********")
            bidamt = 0.0
            for bidlist in bids:
                bidamt = bidamt + float(bidlist[1])
            self.textBrowser.append("Bid Amount")
            self.textBrowser.append(str(bidamt))
            self.textBrowser.append("******************")
            self.textBrowser_2.append("******ASKS ********")
            askamt = 0.0
            for asklist in asks:
                askamt = askamt + float(asklist[1])
            self.textBrowser_2.append("ASK Amount")
            self.textBrowser_2.append(str(askamt))
            self.textBrowser_2.append("***********************")

    def btn2_clicked(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.label_3.clear()
        self.label_6.clear()
        self.label_7.clear()
        self.label_9.clear()
        self.label_11.clear()
        self.label_13.clear()
        self.label_15.clear()


    def setCombo(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        coinlist = pykorbit.get_tickers()
        for coins in coinlist:
            self.comboBox.addItem(str(coins))
            self.comboBox_2.addItem(str(coins))

    def appExit(self,QCloseEvent):
        re = QMessageBox.question(self, "Exit App.", "종료 하시겠습니까?",
                                  QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def comboSelect(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.label_3.clear()
        self.label_6.clear()
        self.label_7.clear()
        coins = self.comboBox.currentText()
        price3 = pykorbit.get_current_price(str(coins))
        order3 = pykorbit.get_orderbook(str(coins))
        self.label_9.setText(str(format(price3, ",")))
        bids = order3["bids"]
        asks = order3["asks"]
        timestmp = order3["timestamp"]
        self.label_11.setText(str(datetime.datetime.fromtimestamp(timestmp / 1000)))
        self.textBrowser.append("*** BIDS ******")
        bidamt = 0.0
        bidtotal = 0.0
        bidsub = 0.0
        for bidlist in bids:
            self.textBrowser.append(str(bidlist))
            bidsub = float(bidlist[0])*float(bidlist[1])
            bidtotal = bidtotal + bidsub
            bidamt = bidamt + float(bidlist[1])
        self.textBrowser.append("Bid Amount")
        self.textBrowser.append(str(format(bidamt,",")))
        self.label_6.setText(str(format(bidamt,",")))
        self.label_13.setText(str(format(round(bidtotal), ",")))
        self.textBrowser.append("**************************")
        self.textBrowser_2.append("**** ASKS ****")
        askamt =0.0
        asktotal = 0.0
        asksub = 0.0
        for asklist in asks:
            self.textBrowser_2.append(str(asklist))
            asksub = float(asklist[0])* float(asklist[1])
            asktotal = asktotal + asksub
            askamt = askamt + float(asklist[1])
        self.textBrowser_2.append("ASK Amount")
        self.textBrowser_2.append(str(format(askamt,",")))
        self.label_7.setText(str(format(askamt, ",")))
        self.label_15.setText(str(format(round(asktotal), ",")))
        self.textBrowser_2.append("************************")
        if askamt >= bidamt :
            self.label_3.setText("하락추세")
        else:
            self.label_3.setText("상승추세")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()