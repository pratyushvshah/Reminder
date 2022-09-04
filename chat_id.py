import requests

TOKEN = "<YOUR BOT TOKEN>"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json()['result'][0]['message']['chat']['id'])
