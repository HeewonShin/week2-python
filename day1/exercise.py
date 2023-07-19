
# love 출력
str = "Dog is love"
print(str[7:])


# Dog -> Cat
print(str.replace("Dog", "Cat"))

# 문자열 길이 구하고 a의 갯수 출력
str2 = "lalalalalalalalalala"
print(len(str2))
print(str2.count("a"))

#  - 제거하여 출력
str3 = "010-1234-5678"
print(str3.replace("-", ""))

# 두 변수를 이용하여 출력
a = "hello"
b = " python"
print(a+"! "+b)

# green 삭제
color = ['red', 'pink', 'orange', 'yellow','green', 'purple', 'black', 'white']
color.remove('green')
print(color)

# red 다음에 pink 추가
color2 = ['red', 'orange', 'green', 'blue', 'black', 'white']
color2.insert(1, 'pink')
print(color2)

