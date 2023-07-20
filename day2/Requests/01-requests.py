import requests
import secrets

def main():
    # response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}")
    payload = {'access_key':secrets.API_KEY}
    response = requests.get('http://api.exchangeratesapi.io/v1/latest', params=payload)
    
    
    print(response.status_code)
    print(response.headers['Content-Type'])
    # print(response.text)
    # print(secrets.API_KEY)
    # print(type(response.text))
    response_json = response.json()  #  response를 dictionary화 시킴
    print(response_json['success'])
    print(response_json['timestamp'])
    
    
    
if __name__ == "__main__":
    main()
    
# 비밀번호는 보통 해쉬알고리즘(난수로 저장됨..?)으로 저장된다