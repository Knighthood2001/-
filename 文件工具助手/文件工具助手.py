# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '文件工具助手.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/knighthood/OneDrive/桌面/熊二表情包/熊二表情包41.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget1.setEnabled(True)
        self.tabWidget1.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.tabWidget1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget1.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget1.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget1.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget1.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget1.setUsesScrollButtons(True)
        self.tabWidget1.setTabsClosable(False)
        self.tabWidget1.setTabBarAutoHide(True)
        self.tabWidget1.setObjectName("tabWidget1")
        self.word = QtWidgets.QWidget()
        self.word.setObjectName("word")
        self.tabWidget2_1 = QtWidgets.QTabWidget(self.word)
        self.tabWidget2_1.setGeometry(QtCore.QRect(0, 0, 871, 561))
        self.tabWidget2_1.setObjectName("tabWidget2_1")
        self.word2pdf = QtWidgets.QWidget()
        self.word2pdf.setObjectName("word2pdf")
        self.label1_1_1 = QtWidgets.QLabel(self.word2pdf)
        self.label1_1_1.setGeometry(QtCore.QRect(40, 30, 72, 31))
        self.label1_1_1.setObjectName("label1_1_1")
        self.btn1_1_1 = QtWidgets.QPushButton(self.word2pdf)
        self.btn1_1_1.setGeometry(QtCore.QRect(130, 30, 121, 41))
        self.btn1_1_1.setObjectName("btn1_1_1")
        self.textBrowser1_1_1 = QtWidgets.QTextBrowser(self.word2pdf)
        self.textBrowser1_1_1.setGeometry(QtCore.QRect(20, 80, 256, 61))
        self.textBrowser1_1_1.setObjectName("textBrowser1_1_1")
        self.label1_1_3 = QtWidgets.QLabel(self.word2pdf)
        self.label1_1_3.setGeometry(QtCore.QRect(600, 30, 181, 31))
        self.label1_1_3.setObjectName("label1_1_3")
        self.btn1_1_3 = QtWidgets.QPushButton(self.word2pdf)
        self.btn1_1_3.setGeometry(QtCore.QRect(120, 350, 93, 28))
        self.btn1_1_3.setObjectName("btn1_1_3")
        self.label1_1_2 = QtWidgets.QLabel(self.word2pdf)
        self.label1_1_2.setGeometry(QtCore.QRect(40, 160, 72, 31))
        self.label1_1_2.setObjectName("label1_1_2")
        self.textBrowser1_1_2 = QtWidgets.QTextBrowser(self.word2pdf)
        self.textBrowser1_1_2.setGeometry(QtCore.QRect(30, 220, 256, 61))
        self.textBrowser1_1_2.setObjectName("textBrowser1_1_2")
        self.btn1_1_2 = QtWidgets.QPushButton(self.word2pdf)
        self.btn1_1_2.setGeometry(QtCore.QRect(130, 160, 121, 41))
        self.btn1_1_2.setObjectName("btn1_1_2")
        self.textBrowser1_1_3 = QtWidgets.QTextBrowser(self.word2pdf)
        self.textBrowser1_1_3.setGeometry(QtCore.QRect(520, 80, 321, 331))
        self.textBrowser1_1_3.setObjectName("textBrowser1_1_3")
        self.tabWidget2_1.addTab(self.word2pdf, "")
        self.none = QtWidgets.QWidget()
        self.none.setObjectName("none")
        self.tabWidget2_1.addTab(self.none, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pyqt5页面/images/PDF2Word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget1.addTab(self.word, icon1, "")
        self.pdf = QtWidgets.QWidget()
        self.pdf.setObjectName("pdf")
        self.tabWidget2_2 = QtWidgets.QTabWidget(self.pdf)
        self.tabWidget2_2.setGeometry(QtCore.QRect(0, 0, 901, 541))
        self.tabWidget2_2.setObjectName("tabWidget2_2")
        self.pdf2word = QtWidgets.QWidget()
        self.pdf2word.setObjectName("pdf2word")
        self.btn2_1_1 = QtWidgets.QPushButton(self.pdf2word)
        self.btn2_1_1.setGeometry(QtCore.QRect(110, 0, 121, 41))
        self.btn2_1_1.setObjectName("btn2_1_1")
        self.btn2_1_2 = QtWidgets.QPushButton(self.pdf2word)
        self.btn2_1_2.setGeometry(QtCore.QRect(110, 120, 121, 41))
        self.btn2_1_2.setObjectName("btn2_1_2")
        self.label2_1_2 = QtWidgets.QLabel(self.pdf2word)
        self.label2_1_2.setGeometry(QtCore.QRect(30, 120, 72, 31))
        self.label2_1_2.setObjectName("label2_1_2")
        self.btn2_1_3 = QtWidgets.QPushButton(self.pdf2word)
        self.btn2_1_3.setGeometry(QtCore.QRect(100, 340, 93, 28))
        self.btn2_1_3.setObjectName("btn2_1_3")
        self.textBrowser2_1_2 = QtWidgets.QTextBrowser(self.pdf2word)
        self.textBrowser2_1_2.setGeometry(QtCore.QRect(20, 180, 331, 51))
        self.textBrowser2_1_2.setObjectName("textBrowser2_1_2")
        self.label2_1_1 = QtWidgets.QLabel(self.pdf2word)
        self.label2_1_1.setGeometry(QtCore.QRect(30, 0, 72, 31))
        self.label2_1_1.setObjectName("label2_1_1")
        self.textBrowser2_1_1 = QtWidgets.QTextBrowser(self.pdf2word)
        self.textBrowser2_1_1.setGeometry(QtCore.QRect(20, 50, 331, 51))
        self.textBrowser2_1_1.setObjectName("textBrowser2_1_1")
        self.label2_1_3 = QtWidgets.QLabel(self.pdf2word)
        self.label2_1_3.setGeometry(QtCore.QRect(410, 20, 181, 31))
        self.label2_1_3.setObjectName("label2_1_3")
        self.textBrowser2_1_3 = QtWidgets.QTextBrowser(self.pdf2word)
        self.textBrowser2_1_3.setGeometry(QtCore.QRect(400, 50, 256, 311))
        self.textBrowser2_1_3.setObjectName("textBrowser2_1_3")
        self.tabWidget2_2.addTab(self.pdf2word, "")
        self.pdf2img = QtWidgets.QWidget()
        self.pdf2img.setObjectName("pdf2img")
        self.btn2_2_1 = QtWidgets.QPushButton(self.pdf2img)
        self.btn2_2_1.setGeometry(QtCore.QRect(100, 10, 121, 41))
        self.btn2_2_1.setObjectName("btn2_2_1")
        self.btn2_2_2 = QtWidgets.QPushButton(self.pdf2img)
        self.btn2_2_2.setGeometry(QtCore.QRect(100, 130, 121, 41))
        self.btn2_2_2.setObjectName("btn2_2_2")
        self.label2_2_2 = QtWidgets.QLabel(self.pdf2img)
        self.label2_2_2.setGeometry(QtCore.QRect(20, 130, 72, 31))
        self.label2_2_2.setObjectName("label2_2_2")
        self.btn2_2_3 = QtWidgets.QPushButton(self.pdf2img)
        self.btn2_2_3.setGeometry(QtCore.QRect(100, 310, 93, 28))
        self.btn2_2_3.setObjectName("btn2_2_3")
        self.textBrowser2_2_2 = QtWidgets.QTextBrowser(self.pdf2img)
        self.textBrowser2_2_2.setGeometry(QtCore.QRect(10, 190, 331, 51))
        self.textBrowser2_2_2.setObjectName("textBrowser2_2_2")
        self.label2_2_1 = QtWidgets.QLabel(self.pdf2img)
        self.label2_2_1.setGeometry(QtCore.QRect(20, 10, 72, 31))
        self.label2_2_1.setObjectName("label2_2_1")
        self.textBrowser2_2_1 = QtWidgets.QTextBrowser(self.pdf2img)
        self.textBrowser2_2_1.setGeometry(QtCore.QRect(10, 60, 331, 51))
        self.textBrowser2_2_1.setObjectName("textBrowser2_2_1")
        self.label2_2_3 = QtWidgets.QLabel(self.pdf2img)
        self.label2_2_3.setGeometry(QtCore.QRect(400, 30, 181, 31))
        self.label2_2_3.setObjectName("label2_2_3")
        self.textBrowser2_2_3 = QtWidgets.QTextBrowser(self.pdf2img)
        self.textBrowser2_2_3.setGeometry(QtCore.QRect(390, 60, 256, 311))
        self.textBrowser2_2_3.setObjectName("textBrowser2_2_3")
        self.tabWidget2_2.addTab(self.pdf2img, "")
        self.pdf2text = QtWidgets.QWidget()
        self.pdf2text.setObjectName("pdf2text")
        self.btn2_3_1 = QtWidgets.QPushButton(self.pdf2text)
        self.btn2_3_1.setGeometry(QtCore.QRect(110, 10, 121, 41))
        self.btn2_3_1.setObjectName("btn2_3_1")
        self.btn2_3_2 = QtWidgets.QPushButton(self.pdf2text)
        self.btn2_3_2.setGeometry(QtCore.QRect(110, 130, 121, 41))
        self.btn2_3_2.setObjectName("btn2_3_2")
        self.label2_3_2 = QtWidgets.QLabel(self.pdf2text)
        self.label2_3_2.setGeometry(QtCore.QRect(30, 130, 72, 31))
        self.label2_3_2.setObjectName("label2_3_2")
        self.btn2_3_3 = QtWidgets.QPushButton(self.pdf2text)
        self.btn2_3_3.setGeometry(QtCore.QRect(240, 310, 121, 71))
        self.btn2_3_3.setObjectName("btn2_3_3")
        self.textBrowser2_3_2 = QtWidgets.QTextBrowser(self.pdf2text)
        self.textBrowser2_3_2.setGeometry(QtCore.QRect(20, 190, 331, 51))
        self.textBrowser2_3_2.setObjectName("textBrowser2_3_2")
        self.label2_3_1 = QtWidgets.QLabel(self.pdf2text)
        self.label2_3_1.setGeometry(QtCore.QRect(30, 10, 72, 31))
        self.label2_3_1.setObjectName("label2_3_1")
        self.textBrowser2_3_1 = QtWidgets.QTextBrowser(self.pdf2text)
        self.textBrowser2_3_1.setGeometry(QtCore.QRect(10, 60, 351, 51))
        self.textBrowser2_3_1.setObjectName("textBrowser2_3_1")
        self.label2_3_3 = QtWidgets.QLabel(self.pdf2text)
        self.label2_3_3.setGeometry(QtCore.QRect(440, 10, 91, 31))
        self.label2_3_3.setObjectName("label2_3_3")
        self.lineEdit2_3_1 = QtWidgets.QLineEdit(self.pdf2text)
        self.lineEdit2_3_1.setGeometry(QtCore.QRect(140, 270, 41, 41))
        self.lineEdit2_3_1.setObjectName("lineEdit2_3_1")
        self.label2_3_4 = QtWidgets.QLabel(self.pdf2text)
        self.label2_3_4.setGeometry(QtCore.QRect(20, 270, 81, 31))
        self.label2_3_4.setObjectName("label2_3_4")
        self.textBrowser2_3_4 = QtWidgets.QTextBrowser(self.pdf2text)
        self.textBrowser2_3_4.setGeometry(QtCore.QRect(800, 10, 41, 41))
        self.textBrowser2_3_4.setObjectName("textBrowser2_3_4")
        self.label2_3_5 = QtWidgets.QLabel(self.pdf2text)
        self.label2_3_5.setGeometry(QtCore.QRect(640, 10, 71, 31))
        self.label2_3_5.setObjectName("label2_3_5")
        self.plainTextEdit2_3_1 = QtWidgets.QPlainTextEdit(self.pdf2text)
        self.plainTextEdit2_3_1.setGeometry(QtCore.QRect(450, 70, 421, 421))
        self.plainTextEdit2_3_1.setObjectName("plainTextEdit2_3_1")
        self.lineEdit2_3_2 = QtWidgets.QLineEdit(self.pdf2text)
        self.lineEdit2_3_2.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.lineEdit2_3_2.setPlaceholderText("")
        self.lineEdit2_3_2.setObjectName("lineEdit2_3_2")
        self.tabWidget2_2.addTab(self.pdf2text, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../pyqt5页面/images/PDF2Img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget1.addTab(self.pdf, icon2, "")
        self.PDF2Text_2 = QtWidgets.QWidget()
        self.PDF2Text_2.setObjectName("PDF2Text_2")
        self.textBrowser3_1 = QtWidgets.QTextBrowser(self.PDF2Text_2)
        self.textBrowser3_1.setGeometry(QtCore.QRect(40, 80, 331, 51))
        self.textBrowser3_1.setObjectName("textBrowser3_1")
        self.label2_4 = QtWidgets.QLabel(self.PDF2Text_2)
        self.label2_4.setGeometry(QtCore.QRect(50, 30, 72, 31))
        self.label2_4.setObjectName("label2_4")
        self.btn3_1 = QtWidgets.QPushButton(self.PDF2Text_2)
        self.btn3_1.setGeometry(QtCore.QRect(130, 30, 121, 41))
        self.btn3_1.setObjectName("btn3_1")
        self.label1_4 = QtWidgets.QLabel(self.PDF2Text_2)
        self.label1_4.setGeometry(QtCore.QRect(390, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        self.label1_4.setFont(font)
        self.label1_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label1_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1_4.setObjectName("label1_4")
        self.label = QtWidgets.QLabel(self.PDF2Text_2)
        self.label.setGeometry(QtCore.QRect(440, 30, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit3_1 = QtWidgets.QLineEdit(self.PDF2Text_2)
        self.lineEdit3_1.setGeometry(QtCore.QRect(540, 20, 41, 41))
        self.lineEdit3_1.setObjectName("lineEdit3_1")
        self.btn3_2 = QtWidgets.QPushButton(self.PDF2Text_2)
        self.btn3_2.setGeometry(QtCore.QRect(470, 110, 111, 41))
        self.btn3_2.setObjectName("btn3_2")
        self.plainTextEdit3_1 = QtWidgets.QPlainTextEdit(self.PDF2Text_2)
        self.plainTextEdit3_1.setGeometry(QtCore.QRect(20, 210, 561, 271))
        self.plainTextEdit3_1.setPlainText("")
        self.plainTextEdit3_1.setObjectName("plainTextEdit3_1")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../pyqt5页面/images/PDF2Text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget1.addTab(self.PDF2Text_2, icon3, "")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("images/pdf.jpg"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label_background.raise_()
        self.tabWidget1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.PDF2Word = QtWidgets.QAction(MainWindow)
        self.PDF2Word.setIcon(icon1)
        self.PDF2Word.setObjectName("PDF2Word")
        self.PDF2Img = QtWidgets.QAction(MainWindow)
        self.PDF2Img.setIcon(icon2)
        self.PDF2Img.setObjectName("PDF2Img")
        self.PDF2Text = QtWidgets.QAction(MainWindow)
        self.PDF2Text.setIcon(icon3)
        self.PDF2Text.setObjectName("PDF2Text")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_2.addAction(self.actionVersion)
        self.menu_2.addAction(self.actionExit)
        self.menu_3.addAction(self.PDF2Word)
        self.menu_3.addAction(self.PDF2Img)
        self.menu_3.addAction(self.PDF2Text)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget1.setCurrentIndex(1)
        self.tabWidget2_1.setCurrentIndex(0)
        self.tabWidget2_2.setCurrentIndex(2)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF工具"))
        self.label1_1_1.setText(_translate("MainWindow", "word路径"))
        self.btn1_1_1.setText(_translate("MainWindow", "选择文件（夹）"))
        self.label1_1_3.setText(_translate("MainWindow", "相关信息展示"))
        self.btn1_1_3.setText(_translate("MainWindow", "开始转换"))
        self.label1_1_2.setText(_translate("MainWindow", "保存路径"))
        self.btn1_1_2.setText(_translate("MainWindow", "选择文件夹"))
        self.tabWidget2_1.setTabText(self.tabWidget2_1.indexOf(self.word2pdf), _translate("MainWindow", "word转pdf"))
        self.tabWidget2_1.setTabText(self.tabWidget2_1.indexOf(self.none), _translate("MainWindow", "待开发"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.word), _translate("MainWindow", "word"))
        self.btn2_1_1.setText(_translate("MainWindow", "选择文件（夹）"))
        self.btn2_1_2.setText(_translate("MainWindow", "选择文件（夹）"))
        self.label2_1_2.setText(_translate("MainWindow", "保存路径"))
        self.btn2_1_3.setText(_translate("MainWindow", "开始转换"))
        self.label2_1_1.setText(_translate("MainWindow", "PDF路径"))
        self.label2_1_3.setText(_translate("MainWindow", "相关信息展示"))
        self.tabWidget2_2.setTabText(self.tabWidget2_2.indexOf(self.pdf2word), _translate("MainWindow", "pdf转word"))
        self.btn2_2_1.setText(_translate("MainWindow", "选择文件（夹）"))
        self.btn2_2_2.setText(_translate("MainWindow", "选择文件（夹）"))
        self.label2_2_2.setText(_translate("MainWindow", "保存路径"))
        self.btn2_2_3.setText(_translate("MainWindow", "开始转换"))
        self.label2_2_1.setText(_translate("MainWindow", "PDF路径"))
        self.label2_2_3.setText(_translate("MainWindow", "相关信息展示"))
        self.tabWidget2_2.setTabText(self.tabWidget2_2.indexOf(self.pdf2img), _translate("MainWindow", "pdf转img"))
        self.btn2_3_1.setText(_translate("MainWindow", "选择文件（夹）"))
        self.btn2_3_2.setText(_translate("MainWindow", "选择文件（夹）"))
        self.label2_3_2.setText(_translate("MainWindow", "保存路径"))
        self.btn2_3_3.setText(_translate("MainWindow", "开始转换"))
        self.label2_3_1.setText(_translate("MainWindow", "PDF路径"))
        self.label2_3_3.setText(_translate("MainWindow", "相关信息展示"))
        self.label2_3_4.setText(_translate("MainWindow", "选择页码"))
        self.label2_3_5.setText(_translate("MainWindow", "总页数："))
        self.tabWidget2_2.setTabText(self.tabWidget2_2.indexOf(self.pdf2text), _translate("MainWindow", "pdf提取文字"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.pdf), _translate("MainWindow", "pdf"))
        self.label2_4.setText(_translate("MainWindow", "PDF路径"))
        self.btn3_1.setText(_translate("MainWindow", "选择文件"))
        self.label1_4.setText(_translate("MainWindow", "相关信息展示"))
        self.label.setText(_translate("MainWindow", "选择页码"))
        self.btn3_2.setText(_translate("MainWindow", "开始提取"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.PDF2Text_2), _translate("MainWindow", "PDF提取文字"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.menu_3.setTitle(_translate("MainWindow", "功能"))
        self.PDF2Word.setText(_translate("MainWindow", "PDF转word"))
        self.PDF2Img.setText(_translate("MainWindow", "PDF转图片"))
        self.PDF2Text.setText(_translate("MainWindow", "PDF提取文字"))
        self.actionVersion.setText(_translate("MainWindow", "版本号"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
