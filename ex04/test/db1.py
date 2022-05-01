# python -m pip install pymysql

from db import connect as db

insert_sql = "INSERT INTO my_member(username,password) VALUES(%s,%s)"
db.cursor.execute(insert_sql, ["love", "1234"])  # 버퍼로 쏜다.
db.conn.commit()
