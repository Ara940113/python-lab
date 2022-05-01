class Post:
    # 생성자 앞에 self를 꼭 넣어줘야한다. (self자리(힙공간)에 자기주소가 바인딩된다.)
    # username은 지역변수
    # 외부에 변수선언이 없다.
    def __init__(self, username, password):  # 생성자 만드는 방법 __init__ : constructor / 키워드다!
        self.username = username
        self.password = password


p = Post("ssar", "1234")

# 클래스를 dict로 바꾸는 방법 = json
print(p.__dict__)
