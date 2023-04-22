# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dinnerroom.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import buttonn
class moWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(moWidget, self).__init__(parent)
        self.parent = parent
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self,event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.parent.move(event.globalPos() - self.dragPosition)
            event.accept()


class Ui_MainWindow(object):
    def setTime(self): 
        time = QtCore.QTime.currentTime()
        text = time.toString("HH:mm")
        self.label_4.setText(text) 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 750)
        MainWindow.setStyleSheet("background-color: rgb(0,0,0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 135, 90, 135))
        self.checkBox.setStyleSheet("QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/musicoff.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/musicon.png);\n"
"\n"
"}\n"
"")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 335, 90, 135))
        self.checkBox_2.setStyleSheet("QCheckBox::indicator:checked{    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/routeroff.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/routeron.png);\n"
"\n"
"}")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 135, 90, 135))
        self.checkBox_3.setStyleSheet("QCheckBox::indicator:checked{    \n"
"    \n"
"    image: url(:/newPrefix/lightoff.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"    \n"
"    image: url(:/newPrefix/lighton.png);\n"
"\n"
"}\n"
"")
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(190, 335, 90, 135))
        self.checkBox_5.setStyleSheet("QCheckBox::indicator:checked{    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/printoff.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/newPrefix/printon.png);\n"
"\n"
"}")
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(375, 210, 41, 141))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(325, 254, 50, 141))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton#pushButton_2{\n"
"    color: rgb(255, 255, 255);\n"
"    background-image: url(:/newPrefix/bedrom0.png);\n"
"\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: rgb(17, 17,17);\n"
"    \n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgb(17, 17,17);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(325, 120, 50, 131))
        self.pushButton_3.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"background-image: url(:/newPrefix/livingroom173.png);\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(325, 400, 50, 141))
        self.pushButton_4.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"background-image: url(:/newPrefix/kitchen17.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(325, 555, 50, 141))
        self.pushButton_5.setStyleSheet("background-image: url(:/newPrefix/diner17.png);\n"
"background-color: rgb(17, 17, 17);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(325, 536, 51, 20))
        self.label.setStyleSheet("background-color: rgb(17,17, 17);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(325, 695, 55, 61))
        self.label_3.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(325, 45, 51, 81))
        self.label_2.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 710, 41, 41))
        self.pushButton_6.setStyleSheet("background-image: url(:/newPrefix/trove.png);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 10, 120, 21))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, -10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-position:center;\n"
"background-repeat:no-repeat;")
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 230, 31, 28))
        self.pushButton_7.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.pushButton_8.setStyleSheet("background-image: url(:/newPrefix/game.png);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.setTime)
        timer.start(1000)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "10:10"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())