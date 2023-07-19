score = int(input('점수가 몇 점인가요? '))

if score <= 100 & score >= 90 :
    print('A')
elif score <90 & score >= 80 :
    print('B')
elif score < 80 & score >= 70 :
    print('C')
elif score < 70 & score >= 60 :
    print('D')
elif score < 60 :
    print('F')
