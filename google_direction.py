import time
import json
import os
import ssl
import urllib.request
import requests

# 구글 direction api를 이용하여 경로를 검색하는 예제
if (__name__ == "__main__") :

    st_location = '경희대학교'
    de_location = '가천대학교'
    URL_a= 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDGzKvPSmSni92L2x0dAUeRZlgHu0DntHc' \
    '&sensor=false&language=ko&address={}'.format(st_location)
    # 출발지, 도착지의 경도, 위도, url등의 값이 필요함 (형식은 공식 사이트 참조)
    response_a = requests.get(URL_a)
    data_a = response_a.json()
    lat_a = data_a['results'][0]['geometry']['location']['lat']
    lng_a = data_a['results'][0]['geometry']['location']['lng']

    URL_b= 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDGzKvPSmSni92L2x0dAUeRZlgHu0DntHc' \
    '&sensor=false&language=ko&address={}'.format(de_location)

    response_b = requests.get(URL_b)
    data_b = response_b.json()
    lat_b = data_b['results'][0]['geometry']['location']['lat']
    lng_b = data_b['results'][0]['geometry']['location']['lng']

    # 경로 출력 설정 값
    origin          = str(lat_a)+","+str(lng_a)
    destination     = str(lat_b)+","+str(lng_b)
    mode            = "driving"
    departure_time  = "now"
    key             = "" #Google Cloud Platform의 key값

    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+ origin \
            + "&destination=" + destination \
            + "&mode=" + mode \
            + "&departure_time=" + departure_time\
            + "&language=ko" \
            + "&key=" + key

    request         = urllib.request.Request(url)
    context         = ssl._create_unverified_context()
    response        = urllib.request.urlopen(request, context=context)
    responseText    = response.read().decode('utf-8')
    # 한글로 디코드
    responseJson    = json.loads(responseText)

    with open("./Agent_Transit_Directions.json","w") as rltStream :
        json.dump(responseJson,rltStream)


if ( __name__ == "__main__" ) : # 실행하면 필요값만 출력하도록 설정

    wholeDict = None
    with open("./Agent_Transit_Directions.json","r") as transitJson :
        wholeDict = dict(json.load(transitJson))

    path            = wholeDict["routes"][0]["legs"][0]
    duration_sec    = path["duration"]["value"]
    start_geo       = path["start_location"]
    end_geo         = path["end_location"]

    print(duration_sec) 
    print(start_geo)	
    print(end_geo)	

    stepList = path["steps"]
    print(stepList[0])
