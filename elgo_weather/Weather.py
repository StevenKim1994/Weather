
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elgo_weather_layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time
import requests
import sys
import numpy as N
import math
import requests
import pyautogui
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

screen_width, screen_height = pyautogui.size()
from bs4 import BeautifulSoup as bs
from pprint import pprint
html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = bs(html.text, 'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
data2 = data1.findAll('dd')
data3 = soup.find('div',{'class':'info_data'})
data4 = data3.findAll('p')
location = soup.findAll('div')
data5 = soup.find('ul',{'class':'list_area'})
data6 = data5.findAll('li')
data7 = soup.find('li',{'class':'on now merge1'})
Precipitation_probability = data7.find('dd').text
data8 = soup.find('ul',{'class':'info_list'})
rainfall_data = data8.findAll('li');
rainfall = rainfall_data[2].find('span',{'class':'num'}).text
data9 = soup.find('div',{'class':'info_list wind _tabContent'})
windpower = data9.find('dd',{'class':'weather_item _dotWrapper'}).text

print(windpower)
# 지역 정보 
for i in soup.select('span[class=btn_select]'): 
    display_location = i.text

# 날씨 캐스트
display_weathercast = soup.find('p', {'class' : 'cast_txt'}).text

sunny = QImage("./image/sunny.png")
rainy = QImage("./image/rainy.png")
snowing = QImage("./image/snowing.png")
cloudy = QImage("./image/coludy.png")



fine_dust = data2[0].find('span', {'class':'num'}).text
display_find_dust = "미세먼지 : "
display_find_dust += fine_dust

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
display_ultra_find_dust = "초미세먼지 : "
display_ultra_find_dust += ultra_fine_dust

today_temperature = data4[0].find('span',{'class':'todaytemp'}).text
display_today_temperature = "현재 온도 : "
display_today_temperature += today_temperature
display_today_temperature += " °C"

print("현재 이 지역의 날씨")
print(display_today_temperature)
print(display_find_dust)
print(display_ultra_find_dust)
print(display_location)
print(display_weathercast)
#pprint(data6[0])

after1time = data6[1].find('dd',{'class':'item_time'}).text  # 이후 시간/날씨/온도 받아오는 부분
after1weather = data6[1].find('dd',{'class':'item_condition'}).text
after1temperature = data6[1].find('dd',{'class':'weather_item _dotWrapper'}).text


after2time = data6[2].find('dd',{'class':'item_time'}).text
after2weather = data6[2].find('dd',{'class':'item_condition'}).text
after2temperature = data6[2].find('dd',{'class':'weather_item _dotWrapper'}).text


after3time = data6[3].find('dd',{'class':'item_time'}).text
after3weather = data6[3].find('dd',{'class':'item_condition'}).text
after3temperature = data6[3].find('dd',{'class':'weather_item _dotWrapper'}).text

after4time = data6[4].find('dd',{'class':'item_time'}).text
after4weather = data6[4].find('dd',{'class':'item_condition'}).text
after4temperature = data6[4].find('dd',{'class':'weather_item _dotWrapper'}).text

after5time = data6[5].find('dd',{'class':'item_time'}).text
after5weather = data6[5].find('dd',{'class':'item_condition'}).text
after5temperature = data6[5].find('dd',{'class':'weather_item _dotWrapper'}).text




class Ui_Elgo_Weather(object):
    def setupUi(self, Elgo_Weather):
        Elgo_Weather.setObjectName("Elgo_Weather")
        Elgo_Weather.resize(screen_width, screen_height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Elgo_Weather.sizePolicy().hasHeightForWidth())
        Elgo_Weather.setSizePolicy(sizePolicy)
        Elgo_Weather.setMinimumSize(QtCore.QSize(screen_width, screen_height))
        Elgo_Weather.setMaximumSize(QtCore.QSize(screen_width, screen_height))
        Elgo_Weather.setSizeIncrement(QtCore.QSize(0, 0))
        Elgo_Weather.setBaseSize(QtCore.QSize(0, 0))
        self.Location = QtWidgets.QLabel(Elgo_Weather)
        self.Location.setGeometry(QtCore.QRect(120, 60, 811, 111))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Location.setFont(font)
        self.Location.setAlignment(QtCore.Qt.AlignCenter)
        self.Location.setObjectName("Location")
        self.Mainimage = QtWidgets.QLabel(Elgo_Weather)
        self.Mainimage.setGeometry(QtCore.QRect(150, 310, 351, 291))
        self.Mainimage.setAutoFillBackground(False)
        self.Mainimage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mainimage.setObjectName("Mainimage")
        self.MainWeather = QtWidgets.QLabel(Elgo_Weather)
        self.MainWeather.setEnabled(True)
        self.MainWeather.setGeometry(QtCore.QRect(680, 270, 541, 111))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.MainWeather.setFont(font)
        self.MainWeather.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainWeather.setFrameShape(QtWidgets.QFrame.Box)
        self.MainWeather.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWeather.setScaledContents(False)
        self.MainWeather.setObjectName("MainWeather")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Elgo_Weather)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 920, 1641, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ImageTable = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ImageTable.setContentsMargins(0, 0, 0, 0)
        self.ImageTable.setObjectName("ImageTable")
        self.Image2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Image2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Image2.setObjectName("Image2")
        self.ImageTable.addWidget(self.Image2)
        self.Image5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Image5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Image5.setObjectName("Image5")
        self.ImageTable.addWidget(self.Image5)
        self.Image4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Image4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Image4.setObjectName("Image4")
        self.ImageTable.addWidget(self.Image4)
        self.Image3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Image3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Image3.setObjectName("Image3")
        self.ImageTable.addWidget(self.Image3)
        self.Image1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Image1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Image1.setObjectName("Image1")
        self.ImageTable.addWidget(self.Image1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Elgo_Weather)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 1020, 1641, 33))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.TimeTable = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TimeTable.setContentsMargins(0, 0, 0, 0)
        self.TimeTable.setObjectName("TimeTable")
        self.Time2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Time2.setFont(font)
        self.Time2.setObjectName("Time2")
        self.TimeTable.addWidget(self.Time2)
        self.Time1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Time1.setFont(font)
        self.Time1.setObjectName("Time1")
        self.TimeTable.addWidget(self.Time1)
        self.Time3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Time3.setFont(font)
        self.Time3.setObjectName("Time3")
        self.TimeTable.addWidget(self.Time3)
        self.Time4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Time4.setFont(font)
        self.Time4.setObjectName("Time4")
        self.TimeTable.addWidget(self.Time4)
        self.Time5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.Time5.setFont(font)
        self.Time5.setObjectName("Time5")
        self.TimeTable.addWidget(self.Time5)
        self.TemporatureTitle = QtWidgets.QLabel(Elgo_Weather)
        self.TemporatureTitle.setGeometry(QtCore.QRect(720, 400, 81, 41))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.TemporatureTitle.setFont(font)
        self.TemporatureTitle.setObjectName("TemporatureTitle")
        self.label = QtWidgets.QLabel(Elgo_Weather)
        self.label.setGeometry(QtCore.QRect(720, 470, 741, 151))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Elgo_Weather)
        self.label_2.setGeometry(QtCore.QRect(140, 660, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Elgo_Weather)
        self.label_3.setGeometry(QtCore.QRect(410, 660, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Elgo_Weather)
        self.label_4.setGeometry(QtCore.QRect(680, 660, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Elgo_Weather)
        self.label_5.setGeometry(QtCore.QRect(960, 660, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Elgo_Weather)
        self.label_6.setGeometry(QtCore.QRect(140, 740, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Elgo_Weather)
        self.label_7.setGeometry(QtCore.QRect(410, 740, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Elgo_Weather)
        self.label_8.setGeometry(QtCore.QRect(680, 740, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Elgo_Weather)
        self.label_9.setGeometry(QtCore.QRect(960, 740, 201, 51))
        font = QtGui.QFont()
        #font.setFamily("배달의민족 주아")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Elgo_Weather)
        QtCore.QMetaObject.connectSlotsByName(Elgo_Weather)
        palette = QPalette()  #786, 594  1920, 1080, screen_width, screen_height
        background_img = QImage("./image/background_img.jpg").scaled(QSize(screen_width, screen_height))
        palette.setBrush(10, QBrush(background_img))
        Elgo_Weather.setPalette(palette)

    def retranslateUi(self, Elgo_Weather):
        _translate = QtCore.QCoreApplication.translate
        Elgo_Weather.setWindowTitle(_translate("Elgo_Weather", "Dialog"))
     
        
        if after1weather[0] == '맑':
            self.Image2.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            
        elif after1weather[0] == '흐':
            self.Image2.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
            
        elif after1weather[0] == '비':
            self.Image2.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif after1weather[0] == '눈':
            self.Image2.setPixmap(QtGui.QPixmap("./Image/snowing"))
            
        elif after1weather[0] == '구':
             self.Image2.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))




        if after2weather[0] == '맑':
            self.Image5.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            
        elif after2weather[0] == '흐':
            self.Image5.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
            
        elif after2weather[0] == '비':
            self.Image5.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif after2weather[0] == '눈':
            self.Image5.setPixmap(QtGui.QPixmap("./Image/snowing"))

        elif after2weather[0] == '구':
            self.Image5.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))

        if after3weather[0] == '맑':
            self.Image4.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            
        elif after3weather[0] == '흐':
            self.Image4.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
            
        elif after3weather[0] == '비':
            self.Image4.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif after3weather[0] == '눈':
            self.Image4.setPixmap(QtGui.QPixmap("./Image/snowing"))

        elif after3weather[0] == '구':
            self.Image4.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))

        if after4weather[0] == '맑':
            self.Image3.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            
        elif after4weather[0] == '흐':
            self.Image3.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
            
        elif after4weather[0] == '비':
            self.Image3.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif after4weather[0] == '눈':
            self.Image3.setPixmap(QtGui.QPixmap("./Image/snowing"))

        elif after4weather[0] == '구':
            self.Image3.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
         
        if after5weather[0] == '맑':
            self.Image1.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            
        elif after5weather[0] == '흐':
            self.Image1.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
            
        elif after5weather[0] == '비':
            self.Image1.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif after5weather[0] == '눈':
            self.Image1.setPixmap(QtGui.QPixmap("./Image/snowing"))

        elif after5weather[0] == '구':
            self.Image1.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))
        
        
        
        self.Time2.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">" +after1time+"</span></p></body></html>"))
        self.Time1.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">" +after2time+"</span></p></body></html>"))
        self.Time3.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">" +after3time+"</span></p></body></html>"))
        self.Time4.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">"+after4time+"</span></p></body></html>"))
        self.Time5.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">"+after5time+"</span></p></body></html>"))
        self.TemporatureTitle.setText(_translate("Elgo_Weather", "<html><head/><body><p><span style=\" font-size:23pt;\">온도</span></p></body></html>"))
       
        self.label_2.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">강수확률</span></p></body></html>"))
        self.label_3.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">강수량</span></p></body></html>"))
        self.label_4.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">미세먼지 농도</span></p></body></html>"))
        self.label_5.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">풍량</span></p></body></html>"))
        self.label_6.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+Precipitation_probability+"</span></p></body></html>"))
        self.label_7.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+rainfall+"mm"+"</span></p></body></html>"))
        self.label_8.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+fine_dust+"</span></p></body></html>"))
        self.label_9.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+windpower+"</span></p></body></html>"))
        self.Location.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">" + display_location)
        self.MainWeather.setText(display_weathercast)
        self.label.setText(_translate("Elgo_Weather", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">"+display_today_temperature+"</span></p></body></html>"))
        if display_weathercast[0] == '맑':
            self.Mainimage.setPixmap(QtGui.QPixmap("./Image/sunny.png"))
            self.Mainimage.setGeometry(QtCore.QRect(200,200, 422, 423))

        elif display_weathercast[0] == '흐':
            self.Mainimage.setPixmap(QtGui.QPixmap("./Image/cloudy.png"))

        elif display_weathercast[0] == '비':
            self.Mainimage.setPixmap(QtGui.QPixmap("./Image/rainy.png"))

        elif display_weathercast[0] == '눈':
            self.Mainimage.setPixmap(QtGui.QPixmap("./Image/snowing.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Elgo_Weather = QtWidgets.QDialog()
    ui = Ui_Elgo_Weather()
    ui.setupUi(Elgo_Weather)
    Elgo_Weather.show()
    Elgo_Weather.showMaximized()
    Elgo_Weather.showFullScreen()
    Elgo_Weather.setFixedSize(screen_width,screen_height)
    sys.exit(app.exec_())
