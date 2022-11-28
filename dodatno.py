import csv
import json

ulogovani_korisnik = {} #trenutno ulogovani korisnik (u recniku)


def ucitaj_predmete(): #za uciavanje predmeta
    predmeti = []
    with open(r"data\predmeti.csv", "r", encoding='utf-8') as pr:
        predmeti_reader = csv.reader(pr)
        next(predmeti_reader)
        for red in predmeti_reader:
            if len(red) > 0:
                predmet = {
                    "sifra": red[0],
                    "naziv": red[1]
                }
                predmeti.append(predmet)
    return predmeti


def ucitaj_profesore(): #za ucitavanje profesora
    profesori = []
    with open(r"data\profesori.csv", "r", encoding='utf-8') as pr:
        profesori_reader = csv.reader(pr)
        for red in profesori_reader:
            if len(red) > 0:
                profesor = {
                    "sifra": red[0],
                    "lozinka": red[1],
                    "ime": red[2],
                    "prezime": red[3],
                    "email": red[4],
                    "termin_konsultacija": red[5]
                }
                profesori.append(profesor)
    return profesori


def ucitaj_studente(): #za ucitavanje studenata
    studenti = []
    with open(r"data\studenti.json", "r", encoding='utf-8') as st:
        try:
            studenti = list(json.load(st))
        except json.JSONDecodeError:
            pass
    return studenti