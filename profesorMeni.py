import json
import csv
import sys
import string 

import dodatno


def menu_prof():
    print("************Glavni meni profesora**************")
    print()

    choice = input("""
                      A: Dodavanje ocene studentu
                      B: Brisanje ocene studentu
                      W: Racunanje prosecne ocene za predmet
                      X: Promena termina konsultacija
                      Q: Povratak na glavni meni

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        dodavanje()
    elif choice == "B" or choice =="b":
       brisanje()
    elif choice == "W" or choice =="w":
       racunanje()
    elif choice == "X" or choice =="x":
        promena_termina()
    elif choice=="Q" or choice=="q":
        menu_prof

    else:
        print("Odaberi A,B,W ili X")
        print("Pokusaj ponovo")
        menu_prof()

def dodavanje():
    studenti = dodatno.ucitaj_studente() #ucitavanje studenata
    predmeti = dodatno.ucitaj_predmete() #ucitavanje liste predmeta
    ime = input("Unesite ime studenta: ")
    ime = ime.upper() #vraca veliko slovo
    redni_broj = 0 #redni broj ispred pretrazenih studenta sa unetim imenom
    for student in studenti: #pretrazivanje studenta po imenu
        if student["ime"].upper().find(ime) != -1:
            redni_broj += 1
            print(str(redni_broj)+".",
                  student["indeks"], student["ime"], student["prezime"])
    if redni_broj > 0:
        indeks = input("Unesite broj indeksa: ")
        postoji_student = False
        for student in studenti: #pretrazivanje unetog indeksa medju studentima
            if str(student["indeks"]) == indeks:
                postoji_student = True
                for i, p in enumerate(predmeti):
                    print(str(i+1)+".", p["sifra"], p["naziv"])
                sifra_predmeta = input("Unesite šifru predmeta: ")
                predmet_postoji = False
                for predmet in predmeti:
                    if predmet["sifra"] == sifra_predmeta: #uneta sifra predmeta se pretrazuje medju postojecim
                        predmet_postoji = True
                        try:
                            ocena = int(input("Unesite ocenu: "))
                            if ocena >= 5 and ocena <= 10:
                                nova_ocena = {
                                    "sifra_predmeta": sifra_predmeta,
                                    "sifra_profesora": dodatno.ulogovani_korisnik["sifra"],
                                    "ocena": ocena
                                }
                                student["ocene"].append(nova_ocena) #ako je uneta ocena u dozvoljenom range onda se dodaje u fajl studenti
                                with open(r"data\studenti.json", "w", encoding='utf-8') as s:
                                    json.dump(studenti, s)
                            else:
                                print("Ocena mora biti izmedju 5 i 10")
                        except ValueError:
                            print("Neispravan unos")
                if not predmet_postoji:
                    print("Neispravna šifra predmeta")
        if not postoji_student:
            print("Neispravan indeksa studenta")
    else:
        print("Ne postoji student sa navedenim imenom.")


def brisanje():
    studenti = dodatno.ucitaj_studente()
    ime = input("Unesite ime studenta: ").upper()
    redni_broj = 0
    for student in studenti: #izlistavanje studenata sa unetim imenom
        if student["ime"].upper().find(ime) != -1:
            redni_broj += 1
            print(str(redni_broj)+".",
                  student["indeks"], student["ime"], student["prezime"])
    if redni_broj > 0:
        indeks = input("Unesite broj indeksa studenta: ")
        student_upisan = False
        ocene_upisane = False
        indeks_ocena = []
        indeks_studenta = 0
        broj_ocena = 0
        
        for s, student in enumerate(studenti):
            if str(student["indeks"]) == indeks:
                indeks_studenta = s
                student_upisan = True
                brojac = 0
                for i, k in enumerate(student["ocene"]):
                    if k["sifra_profesora"] == dodatno.ulogovani_korisnik["sifra"]: #prikazuje samo ocene onih predmeta koje je upisao isti profesor kao onaj sto je trenutno ulogovan
                        brojac += 1
                        indeks_ocena.append(i)
                        ocene_upisane = True
                        broj_ocena += 1
                        print(str(brojac)+".",
                              k["sifra_predmeta"], k["ocena"])
        if not student_upisan:
            print("Neispravan indeksa studenta")
        elif ocene_upisane:
            try:
                redni_broj = int(input("Unesite redni broj: ")) #brisanje ocene za uneti redni br  predmeta
                if redni_broj >= 1 and redni_broj <= broj_ocena:
                    indeks_iz_ocena = indeks_ocena[redni_broj-1]
                    studenti[indeks_studenta]["ocene"].pop(indeks_iz_ocena)
                    with open(r"data\studenti.json", "w", encoding='utf-8') as fajl:
                        json.dump(studenti, fajl)
                else:
                    print("Neispravan unos")
            except ValueError:
                print("Neispravan unos")
        elif not ocene_upisane:
            print("Nema ocenu")
    else:
        print("Ne postoji student sa unetim imenom") 

def racunanje():
    studenti = dodatno.ucitaj_studente()
    predmeti = dodatno.ucitaj_predmete()
    for i, p in enumerate(predmeti):
        print(str(i+1)+".", p["sifra"], p["naziv"]) #izlistavanje svih predmeta i njihovih sifri
    try:
        unos = int(input("Unesite redni broj predmeta: "))
    except ValueError:
        print("Neispravan unos")
    if unos < 1 or unos > len(predmeti):
        print("Neispravan unos")
    else:
        sifra_predmeta = predmeti[unos-1]["sifra"] #ako je unos ispravan racuna se prosecna ocena izabranog predmeta kod svih studenata
        zbir = 0
        broj_ocena = 0
        for student in studenti:
            for o in student["ocene"]:
                if o["sifra_predmeta"] == sifra_predmeta and o["sifra_profesora"] == dodatno.ulogovani_korisnik["sifra"]:
                    zbir += o["ocena"]
                    broj_ocena += 1
        if broj_ocena > 0:
            print("Prosečna ocena je: {:.2f}".format(zbir/broj_ocena))
        else:
            print("Ne postoje ocene ")

def promena_termina():
    print(dodatno.ulogovani_korisnik["termin_konsultacija"])
    novi_termin = input("Unesite novi termin konsultacija: ").strip() #uklanja praznine na pocetku i kraju stringa

    if novi_termin != "": #provera da li je korisnik uneo nesto
        dodatno.ulogovani_korisnik["termin_konsultacija"] = novi_termin
        profesori = dodatno.ucitaj_profesore()
        for profesor in profesori: #pretrazuje ulogovanog profesora u bazi podataki da bi nasao njegov termin
            if profesor["sifra"] == dodatno.ulogovani_korisnik["sifra"]:
                profesor["termin_konsultacija"] = novi_termin
        with open(r"data\profesori.csv", "w", encoding='utf-8') as fajl:
            termin_writer = csv.writer(fajl)
            for profesor in profesori: #novi termin se upisuje u fajl
                termin_writer.writerow(profesor.values())
                

   




       


