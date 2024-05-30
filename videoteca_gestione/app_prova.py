from flask import Flask, render_template, request
from film import Film
from videoteca import Videoteca

# creo un'istanza di Flask
app= Flask(__name__)

# creo un'istanza di Videoteca
videoteca = Videoteca()

# creo percorso per la web app
@app.route('/')
def index():
    return render_template('index.html') # render_template usata per 'riprodurre' un template HTML
                                         # il template HTML è separato dalla 'logica' .py, in questo caso
                                         # si trova nella directory "templates"

@app.route('/aggiungi_film', methods=['POST'])
def aggiungi_film():
    titolo = request.form['titolo']
    regista = request.form['regista']
    anno_uscita = int(request.form['anno_uscita'])
    nuovo_film = Film(titolo, regista, anno_uscita)
    videoteca.aggiungiFilm(nuovo_film)
    return 'Il film è stato aggiunto con successo!'

@app.route('/catalogo_film')
def catalogo_film():
    catalogo = videoteca.getListaFilm()
    return render_template('catalogo.html', catalogo=catalogo)

@app.route('/cerca_film', methods=['GET'])
def cerca_film():
    titolo= request.args.get('titolo')
    regista= request.args.get('regista')
    film_trovati= [film for film in videoteca.getListaFilm() if (titolo and film.getTitolo() == titolo) or (regista and film.getRegista() == regista)]
    return render_template('risultati_ricerca.html', film_trovati=film_trovati)

@app.route('/rimuovi_film', methods=['POST'])
def rimuovi_film():
    titolo= request.form['titolo']
    videoteca.rimuoviFilm(titolo)
    return 'Il film è stato rimosso con successo!'

@app.route('/noleggia_film', methods=['POST'])
def noleggia_film():
    titolo= request.form['titolo'] 
    videoteca.noleggiaFilm(titolo)
    return 'Il film è noleggiato. Enjoy!'

@app.route('/restituisci_film', methods=['POST'])
def restituisci_film():
    titolo = request.form['titolo']
    film_trovato = False
    for film in videoteca.getListaFilm():
        if film.getTitolo().lower() == titolo.lower():
            videoteca.restituisciFilm(titolo)
            film_trovato = True
            break
    if film_trovato:
        return 'Film restituito con successo!'
    else:
        return 'Il film non è stato trovato nel catalogo.'


if __name__ == '__main__':
    app.run(debug=True)