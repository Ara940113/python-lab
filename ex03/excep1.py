# 예외를 잡기위한 try-catch
# 컴파일시에는 에러가 없고 런타임시에만 에러가 있다.


try:
    f = open("c:/hello/txt", "r")
    print(2/0)
except Exception as e:
    print(e)
finally:  # 터져도 실행되고 안터져도 실행됨
    print("무조건 실행됨")
