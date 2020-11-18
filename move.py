import pyautogui
import serial
currentMouseX, currentMouseY= pyautogui.position()
port = 'COM3'
baud = 9600
ard = serial.Serial(port, baud)

def start_btn_click():
        while True:
                if ard.readable():
                        res = ard.readline()               
                        resd = res.decode()
                        r=resd[:1]
                        print(r)
                        if r == "1" :
                                pyautogui.scroll(1000,x=500, y=500)
                        elif r == "2" :
                                pyautogui.scroll(-1000,x=500, y=500)
                        elif r == "3" :
                                pyautogui.click(x=300, y=300, button='right')
                        else :
                                break
start_btn_click()

#pyautogui모듈 테스트, 블루투스와 연결뒤 입력되는 값에따라 마우스커서가 이동
