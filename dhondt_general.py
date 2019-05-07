from tabulate import tabulate

# Definicija klase i metoda #
class Stranka:
  def __init__(self, imeStranke, brojGlasova, brojMandata):
    self.imeStranke = str(imeStranke)
    self.brojGlasova = int(brojGlasova)
    self.brojMandata = int(brojMandata)

# Funkcija vraca broj glasova za proslijedjenu stranku #
def dobaviGlasovePoImenu(trazenaStranka):
  for index, item in enumerate(listaUnesenihStranaka):
    if item.imeStranke == trazenaStranka:
        return item.brojGlasova

# Funkcija vraca broj osvojenih metoda za proslijedjenu stranku #
# Obzirom da smo sortirali kolicnike po broju glasova, metoda ce uzeti broj glasova stranke i podijeliti ga sa zajednickim kolicnikom #
# Na taj nacin dobijamo broj osvojenih mandata za trazenu stranku #
def dobaviBrojOsvojenihMandata(trazenaStranka):
    for index, item in enumerate(listaUnesenihStranaka):
        if item.imeStranke == trazenaStranka:
            return item.brojGlasova/zajednickiKolicnik

# Definicija Varijabli #
ukupanBrojGlasova = 0
listaUnesenihStranaka = []
nezadovoljavajuciPrag = []
zadovoljavajuciPrag = []
listaKolicnika = []
zajednickiKolicnik = 0
imenaStranaka = []
konacnaListaMandata = []

# Unos broja stranki #
print ("Unesite broj stranki: ")
ukupanBrojStranki = input()
ukupanBrojStranki = int(ukupanBrojStranki)

# Unos broja mogucih mandata za podjelu #
print ("Unesite broj mogucih mandata: ")
ukupanBrojMandata = input()
ukupanBrojMandata = int(ukupanBrojMandata)

# Unos stranaka #
print("------------------------------------------------------------------")
print("- Unesite ime stranke u formatu \"Ime Stranke Broj Glasova\"       -")
print("- Primjer: SDP 1550                                              -")
print("------------------------------------------------------------------")
print("Nakon svakog unosa, potvrdite sa tipkom ENTER")
print("------------------------------------------------------------------")

for unos in range(ukupanBrojStranki):
  data = input("{}. UNOS--> ".format(unos+1))
  data = str(data)
  splitUnosa = data.split()
  unesenaStranka = Stranka(str(splitUnosa[0]), int(splitUnosa[1]), 0)
  listaUnesenihStranaka.append(unesenaStranka)

# Lista kolicnika dhondt #
for stranka in listaUnesenihStranaka:
  for mandat in range(1, ukupanBrojMandata):
    rezultatDijeljenjaMandata = Stranka(str(stranka.imeStranke), int(stranka.brojGlasova/mandat), 0)
    listaKolicnika.append(rezultatDijeljenjaMandata)

# Razvrstane stranke po imenu iz liste kolicnika #
# Zatim Uklanjanje duplikata #
for stranka in listaKolicnika:
  imenaStranaka.append(stranka.imeStranke)
imenaStranaka = list(dict.fromkeys(imenaStranaka))

# Sortiranje kolicnika po broju glasova nakon dijeljenje i Definicija zajednickog kolicnika #
listaKolicnika.sort(key=lambda x: x.brojGlasova, reverse=True)
zajednickiKolicnik = listaKolicnika[ukupanBrojMandata-1].brojGlasova

# Dodavanje stranaka u konacnu listu #
for stranka in imenaStranaka:
  r = Stranka(stranka, dobaviGlasovePoImenu(stranka), dobaviBrojOsvojenihMandata(stranka))
  konacnaListaMandata.append(r)

# Ispis u formatu tabele #
konacnaListaStranakatabela = []
nezadovoljavajuciPragTabela = []
for x in konacnaListaMandata:
    lista = [x.imeStranke, x.brojGlasova, x.brojMandata]
    konacnaListaStranakatabela.append(lista)
for x in nezadovoljavajuciPrag:
    lista = [x.imeStranke, x.brojGlasova]
    nezadovoljavajuciPragTabela.append(lista)

print ("")
print ("")
print ("--------- Stranke koje su dobile mandate ---------")
print ("--------------------------------------------------")
print (tabulate(sorted(konacnaListaStranakatabela, key=lambda x: x[1], reverse=True), headers=['Ime stranke', 'Broj glasova', 'Mandati']))