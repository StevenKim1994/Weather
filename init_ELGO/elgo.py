import sys
import numpy as N
import math

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time

import pyautogui
screen_width, screen_height = pyautogui.size()
#screen_width = 1920
#screen_height = 1080

import requests
from bs4 import BeautifulSoup

import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.yna.co.kr/economy/all'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
result = soup.select('strong.news-tl > a')
crawler = list()

for cnt in range(0,20):
    crawler.append(result[cnt].text)
    print(crawler[cnt])

# 리눅스기반 특수문자 처리용
for res in range(0,20):
    while("&apos;" in crawler[res]):
        crawler[res] = crawler[res].replace("&apos;", "'")

cnt = 0

now_value = math.sqrt(pow(786, 2) + pow(594, 2))
change_value = math.sqrt(pow(screen_width, 2) + pow(screen_height, 2))
resize_value = change_value / now_value
resize_py = int(25 * resize_value)

print(resize_value)

label_1_size = int(25 * (resize_value))
label_1_font = QFont("Bahnschrift SemiBold", label_1_size)
font_size = int(16 * (resize_value))
use_font = QFont("Bahnschrift SemiLight", font_size)
print("font_size: ",font_size)
# marquee 길이확인을 위한 변수
# screen_width 786 , font_size 16 -> screen_width 786, font_size 27 인데 label_size 가 같은 값이면 marquee 길이에 문제발생
label_size = 400 *((screen_width/786)/resize_value)
if(label_size > 400): label_size = 400
print("label_size : ", label_size)

