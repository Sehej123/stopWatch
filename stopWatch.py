from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Watch")
        self.setGeometry(100, 100, 400, 500)
        self.uiComponent()
        self.show()
    
    def uiComponent(self):
        self.count = 0
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(75,100,250,70)
        self.label.setStyleSheet('Border:4px Solid Black;')
        self.label.setText(str(self.count))
        self.label.setFont(QFont("Arial",25))
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton('start', self)
        start.setGeometry(125,250,150,40)
        start.pressed.connect(self.startButton)
        pause = QPushButton('pause', self)
        pause.setGeometry(125, 300, 150,40)
        pause.pressed.connect(self.pauseButton)
        restart = QPushButton('restart', self)
        restart.setGeometry(125, 350, 150, 40)
        restart.pressed.connect(self.restartButton)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
    
    def showTime(self):
        if self.flag == True:
            self.count+=1
        
        text=(str(self.count/10))
        self.label.setText(text)

    
    def pauseButton(self):
        self.flag = False
   
    
    def startButton(self):
        self.flag = True

    def restartButton(self):
        self.flag = False
        self.count = 0

        count=(str(self.count))
        self.label.setText(count)        


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
    
