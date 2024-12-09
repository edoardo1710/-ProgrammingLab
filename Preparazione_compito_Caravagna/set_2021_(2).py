# Esercizio B3

class C1():

    def __init__(self,i):
        
        self.i = i

    def quadrato(self):

        return self.i**2
    # Il metodo "quadrato" va realizzato nella classe C1 poiché successivamente potrà essere ereditato dalla C2

class C2(C1):

    def __init__(self, i):
        
        super().__init__(i)
    