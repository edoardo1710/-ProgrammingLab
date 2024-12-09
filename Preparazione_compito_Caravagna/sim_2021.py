# Esercizio B3

class SistemaPagamento():

    def __init__(self):

        pass

    def calcola_pagamento(self, impiegati):

        print('Calcolo pagamento')
        print('===================')

        for impiegato in impiegati:

            print("Payroll: ", impiegato.id, ' - ', impiegato.name)
            print("Totale: ", impiegato.calcola_pagamento(), "\n")

class Impiegato(SistemaPagamento):

    def __init__(self, id, name):

        self.id = id
        self.name = name
        super().__init__()

    def calcola_pagamento(self):
        
        pass

class Amministrativi(Impiegato):

    def __init__(self, id, name, salario):

        self.salario = float(salario)
        super().__init__(id, name)

    def calcola_pagamento(self):
        
        return self.salario
    
class ImpiegatiOre(Impiegato):

    def __init__(self, id, name, tariffa, ore):

        self.tariffa = float(tariffa)
        self.ore = float(ore)
        super().__init__(id, name)

    def calcola_pagamento(self):
        
        return self.tariffa * self.ore
    
class ImpiegatiCommissione(Impiegato):

    def __init__(self, id, name, salario, commissione):

        self.salario = float(salario)
        self.commissione = float(commissione)
        super().__init__(id, name)

    def calcola_pagamento(self):
        
        return self.salario + self.commissione
    
impiegato_1 = ImpiegatiCommissione("c3129", "Tonio Cartonio", " 420", "69")
impiegato_2 = ImpiegatiOre("o2139", "Thomas Turbato", "18", "35")
impiegato_3 = Amministrativi("a2146", "Checco Lione", "870.31")

sistema_pagamento = SistemaPagamento()
sistema_pagamento.calcola_pagamento([impiegato_1, impiegato_2, impiegato_3])