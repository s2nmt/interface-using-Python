import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt5 import QtCore


from kitchen import Ui_MainWindow
from firebase import firebase

firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pb = 'PHONG_BEP'
pbVacuum = 'VACUUM'
pbLovisong = 'LO_VI_SONG'
pbDen = 'DEN'
pbHood = 'HOOD'
pbTulanh = 'TULANH'

pbVacuum1 = firebase.get(pb, pbVacuum)
pbLovisong1 = firebase.get(pb, pbLovisong)
pbDen1 = firebase.get(pb, pbDen)
pbHood1 = firebase.get(pb, pbHood)
pbTulanh1 = firebase.get(pb, pbTulanh)

class KITCHEN_HANDLE(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

        self.checkBox.stateChanged.connect(self.debug11)
        self.checkBox_2.stateChanged.connect(self.debug12)
        self.checkBox_3.stateChanged.connect(self.debug13)
        self.checkBox_4.stateChanged.connect(self.debug14)
        self.checkBox_5.stateChanged.connect(self.debug15)
        if pbVacuum1 == 0:
            if self.checkBox.isChecked()== True:
                pass
            else:
                self.checkBox.click()
        if pbLovisong1 == 0:
            if self.checkBox_2.isChecked()== True:
                pass
            else:
                self.checkBox_2.click()
        if pbDen1 == 0:
            if self.checkBox_3.isChecked()== True:
                pass
            else:
                self.checkBox_3.click()
        if pbHood1 == 0:
            if self.checkBox_4.isChecked()== True:
                pass
            else:
                self.checkBox_4.click()
        if pbTulanh1 == 0:
            if self.checkBox_5.isChecked()== True:
                pass
            else:
                self.checkBox_5.click()
    def debug11(self):
        if self.checkBox.isChecked() == True:
            print("Vacuum phong bep tat")
            pbVacuum2 = firebase.put(pb,pbVacuum, 0)
        else:
            print("Vacuum phong bep bat")
            pbVacuum2 = firebase.put(pb,pbVacuum, 1)
    def debug12(self):
        if self.checkBox_2.isChecked() == True:
            print("Lo vi song phong bep tat")
            pbLovisong2 = firebase.put(pb,pbLovisong, 0)
            
        else:
            print("lo vi song bep bat")
            pbLovisong2 = firebase.put(pb,pbLovisong, 1)
    def debug13(self):
        if self.checkBox_3.isChecked() == True:
            print("den phong bep tat")
            pbDen2 = firebase.put(pb,pbDen, 0)
        else:
            print("den phong bep bat")
            pbDen2 = firebase.put(pb,pbDen, 1)
    def debug14(self):
        if self.checkBox_4.isChecked() == True:
            print("hood phong bep tat")
            pbHood2 = firebase.put(pb,pbHood, 0)
        else:
            print("hood bep bat")
            pbHood2 = firebase.put(pb,pbHood, 1)
    def debug15(self):
        if self.checkBox_5.isChecked() == True:
            print("tu lanh phong bep tat")
            pbTulanh2 = firebase.put(pb,pbTulanh, 0)
        else:
            print("tu lanh phong bep bat")
            pbTulanh2 = firebase.put(pb,pbTulanh, 1)
    
