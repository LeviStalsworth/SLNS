# RaspberryPi username: raspberrypi; password: Glados

import sys

from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar, QColorDialog
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette, QColor
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer

# class Light():
    # lightbtn = 0    
    # laddr = 0
    # redd = 255
    # greenn = 0
    # bluee = 0
    # def __init__(self):
        # lightbtn = 0
        # print(lightbtn, self.laddr, self.redd, self.greenn, self.bluee)
        
# class Joe():
    # lights = [[],[]]
    # def _init_(self):
        # print("no")


class cssden(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        # bill = Joe()
        
        numAL = self.pingPong()
        labelGeo=[]
        
        for i in range(len(numAL[0])):
            labelGeo.append(65+numAL[1][i]*65)
            
        # for i in range(len(numAL[0])):
            # bill.lights[0].append(QPushButton(self))
            # for j in range (len(numAL[1])):
                # bill.lights[1].append(Light())

        # print(bill.lights[1][0].lightbtn)

        # buttonNum = [1, 2]
        
        #size
        self.setFixedSize(800, 480)
        self.center
        
        self.lgt1 = QPushButton(self)
        self.lgt2 = QPushButton(self)
        self.Abtn2 = QPushButton(self)
        
        # Label1
        # self.label1 = QLabel(self)
        # self.label1.setText("Sensor Reading: %d" % self.sensorRead())

        # self.label1.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label1.setGeometry(350,200,120,40)
        
        #Label2
        # self.label2 = QLabel(self)
        # print(bill.lights)
        # for i in range(len(numAL[0])):
            # self.label2.setStyleSheet("border: 2px solid red;" )
            # self.label2.setGeometry(5,15,labelGeo[0],50) # 249         

            # ArduinoButts
            # bill.lights[0][i].setText("A%d" % (i+1))
            # bill.lights[0][i].clicked.connect(lambda: self.pressedard(bill, i))
            # bill.lights[0][i].setStyleSheet("background-color: rgb(0,0,0);"
                           # "border: 2px solid red;"
                           # "color: rgb(255,255,255);"
                           # "font: bold italic 10pt 'Times New Roman';")
            # bill.lights[0][i].setGeometry(10, 30+(65*i), 35, 20)
            
            # for j in range(numAL[1][i]):
                # Butts
                # bill.lights[1][j].lightbtn = QPushButton(self)
                # bill.lights[1][j].lightbtn.setText("Light %d" % (j+1))
                # print(bill.lights[1][j].lightbtn)
                # bill.lights[1][j].lightbtn.clicked.connect(lambda: self.lgtPressed(bill.lights[1][j]))
                # bill.lights[1][j].lightbtn.setStyleSheet("background-color: rgb(0,0,0);"
                               # "border: 2px solid red;"
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
                # bill.lights[1][j].lightbtn.setGeometry(70 + 65*j,20,60,40)

            
        
        if len(numAL[0]) > 0:
            # Label2
            # self.label3 = QLabel(self)

            # self.label3.setStyleSheet(# "background-color: rgb(0,0,0);"
                                   # "border: 2px solid red;" )
                                   # "color: rgb(255,255,255);"
                                   # "font: bold italic 12pt 'Times New Roman';")
            # self.label3.setGeometry(5,5,labelGeo[0],50)
            
            #ArduinoButt
            self.Abtn2.setText("A1")
            self.Abtn2.clicked.connect(self.pressedard1)
            self.Abtn2.setStyleSheet("background-color: rgb(0,0,0);"
                                   "border: 2px solid red;"
                                   "color: rgb(255,255,255);"
                                   "font: bold italic 10pt 'Times New Roman';")
            self.Abtn2.setGeometry(10,20,35,20)
            
            # lgtButts
            self.lgt1.setText("Light%d" % (0+1))
            self.lgt2.setText("Light%d" % (1+1))
            self.lgt1.clicked.connect(self.pressedlgt1)
            self.lgt2.clicked.connect(self.pressedlgt2)
            self.lgt1.setStyleSheet("background-color: rgb(0,0,0);"
                           "border: 2px solid red;"
                           "color: rgb(255,255,255);"
                           "font: bold italic 10pt 'Times New Roman';")
            self.lgt2.setStyleSheet("background-color: rgb(0,0,0);"
                           "border: 2px solid red;"
                           "color: rgb(255,255,255);"
                           "font: bold italic 10pt 'Times New Roman';")
            self.lgt1.setGeometry(70 + 65*0,10,60,40)
            self.lgt2.setGeometry(70 + 65*1,10,60,40)
        
        # Label2
        # self.label4 = QLabel(self)

        # self.label4.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label4.setGeometry(5,125,249,50)
        
        # Label2
        # self.label5 = QLabel(self)
        # self.label5.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label5.setGeometry(5,180,249,50)
        
        # Label2
        # self.label6 = QLabel(self)

        # self.label6.setStyleSheet(# "background-color: rgb(0,0,0);"
                               # "border: 2px solid red;" )
                               # "color: rgb(255,255,255);"
                               # "font: bold italic 12pt 'Times New Roman';")
        # self.label6.setGeometry(5,235,249,50)

        #Butts
        self.Ebtn = QPushButton(self)
        self.Ebtn.setText("Exit")
        self.Ebtn.clicked.connect(self.exitButton)
        self.Ebtn.setStyleSheet("background-color: rgb(0,0,0);"
                               "border: 1px solid red;"
                               "color: rgb(255,255,255);"
                               "font: bold italic 12pt 'Times New Roman';")
        self.Ebtn.setGeometry(735,10,60,40)

        self.show()
        
    # center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def sendInfo(self, red, blue, green, ard, light):
        print("Red: %d; Blue: %d; Green: %d; Arduino Adress; %s; Light address: %s" % (red, blue, green, ard, light))
        
		
    def exitButton(self):
	    sys.exit()
        
    def pressedard1(self):
        self.hide()
        colour = QColorDialog.getColor()
        if colour.isValid():
            red = int(colour.red())
            blue = int(colour.blue())
            green = int(colour.green())
            lights = ["light1","light2"]

            self.lgt1.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;" #"border-color: red;")
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.lgt2.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                "background-color: rgb(0,0,0);"
                "border-style: solid;"
                "color: rgb(255,255,255);"
                "border-width: 2px;" #"border-color: red;")
                "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                
            self.sendInfo(red, blue, green, "ard1", lights[0])
            self.sendInfo(red, blue, green, "ard1", lights[1])
                
        self.show()
        
    def pressedlgt1(self):
        self.hide()
        colour = QColorDialog.getColor()
        red = int(colour.red())
        blue = int(colour.blue())
        green = int(colour.green())
        
        if colour.isValid():
            self.lgt1.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                    "background-color: rgb(0,0,0);"
                    "border-style: solid;"
                    "color: rgb(255,255,255);"
                    "border-width: 2px;"
                    "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                  
            self.sendInfo(red, blue, green, "ard1", "lgt1")
                
        self.show()
        
    def pressedlgt2(self):
        self.hide()
        colour = QColorDialog.getColor()
        red = int(colour.red())
        blue = int(colour.blue())
        green = int(colour.green())
        
        if colour.isValid():
            self.lgt2.setStyleSheet("font: bold italic 12pt 'Times New Roman';"
                    "background-color: rgb(0,0,0);"
                    "border-style: solid;"
                    "color: rgb(255,255,255);"
                    "border-width: 2px;"
                    "border-color: rgb( %d, %d, %d);" % (colour.red(), colour.green(), colour.blue()))
                  
            self.sendInfo(red, blue, green, "ard1", "lgt2")
                
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
        
    def pingPong(self):
        return [[1],[2]]
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())