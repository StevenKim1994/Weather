import sys
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = bs(html.text, 'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
data2 = data1.findAll('dd')
data3 = soup.find('div',{'class':'info_data'})
data4 = data3.findAll('p')
#pprint(data2)


fine_dust = data2[0].find('span', {'class':'num'}).text
display_find_dust = "미세먼지 : "
display_find_dust += fine_dust

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
display_ultra_find_dust = "초미세먼지 : "
display_ultra_find_dust += ultra_fine_dust

today_temperature = data4[0].find('span',{'class':'todaytemp'}).text
display_today_temperature = "현재 온도 : 섭씨 "
display_today_temperature += today_temperature
display_today_temperature += " 도"

print("현재 이 지역의 날씨")
print(display_today_temperature)
print(display_find_dust)
print(display_ultra_find_dust)

