# Esercizio B3

class Function():

    def __init__(self,N):
        
        self.N = N
    
    def eval(self):

        pass

    def f_hat(self,a,b):

        delta = (b-a)/self.N
        sum = 0
        for i in range(self.N):

            sum += self.eval(a+i*delta)
        
        return sum/self.N
    
class F_1(Function):

    def __init__(self, N):
        super().__init__(N)

    def eval(self,x):
        
        return x**2+2*x
    
    def f_hat(self, a, b):
        return super().f_hat(a, b)
    
funzione = F_1(3)
print(f"{funzione.f_hat(0,6)}")
