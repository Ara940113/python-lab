# 함수 (클래스 내부에 있는 것이 아닌 것들을 함수 ) - 독단적으로 input이 들어왔을 때 output을 항상 똑같이 내보낸다.
# 함수형 프로그램 : 상태를 멀리한다 / 클래스 내부에 없기 때문에 1급객체  /상태를 메서드로 변경안시킨다
# 메서드는 상태를 변화시킨다.

def add():
    print("더하기")  # 리턴없음


def minus():
    return 1


add()
n = minus()

print(n)

# 파이썬은 오버로딩이 없다.


def multi(n1, n2=3):  # 디폴트 값이 있으면 뒤로간다
    print(f"곱하기 {n1}*{n2}")


multi(3, 2)

multi(2)

# 여러가지 인수를 하나로 합쳐주는 문법


def my_dict(**data):  # dict 변환 문법
    print(data)  # 실행시에 뜨기때문에 스택
    pass  # 아무것도 안 넣고 싶으면 pass를 적으면 된다


my_dict(id=1, username="ssar")

n1 = 1  # 1급객체 (어디 클래스에 소속된게 아니다) , 힙에 뜬다


def vartest():
    global n1  # n1을 정의해줘야 아래에서 쓰인다
    n1 = 2  # 선언을 한건지, 재사용한건지 알수 없다 => 지역변수


vartest()
print(n1)
