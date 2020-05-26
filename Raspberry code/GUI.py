# RaspberryPi username: raspberrypi; password: Glados

import sys
from functools import partial
import socket
import platform
import os
import time

from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QColorDialog
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette, QColor
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer

UDP_IP1 = "192.168.1.177"
UDP_IP2 = "192.168.1.42"

UDP_PORT = 5004
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)

class Light():
    lightbtn = 0 
    lightname = ''    
    laddr = 0
    IP1 = "..."
    IP2 = "..."
    lard = 0
    redd = 255
    greenn = 0
    bluee = 0
    def __init__(self):
        lightbtn = 0
        
class Joe():
    lights = [[]]
    def _init_(self):
        print("no")


class Control(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.elbows = Joe()
        box = []
        lightcount = 0
        senseirData = 0
        
        numAL = self.pingPong()
        labelGeo=[]
        
        senseir = QLabel(self)
        dateir = QLabel(self)
        senseir.setText("Sensor Reading")
        dateir.setText('%d' % senseirData)
        senseir.setGeometry(660,395,100,40)
        dateir.setGeometry(660,410,60,40)
        
        for i in range(len(numAL[0])):
            labelGeo.append(65+numAL[1][i]*65)
            
        for i in range(len(numAL[0])):
            self.elbows.lights[0].append(QPushButton(self))
            self.elbows.lights.append([])
            box.append(QLabel(self))
            box[i].setStyleSheet("border: 2px solid black;" )
            box[i].setGeometry(5,15+55*i, 60+numAL[1][i]*70,50)
            for j in range (numAL[1][i]):
                self.elbows.lights[i+1].append(Light())
                lightcount = lightcount + 1
                self.elbows.lights[i+1][j].lightname = "light%d" % (lightcount)
                self.elbows.lights[i+1][j].lightbtn = QPushButton(self)
                self.elbows.lights[i+1][j].lightbtn.setText("Light %d" % (lightcount))
                self.elbows.lights[i+1][j].lard = i+1
                self.elbows.lights[i+1][j].laddr = j+1
                self.elbows.lights[i+1][j].lightbtn.clicked.connect(partial(self.lgtPressed,self.elbows.lights[i+1][j]))
                self.elbows.lights[i+1][j].lightbtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 2px solid black;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
                self.elbows.lights[i+1][j].lightbtn.setGeometry(70 + 69*j,20 + 55*i,66,40)
        
        
        buttonNum = [1, 2]
        self.elbows.lights[1][0].IP1 = UDP_IP1     
        self.elbows.lights[1][0].IP2 = UDP_IP2        
        
        #size
        self.setFixedSize(800, 480)
        self.center
        
        #Label2
        self.label2 = QLabel(self)
        for i in range(len(numAL[0])):       

            # Creates arduino buttons and places them on the window
            self.elbows.lights[0][i].setText("A%d" % (i+1))
            self.elbows.lights[0][i].clicked.connect(partial(self.pressedard,self.elbows,i))
            self.elbows.lights[0][i].setStyleSheet("background-color: rgb(0,0,0);"
                           "border: 2px solid black;"
                           "color: rgb(255,255,255);"
                           "font: bold italic 10pt 'Times New Roman';")
            self.elbows.lights[0][i].setGeometry(10, 30+55*i, 35, 20)
            self.elbows.lights[0][i].raise_()

        #Butts
        self.Ebtn = QPushButton(self)
        self.Ebtn.setText("Exit")
        self.Ebtn.clicked.connect(self.exitButton)
        self.Ebtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid black;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
        self.Ebtn.setGeometry(735,20,60,40)

        self.show()
        
    # center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def sendInfo(self, red, blue, green, ard, light, sendIP, sendIP2):
        print("Red: %d; Blue: %d; Green: %d; Light address: %d" % (red, blue, green, light))       
        print("%s %d %d %d %d " % (sendIP, light, red, green, blue))
        return_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        start = time.time()
        # sock.sendto(("%d %d %d %d " % (light, red, green, blue)).encode('utf-8'), (sendIP, UDP_PORT)) 
        # try:
            # data, server = return_sock.recvfrom(1024)
            # end = time.time()
            # elapsed = end - start
            # print('{data}{elapsed}')
        # except socket.timeout:
            # print('REQUEST TIMED OUT')
            # print('trying secondary bus')
            # start = time.time()
            # sock.sendto(("%d %d %d %d " % (light, red, green, blue)).encode('utf-8'), (sendIP2, UDP_PORT))
            # try:
                # data, server = return_sock.recvfrom(1024)
                # end = time.time()               
                # elapsed = end - start
                # print('{data}{elapsed}')
            # except socket.timeout:
                # print('REQUEST TIMED OUT')
                # print('FATAL ERROR')
                # print('SECONDARY BUS DOWN')
		
    def exitButton(self):
	    sys.exit()
        
    def lgtPressed(self, lightP):
        self.hide()
        colour = QColorDialog.getColor()
        print(lightP.lightbtn)
        if colour.isValid():
            lightP.redd = int(colour.red())
            lightP.bluee = int(colour.blue())
            lightP.greenn = int(colour.green())
            light = lightP.lightname
            # print(lightP.lightname)
            lightP.lightbtn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;" #"border-color: red;")
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(lightP.redd, lightP.bluee, lightP.greenn, lightP.lard, lightP.laddr, lightP.IP1, lightP.IP2)
                
        self.show()
        
    def lgtPressed1(self, ardnum,lgtnum):
        self.hide()
        colour = QColorDialog.getColor()
        # print(lightP.lightbtn)
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            light = self.elbows.lights[ardnum+1][lgtnum].lightname
            # print(lightP.lightname)
            self.elbows.lights[ardnum+1][lgtnum].lightbtn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;" #"border-color: red;")
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, ardnum+1, lgtnum+1)
                
        self.show()
        
    def pressedard(self, selbows, ard):
        self.hide()
        colour = QColorDialog.getColor()
        red = int(colour.red())
        blue = int(colour.blue())
        green = int(colour.green())
        
        if colour.isValid():
            # print(len(self.elbows.lights[ard]))
            for i in range(len(selbows.lights[ard+1])):
                selbows.lights[ard+1][i].lightbtn.redd = int(colour.red())
                selbows.lights[ard+1][i].lightbtn.bluee = int(colour.blue())
                selbows.lights[ard+1][i].lightbtn.greenn = int(colour.green())
                selbows.lights[ard+1][i].lightbtn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                    "background-color: rgb(0,0,0);"
                    "border-style: solid;"
                    "color: rgb(255,255,255);"
                    "border-width: 2px;"
                    "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                  
        for i in range(len(self.elbows.lights[ard+1])):
                self.sendInfo(red, blue, green, self.elbows.lights[ard+1][i].lard, self.elbows.lights[ard+1][i].laddr, self.elbows.lights[ard+1][i].IP1, self.elbows.lights[ard+1][i].IP2)
                
        self.show()
        
    # def pressedard1(self):
        # self.hide()
        # colour = QColorDialog.getColor()
        # if colour.isValid():
            # red = int(colour.red())
            # blue = int(colour.blue())
            # green = int(colour.green())
            # light = ["light1", "light2", "light3", "light4"]
            # self.btn4.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                # "background-color: rgb(0,0,0);"
                # "border-style: solid;"
                # "color: rgb(255,255,255);"
                # "border-width: 2px;"
                # "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            # self.btn3.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                # "background-color: rgb(0,0,0);"
                # "border-style: solid;"
                # "color: rgb(255,255,255);"
                # "border-width: 2px;"
                # "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            # self.btn2.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                # "background-color: rgb(0,0,0);"
                # "border-style: solid;"
                # "color: rgb(255,255,255);"
                # "border-width: 2px;"
                # "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
            # self.btn.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                # "background-color: rgb(0,0,0);"
                # "border-style: solid;"
                # "color: rgb(255,255,255);"
                # "border-width: 2px;"
                # "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))                
                
            # for i in range(len(light)):
                # self.sendInfo(red, blue, green, light[i])
            
        # self.show()
        
        
    def sensorRead(self):
        return 200
        
    def pingPong(self): # array organized as len(arr[]) == number of arduinos, arr[][i] returns number of lights connected to arduino. Current usable max return [[1,1,1,1,1,1,1,1],[8,8,8,8,8,8,8,8]]
        return [[1,1,1,1,1,1,1,1],[8,8,8,8,8,8,8,8]]
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = Control()
sys.exit(app.exec_())