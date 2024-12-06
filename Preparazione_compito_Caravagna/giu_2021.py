# Esercizio B3

class Veicolo():

    def __init__(self,p,v,km):
        
        self.posti = p
        self.velocità = v 
        self.km = km

# Sottoclasse Auto4 (4 posti)
class Auto4(Veicolo):
    def __init__(self, km=0):
        super().__init__(p=4, v=120, km=km)  # Presupponendo velocità massima predefinita di 120 km/h

# Sottoclasse Auto5 (5 posti)
class Auto5(Veicolo):
    def __init__(self, km=0):
        super().__init__(p=5, v=120, km=km)  # Presupponendo velocità massima predefinita di 120 km/h

# Sottoclasse Bus_90 (velocità massima 90 km/h)
class Bus_90(Veicolo):
    def __init__(self, km=0):
        super().__init__(p=50, v=90, km=km)  # Presupponendo 50 posti per il bus

# Sottoclasse Bus_130 (velocità massima 130 km/h)
class Bus_130(Veicolo):
    def __init__(self, km=0):
        super().__init__(p=50, v=130, km=km)  # Presupponendo 50 posti per il bus

