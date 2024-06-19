# import requests
# from datetime import datetime
# import json

# # def get_current_date_string():
# #     current_date = datetime.now().date()
# #     return current_date.strftime("%Y%m%d")

# # def get_current_hour_string():
# #     now = datetime.now()
# #     if now.minute<45: # base_time와 base_date 구하는 함수
# #         if now.hour==0:
# #             base_time = "2330"
# #         else:
# #             pre_hour = now.hour-1
# #             if pre_hour<10:
# #                 base_time = "0" + str(pre_hour) + "30"
# #             else:
# #                 base_time = str(pre_hour) + "30"
# #     else:
# #         if now.hour < 10:
# #             base_time = "0" + str(now.hour) + "30"
# #         else:
# #             base_time = str(now.hour) + "30"

# #     return base_time

# # url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
# # params = {
# #     'serviceKey' : 'Ie+TCOGAXvNGev9YJ3bRSBI30HvVJKt9GxtIdoObn4wXutBWB0rW/11KoHiHWOfb1an17vdByseR49EK9XBQvA==',
# #     'pageNo' : '1',
# #     'numOfRows' : '10',
# #     'dataType' : 'JSON',
# #     'stnId' : '109',
# #     # 'tmFc' : get_current_date_string() + '0600'
# #     'tmFc' : '20240619' + '0600'
# #     }


# # def forecast():

# #     response = requests.get(url, params=params)

# #     xml_data = response.content
# #     response_str = xml_data.decode('utf-8')

# #     result = json.loads(response_str)
# #     # print("parse_json result: %s" % type(result))
# #     print(result)

# #     #값 가져오기
# #     weather_data = dict()
# #     for item in result['response']['body']['items']['item']:
# #         # wfSv 키의 값을 가져와서 \n을 기준으로 분할
# #         forecast = item['wfSv'].split('\n')

# #         # 각 문장을 출력
# #         for line in forecast:
# #             print(line.strip())
# #         # # 기온
# #         # if item['category'] == 'T1H':
# #         #     weather_data['tmp'] = item['fcstValue']
# #         # # 습도
# #         # if item['category'] == 'REH':
# #         #     weather_data['hum'] = item['fcstValue']
# #         # # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
# #         # if item['category'] == 'SKY':
# #         #     weather_data['sky'] = item['fcstValue']
# #         # # 강수형태: 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
# #         # if item['category'] == 'PTY':
# #         #     weather_data['sky2'] = item['fcstValue']

# #     return weather_data


# # def proc_weather():
# #     dict_sky = forecast()

# #     # str_sky = "서울 "
# #     # if dict_sky['sky'] != None or dict_sky['sky2'] != None:
# #     #     str_sky = str_sky + "날씨 : "
# #     #     if dict_sky['sky2'] == '0':
# #     #         if dict_sky['sky'] == '1':
# #     #             str_sky = str_sky + "맑음"
# #     #         elif dict_sky['sky'] == '3':
# #     #             str_sky = str_sky + "구름많음"
# #     #         elif dict_sky['sky'] == '4':
# #     #             str_sky = str_sky + "흐림"
# #     #     elif dict_sky['sky2'] == '1':
# #     #         str_sky = str_sky + "비"
# #     #     elif dict_sky['sky2'] == '2':
# #     #         str_sky = str_sky + "비와 눈"
# #     #     elif dict_sky['sky2'] == '3':
# #     #         str_sky = str_sky + "눈"
# #     #     elif dict_sky['sky2'] == '5':
# #     #         str_sky = str_sky + "빗방울이 떨어짐"
# #     #     elif dict_sky['sky2'] == '6':
# #     #         str_sky = str_sky + "빗방울과 눈이 날림"
# #     #     elif dict_sky['sky2'] == '7':
# #     #         str_sky = str_sky + "눈이 날림"
# #     #     str_sky = str_sky + "\n"
# #     # if dict_sky['tmp'] != None:
# #     #     str_sky = str_sky + "온도 : " + dict_sky['tmp'] + 'ºC \n'
# #     # if dict_sky['hum'] != None:
# #     #     str_sky = str_sky + "습도 : " + dict_sky['hum'] + '%'

# #     # return str_sky
    
# # print(proc_weather())


# # url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# # params ={'serviceKey' : 'Ie+TCOGAXvNGev9YJ3bRSBI30HvVJKt9GxtIdoObn4wXutBWB0rW/11KoHiHWOfb1an17vdByseR49EK9XBQvA==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20240620', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }



# # import requests

# url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# params ={'serviceKey' : 'Ie+TCOGAXvNGev9YJ3bRSBI30HvVJKt9GxtIdoObn4wXutBWB0rW/11KoHiHWOfb1an17vdByseR49EK9XBQvA==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20240619', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

# response = requests.get(url, params=params)
# print(response.content)

# # response = requests.get(url, params=params)
# # xml_data = response.content
# # response_str = xml_data.decode('utf-8')

# # # result = json.loads(response_str)
# # # print("parse_json result: %s" % type(result))
# # # print(result)
# # print(response_str)



import requests

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
params ={'serviceKey' : 'Ie+TCOGAXvNGev9YJ3bRSBI30HvVJKt9GxtIdoObn4wXutBWB0rW/11KoHiHWOfb1an17vdByseR49EK9XBQvA==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'stnId' : '108', 'tmFc' : '202406180600' }

response = requests.get(url, params=params)
print(response.content)