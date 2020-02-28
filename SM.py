from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout
import sys
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.InitWindow()
        
    def InitWindow(self):
        self.setStyleSheet("background:gray")
        self.setWindowTitle("HomeScreen")
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Map")
        self.b1.move(600,550)
        self.b1.clicked.connect(self.map1)

        b2 = QtWidgets.QPushButton(self)
        b2.setText("Classes")
        b2.move(720,550)
        b2.clicked.connect(self.cls)

        b3 = QtWidgets.QPushButton(self)
        b3.setText("Cam")
        b3.move(840,550)
        b3.clicked.connect(self.cam)

        b4 = QtWidgets.QPushButton(self)
        b4.setText("Lecturer")
        b4.move(960,550)
        b4.clicked.connect(self.lec)

        b5 = QtWidgets.QPushButton(self)
        b5.setText("Exam")
        b5.move(1080,550)
        b5.clicked.connect(self.exam)

        b6 = QtWidgets.QPushButton(self)
        b6.setText("Website")
        b6.move(1200,550)
        b6.clicked.connect(self.site)
        
        self.showMaximized()
 
    def map1(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()
    def cam(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()
        

    def lec(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()

    def cls(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()
    def site(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()
    def exam(self):
        mydialog = QDialog(self)
        bh = QtWidgets.QPushButton(mydialog)
        bh.setText("Home")
        bh.move(400,950)
        bh.clicked.connect(lambda: mydialog.hide())
        mydialog.showMaximized()
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
