import requests
from datetime import datetime, timedelta

# 현재 날짜와 시간 가져오기
now = datetime.now()
three_days_later = now + timedelta(days=3)
date_time = three_days_later.strftime("%Y-%m-%d")
print(date_time)


api_key = "243a864f8a027704f94f8c945a071854"
# city_name = "Seoul"
lat = "37.5665"  # 서울의 위도
lon = "126.9780" # 서울의 경도
api_url = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + lat + "&lon=" + lon + "&dt=" + date_time + "&lang=kr&APPID=" + api_key + "&units=metric"
# api_url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date_time}&appid={api_key}&lang=kr"
# api_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "dt=" + date_time + "&lang=kr&APPID=" + api_key + "&units=metric"
# api_url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=39.099724&lon=-94.578331&dt=1643803200&appid={api_key}"
response = requests.get(api_url)
data = response.json()

print(data)