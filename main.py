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
# Obzirom da smo sortirali kolicnike po broju glasova, metoda ce sabrati ponavljanja proslijedjene stranke u listi koja je ogranicena brojem dostupnih mandata #
# Na taj nacin dobijamo broj osvojenih mandata za trazenu stranku #
def dobaviBrojOsvojenihMandata(trazenaStranka):
  return sum(s.imeStranke == trazenaStranka for s in listaKolicnika[0:ukupanBrojMandata])

# Definicija Varijabli #
ukupanBrojGlasova = 0
listaUnesenihStranaka = []
nezadovoljavajuciPrag = []
zadovoljavajuciPrag = []
listaKolicnika = []
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

# Ukupan broj glasova #
for stranka in range(0, len(listaUnesenihStranaka)):
  ukupanBrojGlasova = ukupanBrojGlasova + listaUnesenihStranaka[stranka].brojGlasova

# Provjera prelaznog praga od 3% #
for stranka in listaUnesenihStranaka:
  if stranka.brojGlasova < (0.03 * ukupanBrojGlasova):
    nezadovoljavajuciPrag.append(stranka)
  else:
    zadovoljavajuciPrag.append(stranka)

# Lista kolicnika dhondt #
# Glasovi svake stranke se dijele sa 1,3,5,7 itd. dok se mandati ne podijele #
for stranka in zadovoljavajuciPrag:
  for mandat in range(1, ukupanBrojMandata+1, 2):
    rezultatDijeljenjaMandata = Stranka(str(stranka.imeStranke), int(stranka.brojGlasova/mandat), 0)
    listaKolicnika.append(rezultatDijeljenjaMandata)

# Razvrstane stranke po imenu iz liste kolicnika #
for stranka in listaKolicnika:
  imenaStranaka.append(stranka.imeStranke)

# Uklanjanje duplikata #
imenaStranaka = list(dict.fromkeys(imenaStranaka))

# Sortiranje kolicnika po broju glasova nakon dijeljenje (dhondt metoda) #
listaKolicnika.sort(key=lambda x: x.brojGlasova, reverse=True)

# Dodavanje stranaka u konacnu listu #
# Opis metoda se nalazi na pocetku #
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
print ("")
print ("")
print ("---- Stranke koje nisu zadovoljile prag od 3% ----")
print ("--------------------------------------------------")
print (tabulate(sorted(nezadovoljavajuciPragTabela, key=lambda x: x[1], reverse=True), headers=['Ime stranke', 'Broj glasova']))