import sys, os
from time import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from music import Ui_MainWindow
import sys
class MUSIC_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow) :
        self.setupUi(mainwindow)
        self.pushButton.clicked.connect(self.playAudioFile1)
        self.pushButton_2.clicked.connect(self.playAudioFile2)
        self.pushButton_3.clicked.connect(self.playAudioFile3)
        self.pushButton_4.clicked.connect(self.playAudioFile4)
        self.pushButton_5.clicked.connect(self.playAudioFile5)
        self.pushButton_6.clicked.connect(self.playAudioFile6)
        self.pushButton_7.clicked.connect(self.playAudioFile7)
        self.pushButton_8.clicked.connect(self.playAudioFile8)
        self.pushButton_12.clicked.connect(self.playAudioFile9)
        self.pushButton_13.clicked.connect(self.playAudioFile10)

        self.pushButton_11.clicked.connect(self.volumeUp)
        self.pushButton_10.clicked.connect(self.volumeMute)
        self.pushButton_9.clicked.connect(self.volumeDown)

        self.player = QMediaPlayer()
        self.sliderCPU.sliderMoved.connect(self.setPosition)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
    def positionChanged(self, position):
        self.sliderCPU.setValue(position)

    def durationChanged(self, duration):
        self.sliderCPU.setRange(0, duration)
    def setPosition(self, position):
        self.player.setPosition(position)
    def positionChanged(self, position):
        self.sliderCPU.setValue(position)

    def volumeUp(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() # 
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def playAudioFile1(self):
        full_file_path = os.path.join(os.getcwd(), 'Anhthuongemnhama.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        
        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Anh thuong em nhat ma")


    def playAudioFile2(self):
        full_file_path = os.path.join(os.getcwd(), 'Chayvephiaanh.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Chay ve phia anh")
    def playAudioFile3(self):
        full_file_path = os.path.join(os.getcwd(), 'Damcuoinha.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Dam cuoi nha")
    def playAudioFile4(self):
        full_file_path = os.path.join(os.getcwd(), 'Gaclaiaulo.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Gac lai au lo")
    def playAudioFile5(self):
        full_file_path = os.path.join(os.getcwd(), 'Hoanokhongmau.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Hoa no khong mau")
    def playAudioFile6(self):
        full_file_path = os.path.join(os.getcwd(), 'Noinaycoanh.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Noi nay co anh")
    def playAudioFile7(self):
        full_file_path = os.path.join(os.getcwd(), 'Rangkhon.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Rang khon")
    def playAudioFile8(self):
        full_file_path = os.path.join(os.getcwd(), 'Thucgiacda.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Thuc giac da")
    def playAudioFile9(self):
        full_file_path = os.path.join(os.getcwd(), 'Tinhdau.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Tinh dau")
    def playAudioFile10(self):
        full_file_path = os.path.join(os.getcwd(), 'Tinhyeuxanhla.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
        self.player.play()
        print("Mo bai hat : Tinh yeu xanh la")
