import json
import csv
import sys
import string 


    
import dodatno




def menu_stud():
    print("************Glavni meni studenta**************")
    print()

    choice = input("""
                      A: Računanje globalne prosečne ocene
                      B: Prikaz položenih ili nepolozenih predmeta
                      W: Prikaz podataka o profesoru koji predaje predmet
                      Q: Povratak na glavni meni
                      

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        prosecna_ocena()
    elif choice == "B" or choice =="b":
      polozeno_ili_nepolozeno()
    elif choice == "W" or choice =="w":
       podaci_profesora()
    elif choice=="Q" or choice=="q":
        print("Na glavni meni")
        menu_stud()
    else:
        print("Odaberi A,B ili Q")
        print("Pokusaj ponovo")
        menu_stud()

def prosecna_ocena():
    studenti = dodatno.ucitaj_studente()
    for student in studenti:
        if student["indeks"] == dodatno.ulogovani_korisnik["indeks"]:
            zbir=0
            for ocena in student["ocene"]:
                zbir += ocena["ocena"]
            if len(student["ocene"]) > 0:
                prosek = float(zbir/len(student["ocene"])) #racunanje prosecne ocene svih predmeta za trenutno ulogovanog korisnika
                print("Prosecna ocena je: {:.2f}".format(prosek))
            else:
                print("Nema ocene")

def polozeno():
    predmeti = dodatno.ucitaj_predmete()
    studenti = dodatno.ucitaj_studente()
    predmeti_upisani = False
    for student in studenti:
        if student["indeks"] == dodatno.ulogovani_korisnik["indeks"]:
            for ocena in student["ocene"]:
                for p in predmeti:
                    if ocena["sifra_predmeta"] == p["sifra"]: #
                        predmeti_upisani = True
                        print(p["sifra"], p["naziv"])
                        print("Ocena:", ocena["ocena"])
    if not predmeti_upisani:
        print("Nema položenih predmeta")

def nepolozeno():
    predmeti = dodatno.ucitaj_predmete()
    studenti = dodatno.ucitaj_studente()
    postoje_predmeti = False
    for student in studenti:
        if student["indeks"] == dodatno.ulogovani_korisnik["indeks"]:
            for p in predmeti:
                polozen = False
                for ocena in student["ocene"]:
                    if ocena["sifra_predmeta"] == p["sifra"]:
                        polozen = True
                if not polozen: #prikazuje sve one predmeti za koje student nema ocena tj nisu u polozenim
                    print(p["sifra"], p["naziv"])
                    postoje_predmeti = True
    if not postoje_predmeti: #ako su svi predmeti u polozenim 
        print("Nema nepoloženih predmeta")

def polozeno_ili_nepolozeno(): #funkcija koja u zavisnosti od odabira korisnika poziva sledece: polozeno() ili nepolozeno()
    choice = input("""
                      A: Položeni
                      B: Nepoloženi
                      Q: Izlaz

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        polozeno()
    elif choice == "B" or choice =="b":
        nepolozeno()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("Odaberi A ili B")
        print("Pokusaj ponovo")
        polozeno_ili_nepolozeno()

def podaci_profesora():
    studenti = dodatno.ucitaj_studente()
    predmeti = dodatno.ucitaj_predmete()
    profesori = dodatno.ucitaj_profesore()
    for predmet in predmeti: #prikaz svih predmeta iz baze
        print(predmet["sifra"], predmet["naziv"])
    sifra_predmeta = input("\nUnesite šifru predmeta: ")
    unos = False
    for predmet in predmeti:
        if predmet["sifra"] == sifra_predmeta:
            unos = True
    if unos:
        for student in studenti:
            if student["indeks"] == dodatno.ulogovani_korisnik["indeks"]:
                postoji = False
                for ocena in student["ocene"]:
                    if sifra_predmeta == ocena["sifra_predmeta"]:
                        for profesor in profesori:
                            if profesor["sifra"] == ocena["sifra_profesora"]: #proverava sifru profesora u profesorima sa sifrom profeosra iz fajla studenti 
                                postoji = True #ako postoji izlistava podatke profesora koji je za odabrani predmet 
                                print(profesor["ime"], profesor["prezime"])
                                print("Email:", profesor["email"])
                                print("Termin konsultacija:",
                                      profesor["termin_konsultacija"])
                if not postoji:
                    print("\nNema profesora za taj predmet.")
    else:
        print("Neispravna šifra predmeta!")
    
    
       

                       
                
                      

                      


    
    

