# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chartWidget.ui'
#
# Created: Tue Jan  4 04:06:29 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_chartWidget(object):
    def setupUi(self, chartWidget):
        chartWidget.setObjectName("chartWidget")
        chartWidget.resize(1076, 1056)
        self.tabWidget = QtGui.QTabWidget(chartWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 870, 841, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.chartControls = QtGui.QWidget()
        self.chartControls.setObjectName("chartControls")
        self.zoomIn = QtGui.QPushButton(self.chartControls)
        self.zoomIn.setGeometry(QtCore.QRect(290, 10, 110, 29))
        self.zoomIn.setObjectName("zoomIn")
        self.zoomOut = QtGui.QPushButton(self.chartControls)
        self.zoomOut.setGeometry(QtCore.QRect(290, 80, 110, 29))
        self.zoomOut.setObjectName("zoomOut")
        self.chartLength = QtGui.QLabel(self.chartControls)
        self.chartLength.setGeometry(QtCore.QRect(310, 50, 71, 19))
        self.chartLength.setObjectName("chartLength")
        self.candlestick = QtGui.QPushButton(self.chartControls)
        self.candlestick.setGeometry(QtCore.QRect(460, 20, 110, 29))
        self.candlestick.setObjectName("candlestick")
        self.ohlc = QtGui.QPushButton(self.chartControls)
        self.ohlc.setGeometry(QtCore.QRect(460, 50, 110, 29))
        self.ohlc.setObjectName("ohlc")
        self.line = QtGui.QFrame(self.chartControls)
        self.line.setGeometry(QtCore.QRect(420, 10, 16, 101))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.chartControls)
        self.line_2.setGeometry(QtCore.QRect(700, 10, 16, 101))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtGui.QLabel(self.chartControls)
        self.label.setGeometry(QtCore.QRect(520, 0, 91, 19))
        self.label.setObjectName("label")
        self.symbolEntry = QtGui.QLineEdit(self.chartControls)
        self.symbolEntry.setGeometry(QtCore.QRect(20, 30, 221, 29))
        self.symbolEntry.setObjectName("symbolEntry")
        self.loadSymbol = QtGui.QPushButton(self.chartControls)
        self.loadSymbol.setGeometry(QtCore.QRect(20, 70, 110, 29))
        self.loadSymbol.setObjectName("loadSymbol")
        self.newTab = QtGui.QPushButton(self.chartControls)
        self.newTab.setGeometry(QtCore.QRect(130, 70, 110, 29))
        self.newTab.setObjectName("newTab")
        self.line_4 = QtGui.QFrame(self.chartControls)
        self.line_4.setGeometry(QtCore.QRect(250, 10, 16, 101))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.hlc = QtGui.QPushButton(self.chartControls)
        self.hlc.setGeometry(QtCore.QRect(460, 80, 110, 29))
        self.hlc.setObjectName("hlc")
        self.bar = QtGui.QPushButton(self.chartControls)
        self.bar.setGeometry(QtCore.QRect(570, 20, 110, 29))
        self.bar.setObjectName("bar")
        self.dot = QtGui.QPushButton(self.chartControls)
        self.dot.setGeometry(QtCore.QRect(570, 50, 110, 29))
        self.dot.setObjectName("dot")
        self.close = QtGui.QPushButton(self.chartControls)
        self.close.setGeometry(QtCore.QRect(570, 80, 110, 29))
        self.close.setObjectName("close")
        self.tabWidget.addTab(self.chartControls, "")
        self.account = QtGui.QWidget()
        self.account.setObjectName("account")
        self.buy = QtGui.QPushButton(self.account)
        self.buy.setGeometry(QtCore.QRect(20, 40, 110, 29))
        self.buy.setObjectName("buy")
        self.sell = QtGui.QPushButton(self.account)
        self.sell.setGeometry(QtCore.QRect(20, 80, 110, 29))
        self.sell.setObjectName("sell")
        self.showBalance = QtGui.QLabel(self.account)
        self.showBalance.setGeometry(QtCore.QRect(550, 40, 111, 20))
        self.showBalance.setObjectName("showBalance")
        self.label_balance = QtGui.QLabel(self.account)
        self.label_balance.setGeometry(QtCore.QRect(420, 40, 81, 19))
        self.label_balance.setObjectName("label_balance")
        self.buyShares = QtGui.QLineEdit(self.account)
        self.buyShares.setGeometry(QtCore.QRect(140, 40, 113, 29))
        self.buyShares.setObjectName("buyShares")
        self.sellShares = QtGui.QLineEdit(self.account)
        self.sellShares.setGeometry(QtCore.QRect(140, 80, 113, 29))
        self.sellShares.setObjectName("sellShares")
        self.line_3 = QtGui.QFrame(self.account)
        self.line_3.setGeometry(QtCore.QRect(390, 10, 16, 111))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_portfolioValue = QtGui.QLabel(self.account)
        self.label_portfolioValue.setGeometry(QtCore.QRect(420, 20, 121, 19))
        self.label_portfolioValue.setObjectName("label_portfolioValue")
        self.showPortfolioValue = QtGui.QLabel(self.account)
        self.showPortfolioValue.setGeometry(QtCore.QRect(550, 20, 121, 19))
        self.showPortfolioValue.setObjectName("showPortfolioValue")
        self.label_portfolio = QtGui.QLabel(self.account)
        self.label_portfolio.setGeometry(QtCore.QRect(420, 60, 81, 19))
        self.label_portfolio.setObjectName("label_portfolio")
        self.showPortfolio = QtGui.QLabel(self.account)
        self.showPortfolio.setGeometry(QtCore.QRect(550, 60, 161, 61))
        self.showPortfolio.setObjectName("showPortfolio")
        self.buyStop = QtGui.QLineEdit(self.account)
        self.buyStop.setGeometry(QtCore.QRect(260, 40, 113, 29))
        self.buyStop.setObjectName("buyStop")
        self.sellStop = QtGui.QLineEdit(self.account)
        self.sellStop.setGeometry(QtCore.QRect(260, 80, 113, 29))
        self.sellStop.setObjectName("sellStop")
        self.label_shares = QtGui.QLabel(self.account)
        self.label_shares.setGeometry(QtCore.QRect(170, 10, 71, 19))
        self.label_shares.setObjectName("label_shares")
        self.label_stopPrice = QtGui.QLabel(self.account)
        self.label_stopPrice.setGeometry(QtCore.QRect(280, 10, 81, 19))
        self.label_stopPrice.setObjectName("label_stopPrice")
        self.tabWidget.addTab(self.account, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.macd = QtGui.QPushButton(self.tab_4)
        self.macd.setGeometry(QtCore.QRect(150, 30, 110, 29))
        self.macd.setObjectName("macd")
        self.macdLength = QtGui.QLineEdit(self.tab_4)
        self.macdLength.setGeometry(QtCore.QRect(150, 70, 113, 29))
        self.macdLength.setObjectName("macdLength")
        self.sma = QtGui.QPushButton(self.tab_4)
        self.sma.setGeometry(QtCore.QRect(20, 30, 110, 29))
        self.sma.setObjectName("sma")
        self.smaLength = QtGui.QLineEdit(self.tab_4)
        self.smaLength.setGeometry(QtCore.QRect(20, 70, 113, 29))
        self.smaLength.setObjectName("smaLength")
        self.tabWidget.addTab(self.tab_4, "")
        self.nextDay = QtGui.QPushButton(chartWidget)
        self.nextDay.setGeometry(QtCore.QRect(850, 940, 110, 29))
        self.nextDay.setObjectName("nextDay")
        self.next30 = QtGui.QPushButton(chartWidget)
        self.next30.setGeometry(QtCore.QRect(960, 940, 110, 29))
        self.next30.setObjectName("next30")
        self.prev30 = QtGui.QPushButton(chartWidget)
        self.prev30.setGeometry(QtCore.QRect(960, 990, 110, 29))
        self.prev30.setObjectName("prev30")
        self.prevDay = QtGui.QPushButton(chartWidget)
        self.prevDay.setGeometry(QtCore.QRect(850, 990, 110, 29))
        self.prevDay.setObjectName("prevDay")
        self.chartTabs = QtGui.QTabWidget(chartWidget)
        self.chartTabs.setGeometry(QtCore.QRect(0, 0, 1071, 871))
        self.chartTabs.setObjectName("chartTabs")
        self.firstChart = QtGui.QWidget()
        self.firstChart.setObjectName("firstChart")
        self.horizontalLayoutWidget = QtGui.QWidget(self.firstChart)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-10, -10, 1081, 851))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chart = QtGui.QGraphicsView(self.horizontalLayoutWidget)
        self.chart.setObjectName("chart")
        self.horizontalLayout.addWidget(self.chart)
        self.chartTabs.addTab(self.firstChart, "")
        self.currentDayLabel = QtGui.QLabel(chartWidget)
        self.currentDayLabel.setGeometry(QtCore.QRect(910, 910, 101, 19))
        self.currentDayLabel.setObjectName("currentDayLabel")

        self.retranslateUi(chartWidget)
        self.tabWidget.setCurrentIndex(0)
        self.chartTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(chartWidget)

    def retranslateUi(self, chartWidget):
        chartWidget.setWindowTitle(QtGui.QApplication.translate("chartWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomIn.setText(QtGui.QApplication.translate("chartWidget", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOut.setText(QtGui.QApplication.translate("chartWidget", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.chartLength.setText(QtGui.QApplication.translate("chartWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.candlestick.setText(QtGui.QApplication.translate("chartWidget", "Candlestick", None, QtGui.QApplication.UnicodeUTF8))
        self.ohlc.setText(QtGui.QApplication.translate("chartWidget", "OHLC", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("chartWidget", "Chart Style", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSymbol.setText(QtGui.QApplication.translate("chartWidget", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.newTab.setText(QtGui.QApplication.translate("chartWidget", "New Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.hlc.setText(QtGui.QApplication.translate("chartWidget", "HLC", None, QtGui.QApplication.UnicodeUTF8))
        self.bar.setText(QtGui.QApplication.translate("chartWidget", "Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.dot.setText(QtGui.QApplication.translate("chartWidget", "Dot", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("chartWidget", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chartControls), QtGui.QApplication.translate("chartWidget", "Chart Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.buy.setText(QtGui.QApplication.translate("chartWidget", "Buy", None, QtGui.QApplication.UnicodeUTF8))
        self.sell.setText(QtGui.QApplication.translate("chartWidget", "Sell", None, QtGui.QApplication.UnicodeUTF8))
        self.showBalance.setText(QtGui.QApplication.translate("chartWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_balance.setText(QtGui.QApplication.translate("chartWidget", "Balance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_portfolioValue.setText(QtGui.QApplication.translate("chartWidget", "Portfolio Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.showPortfolioValue.setText(QtGui.QApplication.translate("chartWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_portfolio.setText(QtGui.QApplication.translate("chartWidget", "Portfolio:", None, QtGui.QApplication.UnicodeUTF8))
        self.showPortfolio.setText(QtGui.QApplication.translate("chartWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_shares.setText(QtGui.QApplication.translate("chartWidget", "Shares", None, QtGui.QApplication.UnicodeUTF8))
        self.label_stopPrice.setText(QtGui.QApplication.translate("chartWidget", "Stop Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account), QtGui.QApplication.translate("chartWidget", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.macd.setText(QtGui.QApplication.translate("chartWidget", "macd", None, QtGui.QApplication.UnicodeUTF8))
        self.sma.setText(QtGui.QApplication.translate("chartWidget", "sma", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("chartWidget", "Technical Indicators", None, QtGui.QApplication.UnicodeUTF8))
        self.nextDay.setText(QtGui.QApplication.translate("chartWidget", "Next Day", None, QtGui.QApplication.UnicodeUTF8))
        self.next30.setText(QtGui.QApplication.translate("chartWidget", "Next 30", None, QtGui.QApplication.UnicodeUTF8))
        self.prev30.setText(QtGui.QApplication.translate("chartWidget", "Prev 30", None, QtGui.QApplication.UnicodeUTF8))
        self.prevDay.setText(QtGui.QApplication.translate("chartWidget", "Prev Day", None, QtGui.QApplication.UnicodeUTF8))
        self.chartTabs.setTabText(self.chartTabs.indexOf(self.firstChart), QtGui.QApplication.translate("chartWidget", "MSFT", None, QtGui.QApplication.UnicodeUTF8))
        self.currentDayLabel.setText(QtGui.QApplication.translate("chartWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    chartWidget = QtGui.QWidget()
    ui = Ui_chartWidget()
    ui.setupUi(chartWidget)
    chartWidget.show()
    sys.exit(app.exec_())

