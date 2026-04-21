import os #za proveru postojanja json fajla studenti
import json
import csv
import sys #za izlazak iz aplikacije
import string 
from profesorMeni import menu_prof
from studentMeni import menu_stud
import dodatno 

def main(): #funkcija pokrece program pozivanjem druge funkcije koja ucitava glavni meni
   menu()

def menu(): #funkcija koja prikazuje glavni meni 
    print("************Dobrodišli na Glavni Meni**************")
    print()

    choice = input("""
                      A: Registracija
                      B: Login
                      Q: Izlaz

                      Unesite slovo ispred izabrane opcije: """)

    if choice == "A" or choice =="a":
        register()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        sys.exit()
    else:
        print("Odaberi A,B ili Q")
        print("Pokusaj ponovo")
        menu()

        
def login(): 
    print("***********Prijava na sistem***********")
    profesori = dodatno.ucitaj_profesore() #učitavaju se podaci o vec postojecim profesorima
    studenti = dodatno.ucitaj_studente() #učitavaju se podaci o vec postojecim studentima
    korisnicko_ime = input("Unesite Vaše korisničko ime: ")
    lozinka = input("Unesite vašu lozinku: ")
    for profesor in profesori: #for petlja prolazi kroz ucitane profesore i trazi podudaranje sa unetim podacima korisnika
        if korisnicko_ime == profesor["sifra"] and lozinka == profesor["lozinka"]:
            dodatno.ulogovani_korisnik = profesor
            menu_prof()
       
    for student in studenti: #for petlja prolazi kroz ucitane studente i trazi podudaranje sa unetim podacima korisnika
        if korisnicko_ime == str(student["indeks"]) and lozinka == student["lozinka"]:
            dodatno.ulogovani_korisnik = student
            menu_stud()


def register(): 
    print("************Dobro došli, registrujte se:**************")
    print()

    izbor = input("""
                      P: Profesor
                      S: Student
                      Q: Izlaz

                      Please enter your choice: """)

    if izbor == "P" or izbor =="p":
        registracijaProf()
    elif izbor == "S" or izbor =="s":
        registracijaStud()
    elif izbor=="Q" or izbor=="q":
        sys.exit
    else:
        print("Odaberi P ili S")
        print("Pokusaj ponovo")
        register()

def registracijaProf():
        #korisnik unosi sve trazene podatke za registraciju kao profesor
        print("Unesite username koji se sastoji od 3 broja:")
        global username
        username=input()
        print("Unesite lozinku:")
        global password
        password=input()
        print("Unasite ime:")
        global firstname
        firstname=input()
        print("Unesite prezime:")
        global surname
        surname=input()
        print("Unesite email adresu:")
        global email
        email=input()
        print("Unesite termin konsultacija")
        global termin
        termin=input()

#uneti podaci korisnika se cuvaju na sistemu
        with open(r"data\profesori.csv",'a', encoding="utf8" ) as prof:
         profWriter=csv.writer(prof)
         profWriter.writerow([username,password,firstname,surname,email,termin])
         print("Vasi podaci su sacuvani")
         prof.close()
         menu()

#korisnik unosi sve trazene podatke za registraciju kao student
def registracijaStud():
    studenti = dodatno.ucitaj_studente()
    indeks = int(input("Unesite broj indeksa: "))
    for student in studenti: #za proveru jedinstvenosti indeksa koji je korisnik uneo petlja prolazi kroz vec postojece indekse u sistema 
                if student["indeks"] == str(indeks):
                    print("Već postoji korisnik s tim brojem indeksa.")
                    return
    lozinka = input("Unesite lozinku: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    email = input("Unesite email: ")
    student = {
                "indeks": indeks,
                "lozinka": lozinka,
                "ime": ime,
                "prezime": prezime,
                "email": email,
                "ocene": []
            }
    studenti = []
    if os.path.exists(r"data\studenti.json"):
        with open(r"data\studenti.json", "r", encoding='utf-8') as fajl_studenti:
            try:
                studenti = list(json.load(fajl_studenti))#uneti podaci korisnika se cuvaju na sistemu
            except json.JSONDecodeError: #greska sa json fajlom
                pass
    studenti.append(student)
    with open(r"data\studenti.json", "w", encoding='utf-8') as fajl_studenti:
        json.dump(studenti, fajl_studenti)
    
        return


    
main()


            

                  
         
               
               
            
            
            
                  
              
               
         
                    
