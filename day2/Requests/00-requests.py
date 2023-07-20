# 가상 python 환경 venv

import requests

def main():
    response = requests.get('https://outback.60736ldvbpamu.ap-northeast-2.cs.amazonlightsail.com/participation/statistics')
    #  print(response)
    print(response.status_code)  # 
    print(response.headers['Content-Type'])  # 중요--- application/json인지 html/css 등인지를 판단할 수 있다
    print("Content:", response.text)
    # GET POST PATCH PUT DELETE
    
if __name__ == '__main__':  # main함수 실행,,보통 파이썬에서 이렇게 적음
    main()
