# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proje.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ana Sayfa")
        MainWindow.resize(800, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(150, 150, 121, 111))
        self.bt1.setObjectName("bt1")
        self.bt1.clicked.connect(self.Ver)
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(150, 280, 121, 111))
        self.bt2.setObjectName("bt2")
        self.bt2.clicked.connect(self.Verilenler)
        self.bt3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3.setGeometry(QtCore.QRect(500, 150, 121, 111))
        self.bt3.setObjectName("bt3")
        self.bt3.clicked.connect(self.KitapEkle)
        self.bt4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4.setGeometry(QtCore.QRect(500, 280, 121, 111))
        self.bt4.setObjectName("bt4")
        self.bt4.clicked.connect(self.ktphnliste)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Sayfa"))
        self.label.setText(_translate("MainWindow", "??T?? MTAL K??T??PHANE OTOMASYONU"))
        self.bt1.setText(_translate("MainWindow", "K??TAP VER"))
        self.bt2.setText(_translate("MainWindow", "VER??LEN K??TAPLAR"))
        self.bt3.setText(_translate("MainWindow", "K??TAP EKLE"))
        self.bt4.setText(_translate("MainWindow", "K??TAP L??STE"))
    def Ver(self):
        p = subprocess.Popen(['python', 'kitap1.py'])
    def Verilenler(self):
        p = subprocess.Popen(['python', 'kitaplar.py'])
    def KitapEkle(self):
        p = subprocess.Popen(['python', 'kitapekle.py'])
    def ktphnliste(self):
        p = subprocess.Popen(['python', 'kitapliste.py'])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
