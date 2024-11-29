print('Esercizio 3: creare una sottoclasse "Auto" e una "Moto"')

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

class Auto(Veicolo):

    def __init__(self,modello,marca,anno,speed,numero_porte):
        
        super().__init__(modello,marca,anno,speed)
        self.numero_porte = numero_porte

    def __str__(self):

        return super().__str__() + '\nNumero porte: "{}"'.format(self.numero_porte)

class Moto(Veicolo):

    def __init__(self,modello,marca,anno,speed,tipo):

        super().__init__(modello,marca,anno,speed)
        self.tipo = tipo

    def __str__(self):

        return super().__str__() + '\nTipo: "{}"'.format(self.tipo)

moto = Moto('Topolino supersonica','Fiat','1999','0','Sportiva')
print(moto)