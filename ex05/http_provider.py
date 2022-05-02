import requests as api

def get(url):
    response = api.get(url)
    if response.status_code == 200: #200이면 파싱 시작
        #공공데이터에서만 사용할 수 있는 무적의 코드
        datas = response.json()["response"]["body"]["items"]["item"]
        return datas
    
        