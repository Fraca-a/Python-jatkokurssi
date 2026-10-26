# Tehtävä 1 opintolaskuri
# Nimi: Mikael Främling
# Opiskelijanumero: 2628454

# alusta tarvittavat muuttujat, kuten esim. opintopisteiden summa
kurssitulostus = ""
kurssien_määrä = 0
pisteiden_summa = 0
painotettu_summa = 0
arvosanojen_summa = 0
# ... ja mahdolliset muut alustukset

# tulosta alkutervehdys
# (tervehdys tulostetaan silmukan alussa joka kierroksella, ks. alla)

# toistorakenne, josta poistutaan break-lauseella ja joka aloitetaan
# tarvittaessa uudestaan continue-lauseella
while True:
    # lue käyttäjän syöttämä kurssin nimi ja käytä if-lausetta, jotta voit päätellä, halutaanko ohjelman suoritus lopettaa
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi = input("Nimi: ")

    if nimi == "lopeta":
        break

    # lue käyttäjän syöttämät opintopisteet ja arvosana (muista tarkistaa syötteen laillisuus)
    opintopisteet = int(input("Opintopisteet: "))

    # tarkista if-lauseella, että käyttäjän syötteet ovat sallituissa rajoissa
    if opintopisteet < 0 or opintopisteet > 20:
        print("Virheellinen syöte.")
        # vihje: toistorakenteen suorituksen voi aloittaa alusta continue-lauseella
        continue

    arvosana = int(input("Arvosana: "))

    if arvosana < 1 or arvosana > 5:
        print("Virheellinen syöte.")
        continue

    # päivitä muuttujat, joihin keräät opintopisteiden summan ja muut tarvittavat tiedot
    kurssien_määrä = kurssien_määrä + 1
    pisteiden_summa = pisteiden_summa + opintopisteet
    painotettu_summa = painotettu_summa + opintopisteet * arvosana
    arvosanojen_summa = arvosanojen_summa + arvosana

    # kurssitulostuksen sisällön voit muodostaa merkkijonoon käyttämällä f-merkkijonoja ja + -operaatiota.
    # \n -merkki tuottaa rivinvaihdon tulostaessa merkkijonon
    kurssitulostus = kurssitulostus + f"{kurssien_määrä}. {nimi}({opintopisteet}op): {arvosana}\n"

# laske halutut tunnusluvut, ota huomioon myös tapaus jossa käyttäjä ei ole syöttänyt mitään
print(f"Opintopisteet yhteensä {pisteiden_summa}")

# tulosta tunnusluvut, f-merkkijonon voi muotoilla siten, että tulostetaan vain haluttu määrä desimaaleja
if kurssien_määrä > 0:
    print("Suoritetut kurssit:")
    print(kurssitulostus, end="")

    keskiarvo = arvosanojen_summa / kurssien_määrä
    painotettu_keskiarvo = painotettu_summa / pisteiden_summa

    print(f"Arvosanojen keskiarvo: {keskiarvo:.1f}")
    print(f"Arvosanojen painotettu keskiarvo: {painotettu_keskiarvo:.1f}")