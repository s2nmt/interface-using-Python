from PyQt5.QtWidgets import QApplication, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
import time
from threading import Timer
from PyQt5 import QtCore

from dinnerroom import Ui_MainWindow
from firebase import firebase
firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pn = 'PHONG_NGU'
pnAmnhac = 'AMNHAC'
pnDen = 'DEN'
pnRouter = 'ROUTER'
pnPrint = 'PRINT'

pnAmnhac1 = firebase.get(pn, pnAmnhac)
pnDen1 = firebase.get(pn, pnDen)
pnRouter1 = firebase.get(pn, pnRouter)
pnPrint1 = firebase.get(pn, pnPrint)

class DINNERROOM_HANDLE(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

        self.checkBox.stateChanged.connect(self.debug1)
        self.checkBox_3.stateChanged.connect(self.debug2)
        self.checkBox_2.stateChanged.connect(self.debug3)
        self.checkBox_5.stateChanged.connect(self.debug5)

        if pnAmnhac1 == 0:
            if self.checkBox.isChecked()== True:
                pass
            else:
                self.checkBox.click()
        if pnRouter1 == 0:
            if self.checkBox_2.isChecked()== True:
                pass
            else:
                self.checkBox_2.click()
        if pnDen1 == 0:
            if self.checkBox_3.isChecked()== True:
                pass
            else:
                self.checkBox_3.click()
        if pnPrint1 == 0:
            if self.checkBox_5.isChecked()== True:
                pass
            else:
                self.checkBox_5.click()
    def debug1(self):
        if self.checkBox.isChecked() == True:
            print("music phong ngu tat")
            pnAmnhac2 = firebase.put(pn,pnAmnhac, 0)
        else:
            print("music phong ngu bat")
            pnAmnhac2 = firebase.put(pn,pnAmnhac, 1)
    def debug2(self):
        if self.checkBox_3.isChecked() == True:
            print("den phong ngu tat")
            pnDen2 = firebase.put(pn,pnDen, 0)
        else:
            print("den ngu bat")
            pnDen2 = firebase.put(pn,pnDen, 1)
    def debug3(self):
        if self.checkBox_2.isChecked() == True:
            print("router phong ngu tat")
            pnRouter2 = firebase.put(pn,pnRouter, 0)
        else:
            print("router phong ngu bat")
            pnRouter2 = firebase.put(pn,pnRouter, 1)
    def debug5(self):
        if self.checkBox_5.isChecked() == True:
            print("may in phong ngu tat")
            pnPrint2 = firebase.put(pn,pnPrint, 0)
        else:
            print("may in ngu bat")
            pnPrint2 = firebase.put(pn,pnPrint, 1)
    


