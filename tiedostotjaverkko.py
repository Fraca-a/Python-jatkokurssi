# tiedoston lukeminen ja kirjoittaminen with -lauseen avulla
# (muitakin tapoja on, with nykyisin suositeltavin)
# Jos tiedostojen käsittely visual studio codessa ei
# vaikuta toimivan, katso 
# https://ohjelmointi-23.mooc.fi/osa-6/1-tiedostojen-lukeminen#mita-jos-vs-code-ei-loyda-tiedostoja-koodia-suoritettaessa

tiedostonimi = "koe.txt"
with open(tiedostonimi) as tiedosto:
    teksti = tiedosto.read()
    print("Tiedostossa", tiedostonimi, "on", len(teksti), "merkkiä.")
    print("Alkusulkuja:", teksti.count("("))
    print("Printtejä:", teksti.count("print("))

# tiedoston käsittely riveittäin
tiedostonimi = "koe.txt"
with open(tiedostonimi) as tiedosto:
    rivinro = 1
    for rivi in tiedosto:
        print(f"{rivinro}: {rivi}", end="")
        rivinro += 1
print()

tiedosto2nimi = "uusi" + tiedostonimi
# avataan tiedosto kirjoittamista varten: "w", toinen
# yleinen tapa on avata tiedosto loppuun lisäämistä varten,
# silloin: "a"

uusi = "--- --- ---\n" + teksti
print(uusi)

with open(tiedosto2nimi, "a") as tiedosto:
    tiedosto.write(uusi.lower())

# csv-tiedosto
# comma-separated values -tyylinen tiedosto on yleinen tapa 
# siirtää tietoja esim. taulukkolaskentohjelmaan
# ja sieltä pois. Toisiinsa liittyvät arvot ovat samalla 
# rivillä, ja erottimena voi olla pilkun sijasta jokin 
# muukin merkki.
# Pythonissa csv-moduli helpottaa tämän tiedostomuodon 
# käsittelyä:

import csv

with open("esim.csv") as csvtiedosto:
    for rivi in csv.reader(csvtiedosto, delimiter=";"):
        print(rivi)

## JSON -tiedostomuoto

# JSON (JavaScript Object Notation) on tapa esittää rakenteista tietoa tekstimuodossa. 
# Sitä käytetään laajasti verkkopalveluissa tiedonsiirtomuotona sekä myös esim. sovellusten 
# asetusten jne tallentamiseen. Se on melkein täysin korvannut 
# XML-esitystavan näissä käyttötarkoituksissa.
# JSON voi sisältää seuraavia rakenteita (jotka puolestaan 
# voivat esiintyä sisäkkäin):
# * objekti: kaarisulkujen sisään kirjoitettu joukko rakenteitai, jossa avain merkkijonona, ":", ja arvo. Esim.
# { "pituus" : 188 } ja { "etunimi": "Pike", "sukunimi": "Kaakko", "ika": 22 }
# * taulukko: 0 tai useampia hakasulkujen väliin kirjoitettuja rakenteita, jotka on erotettu toisistaan pilkulla. Esim.
# [ { "pituus" : 188 }, { "pituus" : 165 }, { "pituus" : 177 } ]

# Esimerkki verkko-osoitteesta, joka vastaa HTTP-protokollan GET-pyyntöön (jonka selain tekee kun osoiteriville 
# kirjoittaa osoitteen) on https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json/

# JSON-muotoa käsitellään yksityiskohtaisemmin täällä: https://www.json.org/json-en.html
# Pythonissa JSON -muotoisen tiedon käsittelyyn voidaan käyttää
# json-pakettia. Myöhemmin tutustutaan muihin tapoihin käsitellä JSON-tietoa.

import json

# json-modulin loads()-funktion avulla parsitaan eli "avataan" merkkijono (joka sisältää JSON-muotoista tietoa). 
# Parsittu merkkijono sisältää uloimmalla tasolla joko hakemiston tai taulukon, jota voidaan käsitellä normaalisti 
# Python-kielen keinoin. Uloimman tason rakenne voi sisältää edelleen rakenteista tietoa.

esim1 = '{ "pituus" : 188 }'
esim2 = '{ "etunimi": "Pike", "sukunimi": "Kaakko", "ika": 22 }'
esim3 = '[ { "pituus" : 188 }, { "pituus" : 165 }, { "pituus" : 177 } ]'
#esim4 = '{ "koodi": "TX00DZ62", "arvosanat": [{"arvosana": 5}, {"arvosana": 4}, {"arvosana": 5}, {"arvosana": 2}]}'
esim4 = '{ "koodi": "TX00DZ62", "arvosanat": [5, 4, 5, 2]}'

e1 = json.loads(esim1)
print(e1)
print(e1['pituus'])

e2 = json.loads(esim2)
print(e2)
print(e2.keys())
print(e2['etunimi'], e2['sukunimi'], e2['ika'])

e3 = json.loads(esim3)
print(e3)
print(len(e3))
for e in e3:
    print(e['pituus'])
    
e4 = json.loads(esim4)
print(e4['koodi'])
print(e4['arvosanat'])
print(sum(e4['arvosanat']) / len(e4['arvosanat']))

# kun json-muotoista dataa luetaan tiedostosta, voidaan koko data lukea merkkijonomuuttujaan
# ja sitten käyttää .loads() -metodia kuten edellä.
with open("seating.json") as tiedosto:
    data = tiedosto.read() # muuttuja data on tyypiltään merkkijono
    
eduskunta = json.loads(data)

print(len(eduskunta))
print(eduskunta[0])
print(eduskunta[0]['firstname'])
print(eduskunta[100])
print(eduskunta[100]['firstname'])

# Etsitään kansanedustajat, joiden etunimi on Sari
for edustaja in eduskunta:
    if edustaja["firstname"] == "Sari":
        print(edustaja["firstname"], edustaja["lastname"], edustaja["party"])

# Kun käsiteltävä tieto on verkossa, voidaan se lukea esim. käyttämällä urllib.request -modulia. 
# Tietosisältö luetaan merkkijonomuuttujan arvoksi, ja jatkokäsittely tapahtuu samalla tavalla 
# kuin aikaisemmissa esimerkeissä.

# mikäli verkkopyynnöt eivät onnistu, kokeile (macissä):
# cd "/Applications/Python 3.8/" # tai käytössäsi oleva versio 8:n sijaan
# sudo "./Install Certificates.command
# tai jos yhä ongelmia, lue lisää vinkkejä kohdasta https://ohjelmointi-22.mooc.fi/osa-7/4-datan-kasittely
# Kurssien tilastot -tehtävän kohdalta

import urllib.request

# tässä osoitteessa kopio kansanedustajatiedoista
pyynto = urllib.request.urlopen("http://users.metropolia.fi/~peterh/seating.json")
data = pyynto.read()

uusieduskunta = json.loads(data)

print(type(uusieduskunta))
print(len(uusieduskunta))
print(uusieduskunta[0])
print(uusieduskunta[100])

# tai tiedon alkulähteeltä, Eduskunnan sivuilta uusin eduskunta:
#pyynto = urllib.request.urlopen("https://avoindata.eduskunta.fi/api/v1/seating/")
#data = pyynto.read()

uusieduskunta = json.loads(data)
print(len(uusieduskunta))
print(uusieduskunta[0])
print(uusieduskunta[100])
