import json

json_str = '''
{"id":1,"username":"cos","password":"1234"}
'''

#json -> dict
dic1 = json.loads(json_str)
print(dic1)
print(dic1["password"])

#dict -> json
dic_to_json = json.dumps(dic1)
print(dic_to_json)