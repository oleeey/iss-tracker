import matplotlib.pyplot as plt

longitudeL = []
latitudeL = []

f = open("coordinates.txt", "r")
for l in f:
    l = l.strip().split(";")
    l.pop(2)
    longitudeL.append(l[0])
    latitudeL.append(l[1])






