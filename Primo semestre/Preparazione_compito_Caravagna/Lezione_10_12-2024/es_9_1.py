
class Flux():

    def __init__(self,x,delta,y):
        
        self.x = x
        self.delta = delta
        self.y = y

    def __iter__(self):

        return self
    
    def __next__(self):

        if(self.x > self.y):

            raise StopIteration
        else:

            self.x += self.delta
            return (self.x - self.delta)
        
flux = Flux(1,0.5,3)
for i in flux:
    print(i)

