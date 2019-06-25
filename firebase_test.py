from requests import get
import json

firebase_url = "https://annoying-clock.firebaseio.com/.json"

Data = get(firebase_url).json()['alarm']
hour = Data['alarm1']['hour']
minute = Data['alarm1']['minute']

print(hour, minute)