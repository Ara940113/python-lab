import requests

list = []

aid = 1
error = 0
while True:
    try:
        format_aid = '{0:010d}'.format(aid)
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{format_aid}?sid=100")
        aid += 1
        print(html.status_code)
        if(html.status_code == 200):
            error = 0
            list.append(html.text)
        else:
            error += 1
    except Exception as e:
        pass
    if error == 30:
        break

print(len(list))


