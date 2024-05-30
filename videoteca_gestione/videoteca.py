from typing import Any
from film import Film

class Videoteca():
    def __init__(self):
        self._catalogo = []
    
    def getListaFilm(self):
        return self._catalogo
    
    # metodi classe Videoteca
    def aggiungiFilm(self, film: Film):
            self._catalogo.append(film)
            print(f"Il film '{film.getTitolo()}' è stato aggiunto!")

    def rimuoviFilm(self, titolo: str):
        self._catalogo = [film for film in self._catalogo if film.getTitolo().lower() != titolo.lower()]
        print(f"Il film '{titolo}' è stato rimosso!")
        

    def cercaFilm(self, titolo: str = None, regista: str = None):
        film_trovato = False
        for film in self._catalogo:
            if film.getTitolo() == titolo or film.getRegista() == regista:
                print(film)
                film_trovato = True
                break
        if not film_trovato:
            print(f"Il film '{titolo}' di {regista} non è stato trovato. Riprova.")
    
    def noleggiaFilm(self, titolo: str):
        film_trovato = False
        for film in self._catalogo:
            if film.getTitolo() == titolo:
                if film.getDisponibilità():
                    film.setDisponibilità(False)
                    print(f"Il film '{titolo}' adesso è stato noleggiato.")
                    film_trovato = True
                    break
        if not film_trovato:
            print(f"Il film '{titolo}' non è disponibile per il noleggio.\nE' già noleggiato o non è presente nel catologo.\nRiprova!")

    def restituisciFilm(self, titolo: str):
        film_trovato = False
        for film in self._catalogo:
            if film.getTitolo() == titolo:
                film.setDisponibilità(True)
                print(f"Il film '{titolo}' è stato restituito.")
                film_trovato = True
                break
        if not film_trovato:
            print(f"Il film '{titolo}' è noleggiato o non è presente nel catologo.")

    def mostraCatalogoFilm(self):
        print("Film disponibili:")
        disponibili = [film for film in self._catalogo if film.getDisponibilità()]
        if disponibili:
            for film in disponibili:
                print(film)
        else:
            print("Nessun film disponibile al momento.")