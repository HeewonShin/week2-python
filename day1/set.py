# 교집합과 차집합
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1 - s2)


# 중복이 없는 리스트로 출력하기
my_list = [1, 2, 3, 4, 4, 4, 9, 11, 14]
print(set(my_list))
# my_list = list(set(my_list))