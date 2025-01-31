
# https://www.codegrind.it/esercizi/python/classi

print("Esercizio 2: Gestione magazzino")

class ExamException(Exception):
    pass

class GestoreMagazzino:

    def __init__(self, cost):
        """Costruttore

        Parametri:
            cost (float): costo immagazzinaggio di un prodotto
        """

        if not isinstance(cost, float):
            raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta un valore float")
        
        if cost <= 0:
            raise ExamException("Se non costa nulla immagazzinare un prodotto, come pensi che li paghiamo i dipendenti?")
        
        self.prodotti = {}
        self.costo_magazzinaggio = cost

    def aggiungi_prodotto(self, product):
        if product.name not in self.prodotti:
            self.prodotti[product.name] = product

    def rimuovi_prodotto(self, product_name):
        if product_name in self.prodotti:
            del self.prodotti[product_name]

    def calcola_costi_magazzinaggio(self):
        total_cost = 0
        for product in self.prodotti.values():
            total_cost += product.scorta * self.costo_magazzinaggio
        return total_cost

class Prodotto:

    def __init__(self, name, cost, amount):
        """Costruttore

        Parametri:
            name (str): nome del prodotto
            cost (float): costo del prodotto
            amount (int): scorta del prodotto
        """

        if not isinstance(name, str):
            raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta una stringa")
        
        if not isinstance(cost, float):
            raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta un valore float")

        if not isinstance(amount, int):
            raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta un valore intero")
        
        if cost <= 0:
            raise ExamException("Al giorno d'oggi è raro che un prodotto costi zero o meno; sicuro di aver inserito il valore corretto?")
        
        self.name = name
        self.cost = cost
        self.scorta = amount

# Esempio di utilizzo
try:
    prodotto1 = Prodotto("Mela", 1.0, 100)
    prodotto2 = Prodotto("Banana", 0.5, 200)

    magazzino = GestoreMagazzino(0.10)
    magazzino.aggiungi_prodotto(prodotto1)
    magazzino.aggiungi_prodotto(prodotto2)

    print("Costi di magazzinaggio totali:", magazzino.calcola_costi_magazzinaggio(), "€")
except ExamException as e:
    print(e)
