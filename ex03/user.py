# 자바에서는 상태와 행위를 가진 클래스가 필요할때, 데이터 자료형 쓸때 클래스를 만든다
# 파이썬은 무조건 클래스를 만들어야 할 필요가 없다
# 그럼 클래스를 언제써야할까?
# 찍어내야 할 때 (설계도를 기반으로)-> 추상적인 설계도를 만들어놓고 new해서 찍어내야할때
# -> 어떤거를 찍어내야하지??

class User:  # 클래스는 new할때만 뜬다. 클래스가 있네 하고 넘어가지 메모리에 띄우지 않는다
    username = "ssar"
    password = "1234"
