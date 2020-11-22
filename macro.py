import threading
from time import sleep
import pyautogui
import serial
import keyboard
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QComboBox
currentMouseX, currentMouseY= pyautogui.position()

# 아두이노와 연동한 키보드 입력 매크로

def control(n):   # 매크로1, MyApp.cd[0] ~ MyApp.cd[5]에 지정한 키를 입력
    global flag
    if n == "1" :
        pyautogui.press([MyApp.cd[0],MyApp.cd[1],MyApp.cd[2]])
        if keyboard.is_pressed([MyApp.ch0,MyApp.ch1,MyApp.ch2]) :             
            flag = 1
    elif n == "2" :
        pyautogui.press([MyApp.cd[3],MyApp.cd[4],MyApp.cd[5]])
        if keyboard.is_pressed([MyApp.ch0,MyApp.ch1,MyApp.ch2]) :
            flag = 1

def controll(n):    # 매크로2, MyApp.cd[6] ~ MyApp.cd[11]에 지정한 키를 입력
    global flag
    if n == "1" :
        pyautogui.press([MyApp.cd[6],MyApp.cd[7],MyApp.cd[8]])
        if keyboard.is_pressed([MyApp.ch0,MyApp.ch1,MyApp.ch2]) :
            flag = 0
    elif n == "2" :
        pyautogui.press([MyApp.cd[9],MyApp.cd[10],MyApp.cd[11]])
        if keyboard.is_pressed([MyApp.ch0,MyApp.ch1,MyApp.ch2]) :
            flag = 0

def threadin():     # 시리얼 통신을 위한 스레드, 포트와 보드레이트를 입력
    ard = serial.Serial(MyApp.PORT, MyApp.baudrate)
    global flag
    flag = 1
    while True:     
        num = ard.readline()    # 블루투스로 부터 숫자를 읽어
        nu = num.decode()
        n = nu[:1]
        if flag == 0 :
            control(n)
        elif flag == 1 :
            controll(n)

t1=threading.Thread(target=threadin)

class MyApp(QWidget):   # Pyqt를 이용한 gui class, 위치는 수동으로 지정

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        Lab1 = QLabel('보드레이트',self)
        Lab1.move(30, 10)

        self.l1 = QLineEdit(self)
        self.l1.setPlaceholderText('ex): 9600')
        self.l1.move(30, 30)        
        
        Lab2 = QLabel('포트',self)
        Lab2.move(30, 60)

        self.l2 = QLineEdit(self)
        self.l2.setPlaceholderText('ex); COM3')
        self.l2.move(30,80)        
        
        Lab3 = QLabel('모드1 :',self)
        Lab3.move(30, 130)

        self.LE1 = QLineEdit(self)
        self.LE1.move(85,130)
        self.LE1.resize(50,20)

        LAB1 = QLabel('+',self)
        LAB1.move(145,130)
        
        self.LE2 = QLineEdit(self)
        self.LE2.move(165,130)
        self.LE2.resize(50,20)

        LAB2 = QLabel('+',self)
        LAB2.move(225,130)

        self.LE3 = QLineEdit(self)
        self.LE3.move(245,130)
        self.LE3.resize(50,20)

        self.LIE1 = QLineEdit(self)
        self.LIE1.move(85,160)
        self.LIE1.resize(50,20)

        LABE1 = QLabel('+',self)
        LABE1.move(145,160)
        
        self.LIE2 = QLineEdit(self)
        self.LIE2.move(165,160)
        self.LIE2.resize(50,20)

        LABE2 = QLabel('+',self)
        LABE2.move(225,160)

        self.LIE3 = QLineEdit(self)
        self.LIE3.move(245,160)
        self.LIE3.resize(50,20)
        
        Lab4 = QLabel('모드2 :',self)
        Lab4.move(30, 200)

        self.LE4 = QLineEdit(self)
        self.LE4.move(85,200)
        self.LE4.resize(50,20)

        LAB3 = QLabel('+',self)
        LAB3.move(145,200)
        
        self.LE5 = QLineEdit(self)
        self.LE5.move(165,200)
        self.LE5.resize(50,20)

        LAB4 = QLabel('+',self)
        LAB4.move(225,200)

        self.LE6 = QLineEdit(self)
        self.LE6.move(245,200)
        self.LE6.resize(50,20)
        
        self.LIE4 = QLineEdit(self)
        self.LIE4.move(85,230)
        self.LIE4.resize(50,20)

        LABE3 = QLabel('+',self)
        LABE3.move(145,230)
        
        self.LIE5 = QLineEdit(self)
        self.LIE5.move(165,230)
        self.LIE5.resize(50,20)
        
        LABE4 = QLabel('+',self)
        LABE4.move(225,230)

        self.LIE6 = QLineEdit(self)
        self.LIE6.move(245,230)
        self.LIE6.resize(50,20)
        
        Lab4 = QLabel('모드변경: ',self)
        Lab4.move(30, 260)

        self.cmb1 = QComboBox(self)
        self.cmb1.addItem('ctrl')
        self.cmb1.addItem('shift')
        self.cmb1.addItem('p')
        self.cmb1.addItem('q')
        self.cmb1.move(100, 260)
        
        LABEE1 = QLabel('+',self)
        LABEE1.move(170,260)

        self.cmb2 = QComboBox(self)
        self.cmb2.addItem('ctrl')
        self.cmb2.addItem('shift')
        self.cmb2.addItem('p')
        self.cmb2.addItem('q')
        self.cmb2.move(185, 260)

        
        LABEE2 = QLabel('+',self)
        LABEE2.move(255,260)

        self.cmb3 = QComboBox(self)
        self.cmb3.addItem('ctrl')
        self.cmb3.addItem('shift')
        self.cmb3.addItem('p')
        self.cmb3.addItem('q')
        self.cmb3.move(270, 260)

        
        self.start_btn = QPushButton('Start', self)        
        self.start_btn.setCheckable(True)
        self.start_btn.move(30, 300)
        self.start_btn.clicked.connect(self.button_click)
                        
        self.setWindowTitle('매크로 설정')
        self.setGeometry(400, 400, 370, 350)
        self.show()

    def button_click(self):     # 버튼 클릭 함수
        MyApp.baudrate = self.l1.text()
        MyApp.PORT = self.l2.text()
        MyApp.cd = [self.LE1.text(), self.LE2.text(), self.LE3.text(),
                    self.LIE1.text(), self.LIE2.text(), self.LIE3.text(),
                    self.LE4.text(), self.LE5.text(), self.LE6.text(),
                    self.LIE4.text(), self.LIE5.text(), self.LIE6.text()] 
        MyApp.ch0 = self.cmb1.currentText()
        MyApp.ch1 = self.cmb2.currentText()
        MyApp.ch2 = self.cmb3.currentText()
        t1.start()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
        
