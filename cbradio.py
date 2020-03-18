#Ora;  Perc;   AdasDb;   Nev
# 6;     0;      2;     Laci

class Cb:
    def __init__(self,sor):
        sor = sor.strip().split(';')
        self.ora  = int(sor[0])
        self.perc = int(sor[1])
        self.db   = int(sor[2])
        self.nev  = sor[3]

with open('cb.txt', 'r', encoding = 'utf8') as f:
    fejlec = f.readline()
    lista = [Cb(sor) for sor in f]
    
# 3. Feladat

print(f"3. Feladat: Bejegyzések száma: {len(lista)} db")

# 4. Feladat
negy = [sor for sor in lista if sor.db==4]
if(len(negy) > 0):
    print(f"4. Feladat: Volt négy adást indító sofőr.")
else:
    print(f"4. Feladat: Nem volt négy adást indító sofőr.")
 
# 5. Feladat

sofor = input(f"5. Feladat: Kérek egy nevet: ")

szamlalo = sum([sor.db for sor in lista if sor.nev == sofor])
if(szamlalo > 0):
    print(f"        {sofor} {szamlalo}X használta a CB-rádiót.")
else:
    print(f"        Nincs ilyen nevű sofőr!")
    
# 6. Feladat   
    
def AtszamolPercre(ora, perc):
    percek = (ora * 60) +perc
    return percek

# 7. Feladat
# cb2.txt  Kezdes;Nev;AdasDb
#          360;Laci;2
with open('cb2.txt', 'w', encoding = 'utf8') as fout:
    fejlec = "Kezdes;Nev;AdasDb\n"
    fout.write(fejlec)
    for sor in lista:
        szoveg = f"{AtszamolPercre(sor.ora,sor.perc)};{sor.nev};{sor.db}\n"
        fout.write(szoveg)

# 8. Feladat

halmaz = {sor.nev for sor in lista}
print(f"8. Feladat: Sofőrök száma: {len(halmaz)}")

# 9. Feladat

szotar = {sor.nev : 0 for sor in lista}
for sor in lista:
    szotar[sor.nev] += sor.db
nev,db = sorted(szotar.items(), key=lambda x:x[1], reverse=True)[0]
print(f"9. Feladat: Legtöbb adást indító sofőr")
print(f"        Név: {nev}")
print(f"        Adások száma: {db} alkalom")

