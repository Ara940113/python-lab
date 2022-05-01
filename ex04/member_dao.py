# dao : Data Access Object
# 중간 다리 역할 -findAll, findById, save를 가지고있다.(재사용)

from logging import exception
from db import connect as db

# insert_one(username="ssar", password="1234")


def insert_one(**data):  # {"username":"ssar", "password":"1234"}
    sql = "INSERT INTO my_member(username, password) VALUES(%(username)s, %(password)s)"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def select_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()  # list 안에 dict 들어가있음
    return rows

# 셀렉트를 영속화 - 영속화 되면 계속 변경감지 확인 - 변경 안되니까 걱정마
# 변경감지를 안하기 위해 : 트랜잭셔널 리드온리 트루
# 아이솔레이션 영속성 전파


def select_one(**data):
    sql = "SELECT * FROM my_member WHERE id = %(id)s"
    db.cursor.execute(sql, data)
    row = db.cursor.fetchone()  # list 안에 dict 들어가있음
    return row


def update_one(**data):
    sql = "UPDATE my_member SET username=%(username)s,password=%(password)s WHERE id = %(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def delete_one(**data):
    sql = "DELETE FROM my_member WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        print(e)
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1
