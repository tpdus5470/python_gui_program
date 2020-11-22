import time, threading
from time import sleep
import serial
import sys
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QEventLoop, Qt, QDate, QTime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 아두이노와 연동한 스케줄 입력 매크로 
 
class Showcalendar(QDialog):    # 달력 다이어로그를 출력
    def __init__(self):
        super().__init__()
        self.initUI()
        self.date= None
        self.datee= None  
    def initUI(self):
        self.setGeometry(100, 100, 700, 550)
        self.setWindowTitle("calendar")
        self.cal = QCalendarWidget()
        self.cal.clicked.connect(self.calendarClicked)
        
        Clayout=QVBoxLayout()
        Clayout.addWidget(self.cal)
        self.setLayout(Clayout)

    def calendarClicked(self) :     # 버튼 입력함수, 설정한 날짜를 원하는 형태로 출력
        self.date=self.cal.selectedDate()
        self.datee=str(self.date)[21:23].lstrip()+"-"+str(self.date)[24:26].lstrip()+"-"+str(self.date)[-3:-1].lstrip()
        self.close()

class Showclock(QDialog):       # 시계 다이어로그를 출력, am/pm, 시, 분을 설정
    def __init__(self):
        super().__init__()
        self.initUI()
        self.time= None
    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("time")

        CKlayout=QGridLayout()
        self.rdam=QRadioButton("am",self)
        self.rdpm=QRadioButton("pm",self)
        
        hlabel=QLabel("시 :",self)
        self.clkh = QSpinBox(self)
        self.clkh.setRange(0,12)
        mlabel=QLabel("분 :",self)
        self.clkm = QSpinBox(self)
        self.clkm.setRange(0,60)
        
        self.clkbtn=QPushButton('선택',self)
        self.clkbtn.clicked.connect(self.clkbtnClicked)

        CKlayout.addWidget(self.rdam,0,0)
        CKlayout.addWidget(self.rdpm,0,1)
        CKlayout.addWidget(hlabel,1,0)
        CKlayout.addWidget(self.clkh,1,1)
        CKlayout.addWidget(mlabel,2,0)
        CKlayout.addWidget(self.clkm,2,1)
        CKlayout.addWidget(self.clkbtn,3,0)
        self.setLayout(CKlayout)

    def clkbtnClicked(self) :   #버튼 입력 함수, 설정한 시간을 원하는 형태로 출력
        if self.rdam.isChecked():
            ampm="AM"
        elif self.rdpm.isChecked():
            ampm="PM"
        else:
            ampm=""
        hour=str(self.clkh.value())
        minute=str(self.clkm.value())
        self.time=ampm + " " + hour + ":" + minute
        self.close()
    
