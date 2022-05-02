# python -m pip install requests

import requests

response = requests.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

# dict response["키값"]
# class response.객체연결 -> 타입을 보고 찾아야한다.
print(response)
print(type(response))
# text : 니가 준 데이터를 문자열 그대로 읽겠다. -> 변수기 때문에 괄호 x
# json : 제이슨 오브젝트를 파이썬 오브젝트로 바꿔주겠다. -> 메서드기 때문에 괄호 존재
print(type(response.json()))
print(type(response.text))
print(response.status_code)

datas = response.json()["response"]["body"]["items"]["item"]

#예쁘게 돌리기 위한 for문
for data in datas:
    print(data["doName"])