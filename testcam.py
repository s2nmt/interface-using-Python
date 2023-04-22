import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from cam import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class CAM_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)

        self.pushButton.clicked.connect(self.start_capture_video)
        self.pushButton_2.clicked.connect(self.stop_capture_video)

        self.thread = {}
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
        print("Bat cam", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv2.VideoCapture(0)  # 'D:/8.Record video/My Video.mp4'
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.signal.emit(cv_img)
    def stop(self):
        print("Tam dung", self.index)
        self.terminate()

