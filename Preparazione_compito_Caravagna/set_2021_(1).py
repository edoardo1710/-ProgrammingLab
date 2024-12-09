# Esercizio B3

class Rettangolo():

    def __init__(self, l, h):
        
        self.l = l
        self.h = h

    def Perimetro(self):

        return 2 * (self.l + self.h)
    
    def Area(self):

        return self.l * self.h
    
    def Display(self):

        print(f"Rettangolo di base {self.l} e altezza {self.h}; il perimetro corrisponde a {self.Perimetro()}, mentre l'area a {self.Area()}")

class Parallelepipedo(Rettangolo):

    def __init__(self, l, h, p):

        self.p = p
        super().__init__(l, h)

    def Volume(self):

        return super().Area() * self.p
    
    def Display(self):
        
        print(f"Parallelepipedo di base {self.l}, altezza {self.p} e profondità {self.h}; il volume corrisponde a {self.Volume()}")

rettangolo = Rettangolo(3,4)
rettangolo.Display()

parallelepipedo = Parallelepipedo(3,4,7)
parallelepipedo.Display()
