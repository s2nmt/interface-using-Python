

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from dieuhoa import Ui_MainWindow
from firebase import firebase

firebase = firebase.FirebaseApplication('https://esp32-2b360-default-rtdb.firebaseio.com', None)
pk = 'PHONG_KHACH'
pkNhietdo = 'NHIETDO'




class DIEUHOA_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        pkNhietdo1 = firebase.get(pk, pkNhietdo)
        def setValue(self, slider, labelPercentage, progressBarName, color):

            value = slider.value()
            sliderValue = int(value)


            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

            # CALL DEF progressBarValue
            self.progressBarValue(sliderValue, progressBarName, color)
        self.sliderCPU.valueChanged.connect(lambda: setValue(self, self.sliderCPU, self.labelPercentageCPU_2, self.circularProgressCPU_2, "rgba(85, 170, 255, 255)"))
        self.sliderCPU.setValue(pkNhietdo1*10//4)

        self.checkBox_2.stateChanged.connect(self.debug2)
        self.checkBox_3.stateChanged.connect(self.debug3)
        self.checkBox_4.stateChanged.connect(self.debug4)
    def debug2(self):
        if self.checkBox_2.isChecked() == True:
            print("tat hoi lanh")
        else:
            print("bat hoi lanh")       
    def debug3(self):
        if self.checkBox_3.isChecked() == True:
            print("tat quat")
        else:
            print("bat quat")   
    def debug4(self):
        if self.checkBox_4.isChecked() == True:
            print("tat day gio")
        else:
            print("bat day gio")  
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        print("Nhiet do hien tai: ")
        print(value*4//10)
        pk2= firebase.put(pk,pkNhietdo, value*4//10)
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)





        
#if __name__ == "__main__":
 #   app = QtWidgets.QApplication(sys.argv)
  #  MainWindow = QtWidgets.QMainWindow()
  #  ui = DIEUHOA_HANDLE()

  #  MainWindow.show()
    
   # app.exec_()

