#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow,QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 381, 100))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 381, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 0, 411, 551))
        self.label.setObjectName(_fromUtf8("showView"))



        '''
        image = QtGui.QImage()
        image.load('image1.png')
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        '''
        '''
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(380, 0, 411, 551))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pushButton=QToolButton()
        pushButton_2=QToolButton()
        MainWindow.setWindowTitle(_translate("MainWindow", "微型测试平台", None))
        self.pushButton.setText(_translate("MainWindow", "网络拓扑1", None))
        self.pushButton.setIcon(QIcon("image1.png"))
        self.pushButton.setIconSize(QSize(400, 100))
        self.pushButton_2.setText(_translate("MainWindow", "网络拓扑2", None))
        self.pushButton_2.setIcon(QIcon("image1.png"))
        self.pushButton_2.setIconSize(QSize(400, 100))
        
        #按钮响应
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.showimage1)
        self.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.showimage2)

        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))





    def showimage1(self):                 #添加图片

        image = QtGui.QImage()
        image.load('image3.png')
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))



    def showimage2(self):                #添加图片

        image = QtGui.QImage()
        image.load('image2.png')
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))


app = QtGui.QApplication(sys.argv)
main = Ui_MainWindow()
main.show()
app.exec_()
