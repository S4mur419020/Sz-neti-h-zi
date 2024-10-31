import random
import math

def fel1():
    szam:int=int(input(print("Adj meg egy számot!")))
    if szam>920:
        print("A szám nagyobb min 920!")
    elif szam<200:
        print("A szám kisebb mint 200!")
        
def fel2():
    ora:int=int(input(print("Hanyadik óra?: ")))
    if ora==0:
        print("Be se jövök!")
    elif ora==1:
        print("Még 90%-on vagyunk!")
    elif ora==2:
        print("Még bírjuk (60%)")
    elif ora==3:
        print("Még bírjuk (60%)")
    elif ora==4:
        print("Progit tanulink, töltődünk!(70%)")
    elif ora==5:
        print("Progit tanulink, töltődünk!(70%)")
    elif ora==6:
        print("Progit tanulink, töltődünk!(70%)")
    elif ora==7:
        print("Progit tanulink, töltődünk!(70%)")
    elif ora==8:
        print("Lassan nem bírjuk tovább! (50%)")
    elif ora==9:
        print("Lassan nem bírjuk tovább! (50%)")
    else:
        print("Ez már tényleg túlzás!")
        
'''def fel3(nap:str, ora:str):
    nap:str=str(input(print("Adj meg egy napot:")))
    ora:str=str(input(print("adj meg egy tantárgyat:")))
    
    if nap=="Hétfő":
        print("alszik")
        
    elif nap =="Kedd":
        if ora=="Hittan":
            print("figyel")
        else:
            print("alszik")
        
    elif nap =="Szerda":
        if ora=="Progi":
            print("dolgozik")
        else:
            print("alszik")
        
    elif nap=="Csütörtök":
        print("figyel")
    
    elif nap=="Péntek":
        print("félig figyel")
    
    else:
        print("Nincs információnk.")
    
print(fel3("Hétfő","bármi"))
print(fel3("Kedd","Hittan"))
print(fel3("Szerda","Progi"))
print(fel3("Csütörtök","bármi"))
print(fel3("Péntek","bármi"))'''

def fel4():
    szam:int=int(input(print("Adj meg egy egész számot: ")))
    if szam>0:
        print(f"A szám gyöke:{math.sqrt(szam)}")
    else:
        print("A szám negatív! Nem lehet ngyököt vonni belőle!")
        
def fel5():
    szam_a:int=int(input(print("Adj meg egy egész számot!")))
    szam_b:int=int(input(print("Adj meg egy másik egész számot!")))
    kerulet=2*(szam_a+szam_b)
    print(f"A téglalap Kerülete:{kerulet}")
    terulet=szam_a*szam_b
    print(f"A téglalap területe: {terulet}")
    
def fel6():
    szamok=[]
    i=0
    while i<13:
        rszam:int=int(random.random()*17)-5 
        szamok.append(int(rszam))
        i+=1
    return szamok
def fel6_2(szamok):
    negativ=len([rszam for rszam in szamok if rszam<0])
    pozitiv=len([rszam for rszam in szamok if rszam>0])
    
    return pozitiv, negativ
def fel6_3(szamok):
    ossz =0
    for rszam in szamok:
        if rszam %2==0:
            ossz+=rszam
    return ossz
    
def fel6_4(szamok):
    paratlan=0
    paros=0
    for rszam in szamok:
        if rszam %2==0:
            paros+=rszam
        else:
            paratlan+=rszam
    return paratlan, paros

def fel6_5(szamok):
    atlag=0
    for rszam in szamok:
        atlag+=rszam
    if len(szamok)==0:
        return 0
    return atlag/len(szamok)

def fel6_6(szamok):
    if len(szamok)==0:
        return
    max=szamok[0]
    for rszam in szamok:
        if rszam>max:
            max=rszam
    return max