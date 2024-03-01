from urllib.request import urlopen
import time, requests

def getData():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]
    return longitude, latitude

while True:
    print(getData())
    time.sleep(1)




