import requests
# import time


city_name = "Seoul"
# lat = "37.5665"  # 서울의 위도
# lon = "126.9780" # 서울의 경도

# 2023년 6월 15일 12:00의 UNIX 타임스탬프
# dt = int(time.mktime(time.strptime('2023-06-15 12:00:00', '%Y-%m-%d %H:%M:%S')))

# print(dt)
# API 키
api_key = '243a864f8a027704f94f8c945a071854'

# 요청 URL
api_url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&q={city_name}&appid={api_key}&lang=kr&units=metric"
# api_url = f"https://api.openweathermap.org/data/2.5/forecast?lat=37.56826&lon=126.977829&appid={api_key}&lang=kr&units=metric"
# api_url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}&lang=kr&units=metric'

# 요청 보내기
response = requests.get(api_url)
data = response.json()

print(data)

print(data['list'][0]['main']['temp_min'])
print(data['list'][0]['main']['temp_max'])
print(data['list'][1]['main']['temp_min'])
print(data['list'][1]['main']['temp_max'])