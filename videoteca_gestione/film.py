class Film ():
    def __init__(self, titolo: str,
                 regista: str,
                 anno_uscita: int):
        self._titolo = titolo
        self._regista = regista
        self._anno_uscita = anno_uscita
        self._disponibile = True

    def getTitolo(self):
        return self._titolo
    
    def getRegista(self):
        return self._regista
    
    def getAnnoUscita(self):
        return self._anno_uscita
    
    def getDisponibilità(self):
        return self._disponibile
        
    def setDisponibilità(self, 
                         nuova_disponibilità= bool):
        self._disponibile= nuova_disponibilità

    def __str__(self) -> str:
        return f"{self._titolo} di {self._regista} ({self._anno_uscita}) - {'Disponibile' if self._disponibile else 'Non disponibile'}"
    

