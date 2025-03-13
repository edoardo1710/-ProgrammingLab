# Esercizio B3

class Obj():

    def __init__(self,a,b,c):
        
        self.a = a
        self.b = b
        self.c = c

    def eval(self,x):
        
        return self.a*(x**2) + self.b*x + self.c
    
class o1(Obj):

    def __init__(self):
        super().__init__(a=1, b=2, c=0)

    def eval(self,x):
        return super().eval(x)
    
class o2(Obj):

    def __init__(self):
        super().__init__(a=1, b=2, c=-1)

    def eval(self,x):
        return super().eval(x)

f1 = o1()
print(f"{f1.eval(41)}") # 1763

f2 = o2()
print(f"{f2.eval(73)}") # 5474