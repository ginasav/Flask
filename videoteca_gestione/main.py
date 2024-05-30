from typing import Any
from film import Film
from videoteca import Videoteca


videoteca_nuova = Videoteca()


film1 = Film(titolo= "LaLaLand",
            regista= "Damien Chazelle",
            anno_uscita= 2016)

film2 = Film(titolo= "Nuovo Cinema Paradiso",
            regista= "Giuseppe Tornatore",
            anno_uscita= 1988)

film3 = Film(titolo= "The Lobster",
            regista= "Yorgos Lanthimos",
            anno_uscita= 2015)

videoteca_nuova.aggiungiFilm(film1)
videoteca_nuova.aggiungiFilm(film2)
videoteca_nuova.aggiungiFilm(film3)


def cercaFilminCatalogo(videoteca_nuova):
    input_utente= input("Inserisci il titolo o il regista del film che stai cercando: ")
    while input_utente:
        print ("Sta cercando...")
        videoteca_nuova.cercaFilm(input_utente)
        break

# print()
# print("Sto rimuovendo...")
# videoteca_nuova.rimuoviFilm("The Lobster")


# print()
# print("--------------------")
# videoteca_nuova.noleggiaFilm("Napoli velata")

# print()
# print("---------------------")
# videoteca_nuova.restituisciFilm("The Lobster")

# print()
# print("---------------------")
# videoteca_nuova.mostraCatalogoFilm()

if __name__ == "__main__":
    cercaFilminCatalogo(videoteca_nuova)