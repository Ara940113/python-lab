# if 만약에

money = 1000

# 내부 구분을 들여쓰기로 한다
if money == 1000:
    print("돈 1000원 있어요")
else:
    print("없어")

point = "A"

if point == "A":
    print("A학점입니다")
elif point == "D":
    print("D학점입니다")

# in 문법
list = [1, 2, 3]

# 1이 리스트 안에 있니? -> 부울로 응답
print(5 in list)

if 1 in list:
    print("1이 존재합니다")
