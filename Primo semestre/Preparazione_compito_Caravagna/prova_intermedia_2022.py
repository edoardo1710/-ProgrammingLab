
class Successione():

    def __init__(self,x,z):
        
        self. x = x
        self.z = z

    def __iter__(self):
        
        self.s_0 = 1
        self.i = 1
        while(self.i < self.x):

            self.s_0 *= 0.5
            self.i += 1
        
        return self
    
    def __next__(self):

        if(self.i > self.z):

            raise StopIteration
        else:

            self.i += 1
            self.s_0 *= 0.5
            return self.s_0
        
successione = Successione(2,5)
for i in successione:
    print(i)