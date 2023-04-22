import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PyQt5 import QtCore


from dinner import Ui_MainWindow
from firebase import firebase

firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pa = 'PHONG_AN'
paDen = 'DEN'
paMusic = 'MUSIC'
paTivi = 'TIVI'
paFilm = 'FILM'
paDieuhoa = 'DIEU_HOA'
paDen1 = firebase.get(pa, paDen)
paMusic1 = firebase.get(pa, paMusic)
paTivi1 = firebase.get(pa, paTivi)
paFilm1 = firebase.get(pa, paFilm)
paDieuhoa1 = firebase.get(pa, paDieuhoa)

class DINNER_HANDLE(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)
        self.checkBox.stateChanged.connect(self.debug1)
        self.checkBox_2.stateChanged.connect(self.debug2)
        self.checkBox_3.stateChanged.connect(self.debug3)
        self.checkBox_4.stateChanged.connect(self.debug4)
        self.checkBox_5.stateChanged.connect(self.debug5)
        if paDen1 == 0:
            if self.checkBox.isChecked()== True:
                pass
            else:
                self.checkBox.click()

        if paMusic1 == 0:
            if self.checkBox_2.isChecked()== True:
                pass
            else:
                self.checkBox_2.click()
        if paTivi1 == 0:
            if self.checkBox_3.isChecked()== True:
                pass
            else:
                self.checkBox_3.click()
        if paFilm1 == 0:
            if self.checkBox_4.isChecked()== True:
                pass
            else:
                self.checkBox_4.click()    
        if paDieuhoa1 == 0:
            if self.checkBox_5.isChecked()== True:
                pass
            else:
                self.checkBox_5.click() 


    def debug1(self):
        if self.checkBox.isChecked() == True:
            print("den phong an tat")
            paDen2 = firebase.put(pa,paDen, 0)
        else:
            print("den phong an bat")
            paDen2 = firebase.put(pa,paDen, 1)
    def debug2(self):
        if self.checkBox_2.isChecked() == True:
            print("music phong an tat")
            paMusic2 = firebase.put(pa,paMusic, 0)
        else:
            print("music phong an bat")
            paMusic2 = firebase.put(pa,paMusic, 1)
    def debug3(self):
        if self.checkBox_3.isChecked() == True:
            print("tivi phong an tat")
            paTivi3 = firebase.put(pa,paTivi, 0)
        else:
            print("tivi phong an bat")
            paTivi3 = firebase.put(pa,paTivi, 1)
    def debug4(self):
        if self.checkBox_4.isChecked() == True:
            print("Film phong an tat")
            paFilm4 = firebase.put(pa,paFilm, 0)
        else:
            print("Film bep an")
            paFilm4 = firebase.put(pa,paFilm, 1)
    def debug5(self):
        if self.checkBox_5.isChecked() == True:
            print("dieu hoa phong an tat")
            paDieuhoa5 = firebase.put(pa,paDieuhoa, 0)
        else:
            print("dieu hoa phong an bat")
            paDieuhoa5 = firebase.put(pa,paDieuhoa, 1)