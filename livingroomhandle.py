from livingroom import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
import time
from PyQt5 import QtCore
from dieuhoahandle import DIEUHOA_HANDLE
from firebase import firebase
import time
firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pk = 'PHONG_KHACH'
pkDen = 'DEN'
pkTivi = 'TIVI'
pkWifi = 'WIFI'
pkTulanh = 'TULANH'
pkDen1 = firebase.get(pk, pkDen)
pkTivi1 = firebase.get(pk, pkTivi)
pkWifi1 = firebase.get(pk, pkWifi)
pkTulanh1 = firebase.get(pk, pkTulanh)
class LINGVING_HANDLE(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)
        
        self.checkBox_2.stateChanged.connect(self.debug2)
        self.checkBox_4.stateChanged.connect(self.debug3)
        self.checkBox_3.stateChanged.connect(self.debug4)
        self.checkBox_5.stateChanged.connect(self.debug5)
        if pkDen1 == 0:
            if self.checkBox_2.isChecked()== True:
                pass
            else:
                self.checkBox_2.click()
        if pkTivi1 == 0:
            if self.checkBox_4.isChecked()== True:
                pass
            else:
                self.checkBox_4.click()
        if pkWifi1 == 0:
            if self.checkBox_3.isChecked()== True:
                pass     
        else:
            self.checkBox_3.click()
        if pkTulanh1 == 0:
            if self.checkBox_5.isChecked()== True:
                pass      
            else:
                self.checkBox_5.click()
            

    def debug2(self):
        if self.checkBox_2.isChecked() == True:
            print("den phong khach tat")
            pkDen2 = firebase.put(pk,pkDen , 0)
        else:
            print("den phong khach bat")
            pkDen2 = firebase.put(pk,pkDen , 1)
    def debug3(self):
        if self.checkBox_4.isChecked() == True:
            print("Tivi phong khach tat")
            pkTivi2 = firebase.put(pk,pkTivi, 0)
        else:
            print("tivi phong khach bat")
            pkTivi2 = firebase.put(pk,pkTivi, 1)
    def debug4(self):
        if self.checkBox_3.isChecked() == True:
            print("wifi phong khach chua ket noi")
            pkWific2 = firebase.put(pk,pkWifi, 0)
        else:
            print("wifi phong khach da ket noi")
            pkWifi2 = firebase.put(pk,pkWifi, 1)
    def debug5(self):
        if self.checkBox_5.isChecked() == True:
            print("tu lanh phong khach tat")
            pkTulanh2 = firebase.put(pk,pkTulanh, 0)
        else:
            print("tu lanh phong khach bat")
            pkTulanh2 = firebase.put(pk,pkTulanh, 1)
    

        