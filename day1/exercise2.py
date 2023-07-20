# 구구단

def multiply():
    for y in range(2, 10):
        print('------구구단', y,'단------') 
        for x in range(1, 10):
            print(y, "*", x, " = ", x*y)

        
multiply()

# 커피자판기

coffee_dict = {'americano':
    {'price':2000, 'type':'ice'},
    'latte':
        {'price':2500,'type':'hot'}}





# BMI지수
def return_bmi(height, weight):
    height = height / 100
    bmi = round(weight / (height * 0.01)**2 , 2)

    if bmi < 18.5:
        print('저체중')
    elif bmi <24.9:
        print('정상')
    elif bmi < 29.9:
        print('과체중')
    else:
        print('비만')