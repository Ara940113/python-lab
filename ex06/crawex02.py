# 크롤링

# python -m pip install beautifulsoup4

import requests

list = []
aid =["0000000001","0000000002","1000000003"] 

for a in aid:
    try:
        html = requests.get(
         f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
         # print(html.status_code)
        if(html.status_code == 200):
          list.append(html.text)
    except Exception as e:
        pass

#aid=1 로 만들기
print(len(list))
print(list[0])

# 정치(100)/국민일보(005)/0000000001 ~ 끝까지 파이썬으로 크롤링해서 arrayList에
#담고 size를 출력하는 프로그램을 만들면되요.


