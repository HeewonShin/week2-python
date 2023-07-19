print('hello')

# 리스트 == 배열
# 튜플
# True False
# 단어 사이는 _ 사용, 소문자만 사용


# print(1 + 3)
# print('Hello World')
# print(4 - 3)
# print(11 / 3)
# print(11 // 3) #몫
# print(5 * 2)

# a = 500
# a += 50
# a -= 20
# a *= 2 # a=a*2

# print(abs(-5.3)) #절대값
# print(pow(3, 2)) #3의 2승
# print('*' * 100)
# happy_face = '😊'
# print(happy_face)

# a = '3' # string
# b = 5 # int(정수)
# print(a + b) # concatenate err

# print(type(a))
# print(type(b))
# print(type(3.5)) # float
# print(type(True))

# a = '256'
# print(int(a))
# print(float(a), type(float(a)))

# print('hello', 'world')

# number_list = [1, 2, 3, 4, 5]
# names = ['Lukas', 'David', 'George', 'Lee']

# random_list = [3, 6, 9, "Python", False, True, [1, 2, 3]]
# random_list = [1, 2, 3, 4, 5]

# print(random_list)
# for element in random_list:
#     print(type(element))

#Tuple#
# 한 번 만들어진 튜플은 값의 재할당이 불가능하다
# my_tuple = (1, 2, 3.5, 'Hello', False)
# my_tuple[2] = 50 #'tuple' object does not support item assignment
# print(my_tuple[2])

# a = 'Hello World 😊' #13글자
# b = 'ESG'
# my_list = [1, 2, True]

# # length를 구하는 len 함수
# print(a[12])
# print(len(b))
# print(len(my_list))
# print(a[0:13]) # 첫번째 값은 포함이고 두번째 값 12는 포함이 아니다
# print(a[0:0]) #출력 안됨
# print(a[0:3])# 0~2까지 출력
# print(a[6:9]) #시작 인덱스, 출력할 글자수
# print(a[6: ]) # 인덱스6부터 끝까지
# print(a[:9]) # 처음부터 9개
# print(a[:]) # 처음부터 끝까지

# my_list = [1, 2, 3.5, 'Hello', [1, 2, 3, 4, 5], True, False]
# print(my_list[3:6])

# class_name = 'ChatGPT API'
# print(class_name[4:])
# print(class_name.count('A')) # A의 갯수 

# find_str = "python!"
# print(find_str.find("!")) # 찾으려고 하는 문자의 index를 알려준다

# print(".".join(find_str)) # string클래스에 들어있는 join내장함수,,p.y.t.h.o.n.!


# title = "  PyThON ClASs   "
# print(title.lower())
# print(title.upper())
# print(title.strip()) # 양쪽 공백 제거
# print(title.strip().lower().upper()) # 각 함수 순서대로 실행

# quote = "Life is too short"
# print(quote.replace("too", "very")) #바꿀 문자열, 대체 문자열,, quote 값 자체가 바뀌는건 아님
# print(quote.replace(" ", ""))

# print(quote.split()) # 아무 것도 안 넣으면 " "가 들어간다고 생각하면 됨

# quote2 = "Learn Python"
# print(quote2.split())
# print(quote2.split('P')) # P를 기준으로 나눠져서 list에 담긴다
# print(quote2.split('arn'))

# example = 'a:B:c:d'
# print(example.split()) # 공백이 없어서 안 나눠짐

# a = [1, 2, 3]
# a[2] = 4

# del a[2] # a[2]의 값 삭제

# a= [ 0, 2, 3, 4, 5, 6, 7, 8]
# del a[1:6]

# a = [0, 1, 2, 3]
# a.append(4) # append는 list에 종속된 함수이다
# # 참고로 append(["a", "b", "c", "d"])로 배열을 추가하면 새로운 배열이 하나의 요소로 추가됨

# a.extend(["a", "b", "c", "d"]) # [0, 1, 2, 3, 4, 'a', 'b', 'c', 'd']
# print(a)



# a = [9, 3, 6, 1, 2, 33, 12]
# a.sort() # a의 값을 순서대로 정렬,, a의 값이 바뀜
# print(sorted(a)) # a값은 안 바뀜,, sorted는 list에 종속된 함수이다

# a.reverse() #순서 바뀜,, a의 값 바뀜

# a = ["a", "b", "c", "A", "B" ]
# a.insert(2, "0") # 추가될 인덱스 위치, 추가할 값

# print(a)

# a = [1, 2, 3, 1, 2, 3]
# a.remove(3) # 3을 찾아서 제거, 중복이 있으면 제일 앞쪽 제거

# a.pop() # 제일 마지막 요소 제거,, a.pop(제거할 인덱스)
# print(a) # [1, 2, 1, 2]

a = ["A", "a", "b", "c", "e", "d"]
print(a.count("A"))
print(sorted(a))