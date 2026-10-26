import urllib.request
import json

pyynto = urllib.request.urlopen("http//users.metropolia.fi/~peterh/seating.json")
data = pyynto.read()
print(len(data))

eduskunta = json.loads(data)
print(len(eduskunta))

puoluekartta = {}

for edustaja in eduskunta:
    puolue = edustaja ["party"]
    if puolue in puoluekartta:
        puoluekartta[puolue].append(edustaja)
    else:
        puoluekartta[puolue] = [edustaja]

for puolue in puoluekartta:
    print(puolue, len(puoluekartta[puolue]))

ministereitä = 0
for edustaja in eduskunta:
    if edustaja["minister"]:
        print(edustaja["firstname"], edustaja["lastname"])
        ministereitä += 1
print("Ministereitä on", ministereitä)

hallituspuolueet = []
for edustaja in eduskunta:
    if edustaja["minister"] and edustaja ["party"] not in hallituspuolueet:
        hallituspuolueet.append(edustaja["party"])

print(hallituspuolueet)

edustajamäärä = 0
for puolue in hallituspuolueet:
    edustajamäärä += len(puoluekartta[puolue])

print(edustajamäärä)

edustajamäärä = 0
for puolue in ["liik", "tv", "ps", "kok"]:
    edustajamäärä += len(puoluekartta[puolue])

print(edustajamäärä)

def paikkamäärä(puolueet)
    edustajamäärä = 0
    for puolue in puolueet:
        edustajamäärä += len(puoluekartta[puolue])
        return edustajamäärä

print(paikkamäärä(["liik", "tv", "ps", "kok"]))
print(paikkamäärä(["liik", "tv", "ps", "kok"]))