# marquee class
class MarqueeLabel(QLabel):
    def __init__(self, parent=None):
        global cnt
        global label_size
        QLabel.__init__(self, parent)

        self.move = 1
        self.px = 1
        self.py = int(25*(screen_height/594))
        self._direction = Qt.RightToLeft
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(40)
        self._speed = 1
        self.lastx = self.fontMetrics().width(self.text())

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.lastx > label_size:
            self.px -= self.speed()
            self.lastx -= 0.22
        else:
            if self.px > 0:
                self.px -= self.speed()
            else:
                self.move = 0

        painter.drawText(self.px, self.py, self.text())

    def speed(self):
        return self._speed

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
       global resize_py
       # MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
       MainWindow.resize(screen_width, screen_height)

       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")

       _label_ = QtWidgets.QLabel()
       _label_2 = QtWidgets.QLabel()
       _label_3 = QtWidgets.QLabel()
       _label_4 = QtWidgets.QLabel()
       _label_5 = QtWidgets.QLabel()

       self.label = QtWidgets.QLabel(self.centralwidget)
       self.label.setGeometry(QtCore.QRect(50,20,510,60))
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(self.centralwidget)
       self.label_2.setGeometry(QtCore.QRect(130,160,570,50))
       self.label_2.setObjectName("label_2")
       self.label_3 = QtWidgets.QLabel(self.centralwidget)
       self.label_3.setGeometry(QtCore.QRect(130,250,570,50))
       self.label_3.setObjectName("label_3")
       self.label_4 = QtWidgets.QLabel(self.centralwidget)
       self.label_4.setGeometry(QtCore.QRect(130,340,570,50))
       self.label_4.setObjectName("label_4")
       self.label_5 = QtWidgets.QLabel(self.centralwidget)
       self.label_5.setGeometry(QtCore.QRect(130,430,570,50))
       self.label_5.setObjectName("label_5")
       self.label_6 = QtWidgets.QLabel(self.centralwidget)
       self.label_6.setGeometry(QtCore.QRect(130,520,570,50))
       self.label_6.setObjectName("label_6")
       MainWindow.setCentralWidget(self.centralwidget)
       


       self.label.setText("    이번주 HOT")

       ## 객체 위치 조정
       width_resize = screen_width/786
       height_resize = screen_height/594

       width1 = int(50*width_resize)
       width2 = int(510*width_resize)
       height1 = int(35*height_resize)
       height2 = int(45*height_resize)
       self.label.setGeometry(QtCore.QRect(width1, height1, width2, height2))

       width1 = int(130*width_resize)
       width2 = int(570*width_resize)

       height1 = int(160*height_resize)
       height2 = int(50*height_resize)
       self.label_2.setGeometry(QtCore.QRect(width1, height1, width2, height2))
       print(width1, height1, width2, height2)
       height1 = int(250*height_resize)
       height2 = int(50*height_resize)
       self.label_3.setGeometry(QtCore.QRect(width1, height1, width2, height2))

       height1 = int(340*height_resize)
       height2 = int(50*height_resize)
       self.label_4.setGeometry(QtCore.QRect(width1, height1, width2, height2))

       height1 = int(430*height_resize)
       height2 = int(50*height_resize)
       self.label_5.setGeometry(QtCore.QRect(width1, height1, width2, height2))

       height1 = int(520*height_resize)
       height2 = int(50*height_resize)
       self.label_6.setGeometry(QtCore.QRect(width1, height1, width2, height2))
       ## 객체 위치 조정

       #label_size 를 재계산 해줘야함
       #width 의 증가비율과 resize_value 값을 비교


       # crawling 을 갱신하기 위한 타이머 (1시간단위)
       self.timer_crawler = QTimer(MainWindow)
       self.timer_crawler.start(1000*60*60)
       self.timer_crawler.timeout.connect(self.timeout_crawler)

       # marquee class 가져오기
       self.label_2 = MarqueeLabel(self.label_2)
       self.label_3 = MarqueeLabel(self.label_3) 
       self.label_4 = MarqueeLabel(self.label_4)
       self.label_5 = MarqueeLabel(self.label_5)
       self.label_6 = MarqueeLabel(self.label_6)

       #window 기준
       #한글 -> 15
       #알파벳 소문자 -> 8
       #알파벳 대문자 -> 9
       #공백 -> 5
       #현재 공백칸 405

       #linux 기준
       #한글 -> 13~14
       #공백(탭) -> 11
       #공백 -> 3~4
       self.label_2.setText("           ")
       self.label_3.setText("           ")
       self.label_4.setText("           ")
       self.label_5.setText("           ")
       self.label_6.setText("           ")

       global resize_py

       marqueeLen = 400+resize_py*2
       while(self.label_2.fontMetrics().width(self.label_2.text())<marqueeLen):
           self.label_2.setText(self.label_2.text()+"   ")
       while(self.label_2.fontMetrics().width(self.label_2.text())<marqueeLen):
           self.label_2.setText(self.label_2.text()+" ")
       while(self.label_3.fontMetrics().width(self.label_3.text())<marqueeLen):
           self.label_3.setText(self.label_3.text()+"   ")
       while(self.label_3.fontMetrics().width(self.label_3.text())<marqueeLen):
           self.label_3.setText(self.label_3.text()+" ")
       while(self.label_4.fontMetrics().width(self.label_4.text())<marqueeLen):
           self.label_4.setText(self.label_4.text()+"   ")
       while(self.label_4.fontMetrics().width(self.label_4.text())<marqueeLen):
           self.label_4.setText(self.label_4.text()+" ")
       while(self.label_5.fontMetrics().width(self.label_5.text())<marqueeLen):
           self.label_5.setText(self.label_5.text()+"   ")
       while(self.label_5.fontMetrics().width(self.label_5.text())<marqueeLen):
           self.label_5.setText(self.label_5.text()+" ")
       while(self.label_6.fontMetrics().width(self.label_6.text())<marqueeLen):
           self.label_6.setText(self.label_6.text()+"   ")
       while(self.label_6.fontMetrics().width(self.label_6.text())<marqueeLen):
           self.label_6.setText(self.label_6.text()+" ")

       # 이미지설정
       palette = QPalette()  #786, 594  1920, 1080, screen_width, screen_height
       background_img = QImage("./image/background_img.png").scaled(QSize(screen_width, screen_height))
       palette.setBrush(10, QBrush(background_img))
       MainWindow.setPalette(palette)

       # font
       # 라벨 티몬소리블랙
       # 내용 배달의민족 도현체
       global use_font
       global label_1_font

       self.label.setFont(label_1_font)
       self.label.setStyleSheet('color:blue;')
       self.label_2.setFont(use_font)
       self.label_3.setFont(use_font)
       self.label_4.setFont(use_font)
       self.label_5.setFont(use_font)
       self.label_6.setFont(use_font)

       # marquee 이 종료됨을 확인하고 crawling 을 갱신하는 작업을 위한 타이머(0.5초마다확인)
       self.check_finish = QTimer(MainWindow)
       self.check_finish.start(500)
       self.check_finish.timeout.connect(self.check_move)


    def check_move(self):
           if self.label_2.move == 0 :
               if self.label_3.move == 0 :
                   if self.label_4.move == 0 :
                       if self.label_5.move == 0 :
                           if self.label_6.move == 0 :
                               time.sleep(2)
                               self.change_text()

    def change_text(self):
           # globar => 전역변수를 지역범위에서 사용하기위해
           global cnt
           global resize_py
           self.label_2.setText(crawler[cnt])
           self.label_3.setText(crawler[cnt+1])
           self.label_4.setText(crawler[cnt+2])
           self.label_5.setText(crawler[cnt+3])
           self.label_6.setText(crawler[cnt+4])

           print(crawler[cnt])
           print(MainWindow.fontMetrics().width(crawler[cnt]))
           print(crawler[cnt+1])
           print(MainWindow.fontMetrics().width(crawler[cnt+1]))
           print(crawler[cnt+2])
           print(MainWindow.fontMetrics().width(crawler[cnt+2]))
           print(crawler[cnt+3])
           print(MainWindow.fontMetrics().width(crawler[cnt+3]))
           print(crawler[cnt+4])
           print(MainWindow.fontMetrics().width(crawler[cnt+4]))

           ㄹㅇself.label_2.px = 1; self.label_2.lastx = MainWindow.fontMetrics().width(crawler[cnt]); self.label_2.move = 1
           self.label_3.px = 1; self.label_3.lastx = MainWindow.fontMetrics().width(crawler[cnt+1]); self.label_3.move = 1
           self.label_4.px = 1; self.label_4.lastx = MainWindow.fontMetrics().width(crawler[cnt+2]); self.label_4.move = 1
           self.label_5.px = 1; self.label_5.lastx = MainWindow.fontMetrics().width(crawler[cnt+3]); self.label_5.move = 1
           self.label_6.px = 1; self.label_6.lastx = MainWindow.fontMetrics().width(crawler[cnt+4]); self.label_6.move = 1
           self.label_2.py = resize_py; self.label_3.py = resize_py; self.label_4.py = resize_py
           self.label_5.py = resize_py; self.label_6.py = resize_py


           cnt = cnt+5
           if cnt>=20: cnt = 0

    def timeout_crawler(self):
           self.timer_crawler.stop()
           self.check_finish.stop()
           # 1시간단위 크롤러
           req = requests.get(url)
           html = req.text
           soup = BeautifulSoup(html, 'html.parser')
           result = soup.select('strong.news-tl > a')

           for cnt in range(0,20):
               crawler.append(result[cnt])
               print(crawler[cnt])

           for res in range(0,20):
               while("'" in crawler[res]):
                   crawler[res] = crawler[res].replace("'", 'a')

           self.timer_crawler.start(1000*60*60)
           self.check_finish.start(500)

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   # MainWindow.show()
   MainWindow.showFullScreen()
   sys.exit(app.exec_())
