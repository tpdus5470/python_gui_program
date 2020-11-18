import requests
import urllib

# url 위치의 경도, 위도 값을 출력하는 코드

start_location_c = '수원시'
depart_location_c = '성남시'
start_lo_c = urllib.parse.quote(start_location_c)
depart_lo_c = urllib.parse.quote(depart_location_c)
start_location_g = '영통구'
depart_location_g = '수정구'
start_lo_g = urllib.parse.quote(start_location_g)
depart_lo_g = urllib.parse.quote(depart_location_g)
start_location_d = '영통동'
depart_location_d = '복정동'
start_lo_d = urllib.parse.quote(start_location_d)
depart_lo_d = urllib.parse.quote(depart_location_d)
start_location_da = '영통역'
depart_location_da = '가천대학교'
start_lo_da = urllib.parse.quote(start_location_da)
depart_lo_da = urllib.parse.quote(depart_location_da)

URL_a= 'https://apis.openapi.sk.com/tmap/geo/geocoding?version=1&city_do='+ str(start_lo_c) \
+ '&gu_gun=' + str(start_lo_g)+'&dong='+ str(start_lo_d)+'&detailAddress='+ str(start_lo_da) \
+ '&coordType=WGS84GEO&appKey=l7xx4b80ff43a39140cca93263e35145e4e0'
    
URL_b= 'https://apis.openapi.sk.com/tmap/geo/geocoding?version=1&city_do='+ str(depart_lo_c) \
+ '&gu_gun='+ str(depart_lo_g)+'&dong='+ str(depart_lo_d)+'&detailAddress='+ str(depart_lo_da) \
+ '&coordType=WGS84GEO&appKey=l7xx4b80ff43a39140cca93263e35145e4e0'

response_a = requests.get(URL_a)
data_a = response_a.json()
lat_a = data_a['coordinateInfo']['lat']
lon_a = data_a['coordinateInfo']['lon']

response_b = requests.get(URL_b)
data_b = response_b.json()
lat_b = data_b['coordinateInfo']['lat']
lon_b = data_b['coordinateInfo']['lon']

print(lat_a)
print(lon_a)

print(lat_b)
print(lon_b)
