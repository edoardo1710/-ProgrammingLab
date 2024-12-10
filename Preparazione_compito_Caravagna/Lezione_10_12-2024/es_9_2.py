
class Prime():

    def __init__(self,list):
        
        self.list = list

    def is_Prime(self, num):

        for i in range(num,1,-1):

            if(num % i == 0):

                return False
        
        return True

    def __iter__(self):
        
        self.i = 0
        return self
    
    def __next__(self):

        while(self.i < len(self.list)):

            number = int(self.list[self.i])
            self.i +=1
            if self.is_Prime(number):

                return number
            
        raise StopIteration
        
lista = Prime("[10,15,3,7,12,19,4]")
for i in lista:
    print(i)



        

        
        
    



                



            



