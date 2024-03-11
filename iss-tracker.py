import time, requests, turtle, csv
def getData():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]
    return [longitude, latitude]

def gui():
    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)

    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()

    while True:
        iss.goto(getData()[0], getData()[1])
        time.sleep(5)



while True:                      
    # print(getData()[0],getData()[1])
    coords = ";".join(getData()) + ";"
    print(coords)
    f = open("coordinates.txt", "a")
    f.write(coords + "\n")
    f.close()
    time.sleep(5)



