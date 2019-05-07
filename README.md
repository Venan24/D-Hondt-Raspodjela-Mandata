# Primjena D'Hondt u glasanju FBiH

## Raspodjela mandata u Skupstinama kantona u FBiH
Sama metoda je modificirana jer se u izvornoj metodi svi glasovi dijele na 1,2,3,4,5 i tako redom. Zatim se uzima n-ti clan koji je jednak broju dostupnih mandata i to je zajednicki djeljutelj. Zatim se mandati racunaju na princip Ukupan broj glasova stranke / n-ti clan = broj osvojenih mandata.

## Princip rada po nasem Izbornom zakonu
* Glasovi svih stranaka se dijele sa 1,3,5,7 itd. do broja dostupnih mandata i ta lista se naziva Kolicnici
* Novu listu Kolicnici sortiramo po varijabli broj glasova (nakon dijeljenja sa 1,3,5,7...)
* Ukoliko imamamo 7 mandata za podjelu. Uzimamo prvih 7 clanova te sortirane liste i izbrojimo koliko se puta neka stranka ponavlja unutar te liste
* Dobijeni broj je broj osvojenih mandata za tu stranku

## Simulacija
![](https://media.giphy.com/media/cjKo7rD3ELLbjmO29S/giphy.gif)