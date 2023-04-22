
import imp
from pickle import TRUE
from PyQt5.QtWidgets import QApplication, QMainWindow
from loadinghandle import LOADING_HANDLE
from loginhandle import LOGIN_HANDLE
from dieuhoahandle import DIEUHOA_HANDLE
from selenium import webdriver
from dinnerroomhandle import DINNERROOM_HANDLE
from livingroomhandle import LINGVING_HANDLE
from kitchenhandle import KITCHEN_HANDLE
from dinnerhandle import DINNER_HANDLE
from musichandle import MUSIC_HANDLE
from testcam import CAM_HANDLE
from testmeunu import MENU_HANDLE

import sys
import platform
from PySide2 import QtCore
from loading import Ui_MainWindow
from PyQt5 import QtWidgets
from firebase import firebase

import time

firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pk = 'PHONG_KHACH'
pkDieuhoa = 'DIEUHOA'
pkNhietdo = 'NHIETDO'
pkDieuhoa1 = firebase.get(pk, pkDieuhoa)
pkNhietdo1 = firebase.get(pk, pkNhietdo)

counter = 0


class UI():
    def __init__(self):
        self.dinnerUI = QMainWindow()       
        self.dinnerroomhandle = DINNERROOM_HANDLE(self.dinnerUI)
        self.dinnerroomhandle.pushButton_3.clicked.connect(lambda: self.loadliving())
        self.dinnerroomhandle.pushButton_4.clicked.connect(lambda: self.loadktdn())
        self.dinnerroomhandle.pushButton_5.clicked.connect(lambda: self.loaddidn())
        self.dinnerroomhandle.pushButton_6.clicked.connect(lambda: self.loadlogindn())
        self.dinnerroomhandle.pushButton_7.clicked.connect(lambda: self.loadmusicdn())
        self.dinnerroomhandle.pushButton_8.clicked.connect(lambda: self.loadgame())


        self.dieuhoaUI = QMainWindow()
        self.dieuhoahandle = DIEUHOA_HANDLE(self.dieuhoaUI)
        self.dieuhoahandle.pushButton_3.clicked.connect(lambda: self.loadlvdh())
                

        self.livingUI = QMainWindow()
        self.livingroomhandle = LINGVING_HANDLE(self.livingUI)
        self.livingroomhandle.pushButton_2.clicked.connect(lambda: self.loaddinnerroom())
        self.livingroomhandle.pushButton_3.clicked.connect(lambda: self.loadktlv())
        self.livingroomhandle.pushButton_4.clicked.connect(lambda: self.loaddilv())
        self.livingroomhandle.pushButton_5.clicked.connect(lambda: self.loadloginlv())
        self.livingroomhandle.pushButton_6.clicked.connect(lambda: self.loaddhlv())
        self.livingroomhandle.checkBox.stateChanged.connect(lambda: self.dhlv())
        self.livingroomhandle.pushButton_7.clicked.connect(lambda: self.mocam())

        self.kitchenUI = QMainWindow()
        self.kitchenhandle = KITCHEN_HANDLE(self.kitchenUI)
        self.kitchenhandle.pushButton.clicked.connect(lambda: self.loadlvkt())
        self.kitchenhandle.pushButton_2.clicked.connect(lambda: self.loaddinnerkt())
        self.kitchenhandle.pushButton_4.clicked.connect(lambda: self.loaddikt())
        self.kitchenhandle.pushButton_5.clicked.connect(lambda: self.loadloginkt())

        self.dinUI = QMainWindow()
        self.dinnerhandle = DINNER_HANDLE(self.dinUI)
        self.dinnerhandle.pushButton.clicked.connect(lambda: self.loadlvdi())
        self.dinnerhandle.pushButton_2.clicked.connect(lambda: self.loaddndi())
        self.dinnerhandle.pushButton_3.clicked.connect(lambda: self.loadktdi())
        self.dinnerhandle.pushButton_5.clicked.connect(lambda: self.loadlogindi())
        self.dinnerhandle.pushButton_6.clicked.connect(lambda: self.loadmenu())
                

        self.loginUI = QMainWindow()
        self.loginhandle = LOGIN_HANDLE(self.loginUI)   
        self.loginhandle.pushButton_2.clicked.connect(self.login)
        self.loginhandle.pushButton_4.clicked.connect(self.loginfb)
        self.loginhandle.pushButton_5.clicked.connect(self.loginyoutube)

        self.musicUI = QMainWindow()
        self.musichandle = MUSIC_HANDLE(self.musicUI)
        self.musichandle.pushButton_14.clicked.connect(lambda:self.brmusic())
                
        self.loadingUI = QMainWindow()
        self.loadinghandle = LOADING_HANDLE(self.loadingUI)
        self.loadinghandle.timer = QtCore.QTimer()
        self.loadinghandle.timer.timeout.connect(lambda: self.progress())
        self.loadinghandle.timer.start(35)


        self.camUI = QMainWindow()
        self.camhandle = CAM_HANDLE(self.camUI)
        self.camhandle.pushButton_3.clicked.connect(lambda:self.lvcam())

        self.menuUI = QMainWindow()
        self.menuhandle = MENU_HANDLE(self.menuUI)
        self.menuhandle.pushButton_4.clicked.connect(lambda:self.dnmenu())

        if pkDieuhoa1 == 0:
            if self.livingroomhandle.checkBox.isChecked()== True:
                pass
            else:
                self.livingroomhandle.checkBox.click()

        self.loadingUI.show()     
    def dnmenu(self):
        self.menuUI.hide()
        self.dinUI.show()
    def loadmenu(self):
        self.dinUI.hide()
        self.menuUI.show()
    def progress(self):
        global counter        
        self.loadinghandle.progressBar.setValue(counter)
        print(counter)
        if counter > 30:
            self.loadinghandle.label_3.setText("Loading 30%")
        if counter > 60:
            self.loadinghandle.label_3.setText("Gan Duoc Roi")
    
        if counter > 90:
            self.loadinghandle.label_3.setText("Do")
        if counter > 100:
                # STOP TIMER
            self.loadinghandle.timer.stop()

            self.loadingUI.close()
            print("Vao trang dang nhap")
            self.loginUI.show()

            # INCREASE COUNTER
        counter += 1  
    def loadgame(self):
        self.dinnerUI.hide()
        from main import run,reset,close
        reset()
        run()
        close()
        self.dinnerUI.show()
    
    def lvcam(self):
        self.camUI.close()
        self.livingUI.show()

    def mocam(self):
        self.livingUI.close()  
        self.camUI.show()
    def dhlv(self):
        if self.livingroomhandle.checkBox.isChecked() == True:
            print("dieu hoa phong khach tat")
            self.dieuhoahandle.checkBox.setEnabled(1)
            self.dieuhoahandle.checkBox.click()
            self.dieuhoahandle.sliderCPU.setEnabled(0)
            self.dieuhoahandle.checkBox.setEnabled(0)
            pkDieuhoa2= firebase.put(pk,pkDieuhoa, 0)
        else:
            print("dieu hoa phong khach bat")
            self.dieuhoahandle.checkBox.setEnabled(1)
            self.dieuhoahandle.checkBox.click()
            self.dieuhoahandle.sliderCPU.setEnabled(1)
            self.dieuhoahandle.checkBox.setEnabled(0)
            pkDieuhoa2= firebase.put(pk,pkDieuhoa, 1)
    def brmusic(self):
        self.musicUI.close()
        self.dinnerUI.show()
        print("mo phong ngu")
    def loadlvdi(self):
        self.dinUI.hide()
        self.livingUI.show()
        print("Mo phong khach")
    def loaddndi(self):
        self.dinUI.hide()
        self.dinnerUI.show()
        print("Mo phong ngu")
    def loadktdi(self):
        self.dinUI.hide()
        self.kitchenUI.show()
        print("Mo phong bep")
    def loadlogindi(self):
        self.dinUI.hide()
        self.loginUI.show()
        print("Tro ve trang dang nhap")

    def loadktlv(self):
        self.livingUI.hide()
        self.kitchenUI.show()
        print("Mo phong bep")
        
    def loaddilv(self):
        self.livingUI.hide()
        self.dinUI.show()
        print("Mo phong an")
    def loaddhlv(self):
        self.livingUI.hide()
        self.dieuhoaUI.show()
        print("Mo dieu hoa")

    def loadktdn(self):
        self.dinnerUI.hide()
        self.kitchenUI.show()
        print("Mo phong bep")

    def loadlvkt(self):
        self.kitchenUI.hide()
        self.livingUI.show()
        print("Mo phong khach")
    def loaddinnerkt(self):
        self.kitchenUI.hide()
        self.dinnerUI.show()
        print("Mo phong ngu")
    def loaddikt(self):
        self.kitchenUI.hide()
        self.dinUI.show()
        print("Mo phong an")

    
    def login(self):
        id = self.loginhandle.lineEdit_2.text()
        password = self.loginhandle.lineEdit.text()     
        
        if id == "taikhoan" and password == "matkhau":
            self.loadMainForm()
            print("taikhoan: ",id)  
            print("mat khau: ",password)
            self.loginhandle.textEdit.setText("")
            print("Phong khach")
        else:
            self.loginhandle.textEdit.setText("Error")
            print("Sai tai khoan hoac mat khau")
    def loadloginlv(self):
        self.livingUI.hide()
        self.loginUI.show()
        print("Tro ve trang dang nhap")

    def loadlogindn(self):
        self.dinnerUI.hide()
        self.loginUI.show()
        print("Tro ve trang dang nhap")
    def loaddidn(self):
        self.dinnerUI.hide()
        self.dinUI.show()
        print("Mo phong an")
    def loadmusicdn(self):
        self.dinnerUI.hide()
        self.musicUI.show()
        print("Mo nhac")
    
    def loadloginkt(self):
        self.kitchenUI.hide()
        self.loginUI.show()
        print("Tro ve trang dang nhap")

    def loadMainForm(self):       
        self.loginUI.hide()
        self.livingUI.show()
        print("Mo phong khach")
    def loadliving(self):
        self.dinnerUI.hide()
        self.livingUI.show()
        print("Mo phong khach")
    def loaddinnerroom(self):
        self.livingUI.hide()
        self.dinnerUI.show()
        print("Mo phong ngu")

    def loadlvdh(self):
        self.dieuhoaUI.hide()
        self.livingUI.show()
        print("Tro ve phong khach")
    def loginfb(self):
        driver = webdriver.Chrome()
        driver.get('https://www.facebook.com/s2nmt')
        
        self.sleep(5)
    def loginyoutube(self):
        driver = webdriver.Chrome()
        driver.get('https://www.youtube.com/')
        self.sleep(5)

        
if __name__ == "__main__":
    app = QApplication([])  
    ui =UI()
    app.exec_()