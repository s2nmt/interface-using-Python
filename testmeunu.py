import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from Menu import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MENU_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        states_cities = [
            'Phim 1',
            'Phim 2',
            'Phim 3',
            'Phim 4',
            'Phim 5',
            'Phim 6',
            'Phim 7',
            'Phim 8',
            'Phim 9',
            'Phim 10'
        ]


        menu = QMenu()
        menu.triggered.connect(lambda x: print(x.text()))

        self.pushButton.setMenu(menu)
        self.add_menu(states_cities, menu)

        self.pushButton_2.clicked.connect(self.start_capture_video)
        self.pushButton_3.clicked.connect(self.stop_capture_video)
        self.pushButton_6.clicked.connect(self.volumeUp)
        self.pushButton_5.clicked.connect(self.volumeDown)

        self.thread = {}
        self.player = QMediaPlayer()
    def volumeUp(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def add_menu(self, data, menu_obj):
        if isinstance(data, dict):
            for k, v in data.items():
                sub_menu = QMenu(k, menu_obj)
                menu_obj.addMenu(sub_menu)
                self.add_menu(v, sub_menu)
        elif isinstance(data, list):
            for element in data:
                self.add_menu(element, menu_obj)
        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)
    def closeEvent(self, event):
        self.stop_capture_video()
    def stop_capture_video(self):
        self.thread[1].stop()
    def start_capture_video(self):
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)

    def show_wedcam(self, cv_img):

        qt_img = self.convert_cv_qt(cv_img)
        self.label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):

        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(371, 291, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)
    def __init__(self, index):
        self.index = index
        print("Mo phim", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv2.VideoCapture('C:/Users/Minh Tuan/Documents/python/main 1/phim.mp4')
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.signal.emit(cv_img)
    def stop(self):
        print("Tam dung", self.index)
        self.terminate()

