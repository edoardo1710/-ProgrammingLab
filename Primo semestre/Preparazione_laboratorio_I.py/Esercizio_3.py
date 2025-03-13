
# https://www.codegrind.it/esercizi/python/classi

print("Esercizio 3: Gestione impiegati")

class ExamException(Exception):
    pass

class Impiegato():

    def __init__(self, name, subname, id, wage):

        if not isinstance(name, str):
            raise ExamException("Il parametro passato come 'nome dipendente' non è del tipo richiesto, ci si aspetta una stringa")
        
        if not isinstance(subname, str):
            raise ExamException("Il parametro passato come 'cognome dipendente' non è del tipo richiesto, ci si aspetta una stringa")
        
        if not isinstance(id, str):
            raise ExamException("Il parametro passato come 'id dipendente' non è del tipo richiesto, ci si aspetta una stringa")
        
        if not isinstance(wage, float):
            raise ExamException("Il parametro passato come 'stipendio dipendente' non è del tipo richiesto, ci si aspetta un valore float")
        
        if wage <= 0:
            raise ExamException("Non pagare un dipendente è scandaloso...vuoi che ti denunci?")
        
        self.name = name
        self.subname = subname
        self.id = id
        self.wage = wage

    def aumenta_stipendio(self, percentuale):

        if percentuale <= 0:
            raise ExamException("Vuoi rovinargli la vita per caso?")
        
        self.wage += (self.wage * percentuale) / 100

    def stampa_dettagli(self):

        return f"Nome: {self.name}, Cognome: {self.subname}, ID: {self.id}, Stipendio attuale: {self.wage}"