import sys
import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__
        self.resize(500,500)

        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container {backgroud-color: #222")
        self.layout = QVBoxLayout()

        self.toggle = QCheckBox()
        