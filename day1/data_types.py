#print('hello')

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

# a = ["A", "a", "b", "c", "e", "d"]
# print(a.count("A"))
# print(sorted(a))

# my_list = [0] * 10
# my_tuple = (0, ) * 10 # 튜플로 인식 시키려면 ,콤마를 찍어야됨

# print(my_list)
# print(my_tuple)

# my_list = [1, 2, 3, ["a", "b", "c"]]
# print(my_list[3][2])
# print(len(my_list))  # 4
# print(len(my_list[3]))  # 3

# my_dictionary = dict()  # 빈 딕셔너리
# my_dictionary = {'name':'Heewon', 'location':'Yangsan'}

# my_dictionary['name'] = 'Paul'  # 키, 밸류값 변경하기
# del my_dictionary['age']
# my_dictionary['favorite_foods'] = [{'name':'pizza',
#                                     'is_healthy':False},
#                                     {'name':'hamburger',
#                                     'is_healty':False}]
# print(my_dictionary)
# print(my_dictionary['favorite_foods'])
# print(my_dictionary.get('age'))  #  키 값 찾기!!
# print(my_dictionary.get("office_location", '모름'))  # 찾는 key 값, 없는 경우 출력될 값

# for key in my_dictionary.keys():
#     print(key)
    
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary.items())
# for key, value in my_dictionary.items():
#     print('keys : ', key)
#     print('values : ', value)
    

# print('age' in my_dictionary)  # age라는 key값 출력,, true/false 출력

# if 'age' in my_dictionary:
#     pass
# else:
#     my_dictionary['age'] = 50

# my_list = [1, 2, 3, 4, "A"]
# print(set(my_list))
# my_list.append("B")
# my_list.append("B")
# my_list.append("B")
# print(my_list)  # B가 계속 추가됨(중복 허용)

# my_set = {1, 2, 3}
# my_set.add(4)
# my_set.add(4)  # set는 중복값을 허용하지 않아서 값을 추가해도 한번만 추가됨
# print(my_set)

# a = "Hello"
# my_set = set(a)  # set로 바꿈
# print(my_set)

# set1 = {1, 2, 3, 4, 5}
# set2 ={4, 5, 6, 7}

# print(set1 & set2)  # 교집합
# print(set1 | set2)  # 공집합
# print(set1 - set2)  # 차집합

# print(5 == '5')
# print(5 != "5")

# print(5 > 3 and 10 > 1)
# print(5 > 3 or 1 > 10)
# print(not False)

# score = int(input('점수가 몇 점인가요? '))

# if score >= 60 :
#     print('pass')
# else:
#     print('fail')

# a = 10
# while a > 0:
#     print('hello')
#     a -= 1
    
    
# a = -5
# while a < 0:
#     print('a is below 0')
#     a += 1

# my_list = ['A', 'B', 'C', 'D']
# for letter in my_list:  # 변수명 잘 정하기!
#     print(letter)

# # for i in range(len(my_list)):
# #    print(my_list[i])

# # for i in range(5):  # i는 0부터 시작, 5개 출력
# #     print(i)

# def say_hello(name):
#     print('hello', name)
    
# say_hello('희원')

# abs 함수
# print(abs(-3))
# print(abs(-3.5))

# #id 함수
# a = 3
# print(id(a))

# b = 3
# print(id(b))
# print(id(a is b)) #  객체 주소값 출력됨


# # sum 함수 : 합계 구해줌
# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# def say_hello(my_list):
#     if not isinstance(my_list, list):
#         print("Error")
#         return
#     for name in my_list:
#         print("hello", name)
        
# say_hello("Mike")

# range함수
# print(range(5))  # 총 3개의 값이 들어감,,(시작값, 0부터 시작하니까 최대값 -1, 증가량 혹은 감소량)
# for i in range(5, 0, -2):
#     print(i)
    
# # filter 함수 : true인 것만 걸러줌,,(g함수, 반복 가능한 데이터) 
    
# a = [5, 3, 2, 1, 4]
# print(sorted(a))
# a.sort()
# print(a)

# def positive(x):
#     return x > 0
# a = [1, 3, 0, -4, -8]

# print(list(filter(positive, a)))


# enumerate : 인덱스를 포함하는 enumerate객체를 리턴,,  많이 사용!

# colors = ["white", "red", "brown", "blue"]
# names = ["Lukas", "Mike", "Yoon", "Lee"]

# for i, name in enumerate(names):
#     print(name, f'likes color {colors[i]}')  # f를 붙여주면 자동으로 {}안을 변수로 인식!
    

# number_list = [55, 21, 1, 158, 88, 213]
# print(max(number_list))

# int함수 : 소수점 값은 무조건 내림 처리!
# print(int('35'))
# print(int(3.8))

# # tuple 함수
# a = [1,1, 1, 1 ,1 ,1 ,1 ,1, 4, 4, 4]
# print(tuple(a))

# a = '3.5'
# print(float(a))

# print(bool('a'))  # 0이 아닌 대부분의 수는 true

# print(len("Dfsafa"))
# print(len(['d', 5, 'd']))

# a = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in range(0, len(a)):
#     print(a[i])
    
# a = 3.5
# print(str(a) == '3.5')

# print(type(str(a)))

# 외장함수
# import os
# print(os.getcwd())  # get current working directory
# print(os.name)

# import time
# # from time import time
# print(time.time())  # epock 검색해서 넣어보면 시간 알 수 있음

# def million_operations_function():
#     start = time.time()
#     my_list = []
#     for _ in range(0, 1000000): # i를 사용하지 않을 때 _ 로 표시   
#         my_list.append(0)
        
#     end = time.time()
#     print(end - start)  # 1000000번 찍는데 얼마나 걸렸는지 시간 잴 수 있다
    
    
# import datetime
# now = datetime.datetime.now()
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)    
        
        
import random
print(random.randint(0, 10))  # random 함수 : 0~10 사이의 숫자 랜덤하게 나옴