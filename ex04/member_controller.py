# C:\Users\arako\AppData\Local\Programs\Python\Python310\Scripts
# python -m pip install flask
# 환경 변수가 설정 안되어 있을 때 (python -m )
# 스프링같은 프레임워크

from flask import Flask, request, jsonify  # 파스칼이니까 클래스
# request : 바디데이터 받기
import member_dao as dao

flask = Flask(__name__)  # 플라스크를 메모리에 띄움


@flask.route("/my-member")
def list():
    return jsonify(dao.select_all())


@flask.route("/my-member/<id>")
def detail(id):
    return jsonify(dao.select_one(id=id))  # **data / 왼쪽이 키, 오른쪽이 변수


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return dao.delete_one(id=id)


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    # data = request.data # x-www-form-urlencoded
    data = request.get_json()  # application/json
    return dao.update_one(id=id, username=data["username"], password=data["password"])


@flask.route("/my-member", methods=['POST'])
def save():
    data = request.get_json()
    return dao.insert_one(username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",  # 모든 ip 접속 가능
    port=5000,
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 리로드 된다.
)