class MainGui(QWidget):     # Pyqt를 이용한 gui class, 위치는 레이아웃으로 자동지정

    def __init__(self):
        super().__init__()

        setboxlayout=QGridLayout()
        baudlabel=QLabel('Baudrate',self)
        self.baudline = QLineEdit(self)
        self.baudline.setPlaceholderText('ex): 9600')
        portlabel=QLabel('Port',self)
        self.portline = QLineEdit(self)
        self.portline.setPlaceholderText('ex): COM9')
        self.setbtn=QPushButton('연결',self)
        self.stopbtn=QPushButton('연결 해제',self)
        setboxlayout.addWidget(baudlabel,0,0)
        setboxlayout.addWidget(self.baudline,0,1)
        setboxlayout.addWidget(portlabel,1,0)
        setboxlayout.addWidget(self.portline,1,1)
        setboxlayout.addWidget(self.setbtn,0,2)
        setboxlayout.addWidget(self.stopbtn,1,2)
        
        firstlayout=QGridLayout()
        TDLlabel=QLabel("To Do List",self)
        self.TDLcmb=QComboBox(self)
        self.TDLcmb.addItem('1')
        self.TDLcmb.addItem('2')
        self.TDLcmb.addItem('3')
        self.TDLcmb.addItem('4')
        self.TDLcmb.addItem('5')
        self.TDLline=QLineEdit(self)
        self.TDLline.setPlaceholderText("스케줄")
        self.TDLbtn=QPushButton('전송',self)
        firstlayout.addWidget(TDLlabel,0,0)
        firstlayout.addWidget(self.TDLcmb,1,0)
        firstlayout.addWidget(self.TDLline,2,0)
        firstlayout.addWidget(self.TDLbtn,2,1)

        secondlayout=QGridLayout()
        SDLlabel=QLabel("Schedule",self)
        self.SDLcmb=QComboBox(self)
        self.SDLcmb.addItem('1')
        self.SDLcmb.addItem('2')
        self.SDLcmb.addItem('3')
        self.SDLcmb.addItem('4')
        self.SDLcmb.addItem('5')
        self.ScDLbtn=QPushButton('날짜',self)
        self.SDLline=QLineEdit(self)
        self.SDLline.setPlaceholderText("목적지")
        self.ScDLline=QLineEdit(self)
        self.ScDLline.setPlaceholderText("목적")
        self.SchDLbtn=QPushButton('시간',self)
        self.SchDLline=QLineEdit(self)        
        self.SchDLline.setPlaceholderText("만날사람")
        self.SDLbtn=QPushButton('전송',self)
        secondlayout.addWidget(SDLlabel,0,0)
        secondlayout.addWidget(self.SDLcmb,1,0)
        secondlayout.addWidget(self.ScDLbtn,2,0)
        secondlayout.addWidget(self.SDLline,3,0)
        secondlayout.addWidget(self.ScDLline,4,0)
        secondlayout.addWidget(self.SchDLbtn,2,1)
        secondlayout.addWidget(self.SchDLline,3,1)
        secondlayout.addWidget(self.SDLbtn,4,1)

        thirdlayout=QGridLayout()
        IDPWlabel=QLabel("ID/PW",self)
        self.IDPWcmb=QComboBox(self)
        self.IDPWcmb.addItem('1')
        self.IDPWcmb.addItem('2')
        self.IDPWcmb.addItem('3')
        self.IDPWcmb.addItem('4')
        self.IDPWcmb.addItem('5')
        self.IDPWline=QLineEdit(self)
        self.IDPWline.setPlaceholderText("사이트")
        self.IDWline=QLineEdit(self)
        self.IDWline.setPlaceholderText("아이디")
        self.IPWline=QLineEdit(self)
        self.IPWline.setPlaceholderText("비밀번호")
        self.IDPWbtn=QPushButton("전송",self)
        thirdlayout.addWidget(IDPWlabel,0,0)
        thirdlayout.addWidget(self.IDPWcmb,1,0)
        thirdlayout.addWidget(self.IDPWline,2,0)
        thirdlayout.addWidget(self.IDWline,3,0)
        thirdlayout.addWidget(self.IPWline,4,0)
        thirdlayout.addWidget(self.IDPWbtn,4,1)
        
        fourthlayout=QGridLayout()
        dellabel=QLabel("delete",self)
        self.delcmb=QComboBox(self)
        self.delcmb.addItem('1')
        self.delcmb.addItem('2')
        self.delcmb.addItem('3')
        self.delcmb.addItem('4')
        self.delcmb.addItem('5')
        self.delbtn=QPushButton("삭제",self)
        fourthlayout.addWidget(dellabel,0,0)
        fourthlayout.addWidget(self.delcmb,1,0)
        fourthlayout.addWidget(self.delbtn,1,1)
        
        MainGui.textarea=QTextBrowser(self)
        
        layout=QVBoxLayout()
        layout.addLayout(setboxlayout)
        layout.addLayout(firstlayout)
        layout.addLayout(secondlayout)
        layout.addLayout(thirdlayout)
        layout.addLayout(fourthlayout)
        layout.addWidget(self.textarea)
        
        self.setLayout(layout)
        self.setWindowTitle('macro 설정')
        self.setGeometry(100, 100, 400, 700)
        
