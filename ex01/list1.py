# 리스트 , 슬라이싱
print('='*60)


# 리스트 만들기
list1 = [1,2,3,4]
list2 = ['1',2,'3',4]

print(list1[0])

# 리스트 추가하기
list1.append(5)
print(list1)

# 리스트 요소제거
del list1[0]
print("0번지 제거",list1)

# 리스트 정렬
list3=[3,1,2]
list3.sort()
print(list3)
list3.reverse()
print(list3)

# 리스트 값의 위치 찾기
print(list3.index(3))

# 문자열 슬라이싱
str1 = '안녕하세요'
print(str1[0])
print(str1[1:2]) #시작위치, 끝위치
print(str1[-1]) # 끝 인덱스를 찾는다
print(str1[1:])