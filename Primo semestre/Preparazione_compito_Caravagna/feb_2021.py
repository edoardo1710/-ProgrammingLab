# Esercizio B3

class myPower():

    def __init__(self,a):
        
        self.a = a
        self.somma = 0
    
    def __iter__(self):

        self.n = 1
        return self
    
    def __next__(self):

        if self.n > self.a:
            raise StopIteration
        else:
            self.n += 1
            self.somma += 3**((self.n-1)+1)/(self.n-1) 
            return 3**((self.n-1)+1)/(self.n-1)
        
    def mean_pow_a(self):

        return self.somma/(self.n-1)
        

numbers = myPower(3)
for i in numbers:
    print(i)
media = numbers.mean_pow_a()
print("{}".format(media))