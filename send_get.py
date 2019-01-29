import requests

url = 'http://127.0.0.1:5000/move'

command = {
            'botId': 2,
            'moveType':4
}

r=requests.get(url,json=command)

print(r.json()['success'])