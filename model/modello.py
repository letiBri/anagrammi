import copy
from time import time
from functools import lru_cache


class Model:
    def __init__(self):
        self.lista_soluzioni = []
        self.set_soluzioni = set()  # con l'insieme non mi mette i doppioni

    # funzione entry point
    def calcola_anagrammi(self, parola: str):  # passo all'editor il fatto che il parametro parola è una stringa
        # vogliamo tenere traccia di tutti gli anagrammi quindi vogliamo salvarli da qualche parte
        # dove passiamo questa collection?
        self.lista_soluzioni = []  # dobbiamo pulire la lista soluzioni per ogni volta che richiamo il metodo con una parola diversa, altrimenti salva TUTTE le sol per ogni parola
        self.set_soluzioni = set()  # lo pulisco
        self._ricorsione("", parola)  # inizialmente la soluzione parziale è la stringa vuota
        # return self.lista_soluzioni
        return self.set_soluzioni  # così mi esclude i doppioni

    # @lru_cache(maxsize=None) # in questo modo salva le copie nella cache e se ne trova una uguale non la rimette
    def _ricorsione(self, parziale, rimanenti):  # ci servono le soluzioni parziali e poi le lettere rimanenti, soluzioni è la collection dove salviamo tutte le sol parziali
        if len(rimanenti) == 0:  # condizione terminale: quando la collection di rimanenti è di lunghezza 0, non posso più formare soluzioni
            #print(parziale)
            #self.lista_soluzioni.append(parziale)
            self.set_soluzioni.add(parziale)  # aggiungo la sol parziale al set
        else:
            # for lettera in rimanenti: # se lavoriamo con stringhe
                # parziale += lettera
                # chiamare la ricorsione con parziale e tutte le lettere rimanenti meno lettera
                # questo metodo non è ottimale, è meglio lavorare con gli indici

            for i in range(len(rimanenti)):
                parziale += rimanenti[i]
                # chiamare la ricorsione con parziale e tutte le lettere rimanenti meno lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]  # prendo tutti gli elementi che rimangono escludendo i
                self._ricorsione(parziale, nuove_rimanenti)
                # mettiamo il backtracking # ogni volta che torniamo indietro dobbiamo togliere la lettera aggiunta nella soluzione parziale
                parziale = parziale[:-1]  # considero tutte le lettere tranne l'ultima


    # soluzione alternativa: utilizzo liste di caratteri e ciclo sulla lista
    def calcola_anagrammi_list(self, parola: str):
        self.lista_soluzioni = []
        self._ricorsione_list([], parola)
        # [ 'd', 'o', 'g' ]
        return self.lista_soluzioni

    # @lru_cache(maxsize=None)
    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            self.lista_soluzioni.append(copy.deepcopy(parziale))  # appendo una copia della soluzione parziale alla lista di soluzioni
        else:
            for i in range(len(rimanenti)):
                parziale.append(rimanenti[i])
                nuove_rimanenti = rimanenti[:i] + rimanenti[i + 1:]
                self._ricorsione_list(parziale, nuove_rimanenti)
                parziale.pop()  # rimuovo l'ultimo elemento, backtracking


if __name__ == '__main__':
    model = Model()
    start_time = time()
    risultato = model.calcola_anagrammi_list("")
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(risultato)

