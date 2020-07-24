import requests
import json

api_url = 'http://localhost:8000/predict'
file_path = '../data/images/ISIC_0052212.jpg'

if __name__ == '__main__':
    response = requests.post(
        api_url,
        files = {'img': open(file_path, 'rb')}
    )
    print(response.json()['prediction'])