def connection() :          #   시리얼 통신을 위한 스레드, 포트와 보드레이트를 입력
    ard=serial.Serial(MyMain.port,MyMain.baudrate)
    if ard.is_open==True :
        MainGui.textarea.append("접속 완료") # 아두이노와 연결된 경우 textarea에 접속 완료 표시

    while True:         
        if MyMain.switch==True :
            MainGui.textarea.append("전송 완료")    # 아두이노에 데이터를 전송한 경우 textarea에 전송 완료 표시
            Trans=MyMain.send
            MainGui.textarea.append(": "+Trans)
            ard.write(Trans.encode())
            read=ard.readline()
            read=read.decode()
            print(read)
            MyMain.switch=False
        if ard.is_open==False :
            MainGui.textarea.append("접속 종료") # 아두이노와 연결해제된 경우 textarea에 접속 종료 표시
        if MyMain.i==1 :        #   종료동작
            sys.exit()
            print(i)
        
class MyMain(MainGui):      # gui 버튼동작 함수를 정리한 class
    def __init__(self):
        super().__init__()
        self.date=None
        self.time=None
        MyMain.switch=False
        MyMain.i=0
        self.setbtn.clicked.connect(self.setbtnClicked)
        self.stopbtn.clicked.connect(self.stopbtnClicked)
        self.ScDLbtn.clicked.connect(self.ScDLbtnClicked)
        self.SchDLbtn.clicked.connect(self.SchDLbtnClicked)
        self.TDLbtn.clicked.connect(self.TDLbtnClicked)
        self.IDPWbtn.clicked.connect(self.IDPWbtnClicked)
        self.SDLbtn.clicked.connect(self.SDLbtnClicked)
        self.delbtn.clicked.connect(self.delbtnClicked)

    def setbtnClicked(self) :           # 통신 시작 버튼 함수
        MyMain.baudrate=self.baudline.text()
        MyMain.port=self.portline.text()
        connect.start()

    def stopbtnClicked(self) :          # 종료 버튼 함수
        MyMain.i=1

    def ScDLbtnClicked(self) :          # 달력 출력 함수
        dlg = Showcalendar()
        dlg.exec_()
        self.date=dlg.datee
        
    def SchDLbtnClicked(self) :         # 시계 출력 함
        dlgg = Showclock()
        dlgg.exec_()
        self.time=dlgg.time
        
    def TDLbtnClicked(self) :           # to do list 데이터 전송 함수, 각각 w/d, 1/2/3, %으로 구분하여 전송
        anum=self.TDLcmb.currentText()
        schedule=self.TDLline.text()
        MyMain.send="w"+"1"+anum+schedule +"\r\n"
        MyMain.switch=True
        
    def IDPWbtnClicked(self) :          # ID/PW 데이터 전송 함수
        bnum=self.IDPWcmb.currentText()
        site=self.IDPWline.text()
        Id=self.IDWline.text()
        pwd=self.IPWline.text()
        MyMain.send="w"+"3"+bnum+site+"%"+Id+"%"+pwd + "\r\n"
        MyMain.switch=True
        
    def SDLbtnClicked(self) :           # schedule 데이터 전송 함수
        cnum=self.SDLcmb.currentText()
        place=self.SDLline.text()
        purpose=self.ScDLline.text()
        who=self.SchDLline.text()            
        MyMain.send="w"+"2"+cnum+self.date+" / "+self.time+"%"+place+"%"+who+"%"+purpose + "\r\n"
        MyMain.switch=True
        
    def delbtnClicked(self) :           # delete 데이터 전송 함수
        dnum=self.delcmb.currentText()
        MyMain.send="d"+dnum + "\r\n"
        MyMain.switch=True
        
if __name__ == '__main__':
    connect=threading.Thread(target=connection)
    connect.daemon=True
    app = QApplication(sys.argv)
    ex = MyMain()
    ex.show()
    sys.exit(app.exec_())
