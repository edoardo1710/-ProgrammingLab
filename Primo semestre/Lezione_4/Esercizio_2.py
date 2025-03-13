print('Esercizo 2: scrivere una classe denominata veicolo')

class Veicolo():

    def __init__(self,modello,marca,anno,speed):
        
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        
        return 'Modello: "{}"\nMarca: "{}"\nAnno: "{}"\nVelocità: "{}" '.format(self.modello,self.marca,self.anno,self.speed)
    
    def accelerare(self):

        self.speed = self.speed + 5
    
    def frenare(self):

        if self.speed >= 5:
            self.speed = self.speed - 5
    
    def get_speed(self):
        
        return 'Velocità attuale: {}'.format(self.speed)
    
    
veicolo = Veicolo('Topolino supersonica','Fiat','1999','0')
print(veicolo)
veicolo.frenare()
print(f'{veicolo.get_speed()}')



