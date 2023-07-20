import requests
import secrets

def main():
    response = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}')
    
    
    print(response.status_code)
    print(response.headers['Content-Type'])
    
    
    response_json = response.json()  #  response를 dictionary화 시킴
    print(response_json['success'])
    print(response_json['timestamp'])
    print(response_json['rates'])
    
if __name__ == "__main__":
    main()