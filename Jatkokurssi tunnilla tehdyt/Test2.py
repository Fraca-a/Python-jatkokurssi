import json

with open("kurssit.json") as tiedosto:
    data = tiedosto.read()

kurssi = json.loads(data)

print(len(kurssi))
print(kurssi[0])

import urllib.request

pyynto = urllib.request.urlopen("https://users.metropolia.fi/~peterh/kurssit.json")
data = pyynto.read()

kurssit = json.loads(data)
print(len(kurssit))
print(kurssit[0])