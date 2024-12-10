
class EvaluateFunction():

    def __init__(self,a,b,n):
        
        self.a = a
        self.b = b
        self.n = n
        self.i = 1
        self.delta = (self.b - self.a)/(self.n-1)

    def __iter__(self):

        return self
    
    def __next__(self):

        if(self.i > self.n):

            raise StopIteration
        
        else:

            self.i += 1
            return (self.a + ((self.i-1) -1) * self.delta)**2
        
funct = EvaluateFunction(0,2,5)
for i in funct:
    print(i)