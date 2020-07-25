# 구글 스프레드 시트 자동 업로드를 위한 코드 
import gspread
import keyboard
import time as delay
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'spreadsheet-267309-2a78d4b64574.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gR5iVoZiSYu9Uh4gQYA5xiDt0QNobOo2nM8kTSHp6l8/edit#gid=0'
# 스프레스시트 문서 가져오기 

global doc
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기

def out():
    global doc
    worksheet = doc.worksheet('시트1')
    range_list = worksheet.range('A1:E2')
    for cell in range_list:
        print(cell.value)
    delay.sleep(1)
#시트 내용 출력

def ins():
    global doc
    worksheet = doc.worksheet('시트1')
    time = datetime.datetime.now()
    t=time.strftime('%Y-%m-%d %H:%M:%S')
    worksheet.update_acell('c2', t)
#시트 내용 수정1
    
def inse():
    global doc
    worksheet = doc.worksheet('시트1')
    global i   
    i+=1
    worksheet.update_acell('e2', i)
    return i
#시트 내용 수정2
    
def running() :
    global i
    i=0
    while True:
        if keyboard.is_pressed('1') :
            out()
        elif keyboard.is_pressed('2') :
            ins()
        elif keyboard.is_pressed('3') :
            inse()            
        elif keyboard.is_pressed('4'):
            break
running()
#실행 함수


    
