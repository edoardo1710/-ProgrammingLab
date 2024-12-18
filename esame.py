
class ExamException():

    pass

class MovingAverage():

    def __init__(self, window):
        
        if not isinstance(window, int):

            raise ExamException("Errore, il valore della finestra deve essere un intero")
        if window <= 0:

            raise ExamException("Errore, il valore della finestra non può essere minore o uguale a zero")

        self.window = window
    
    def media (self, data):

        return sum(data) / len(data)

    def compute (self, data):

        if not isinstance(data, list):

            raise ExamException("Errore, il dato fornito non è una lista")
        if len(data) == 0:

            raise ExamException("Errore, la lista è vuota")
        if not all(isinstance(x, (int, float)) for x in data):

            raise ExamException("Errore, la lista contiene valori non numerici")
        if self.window == 1:

            return data
        if self.window > len(data):

            raise ExamException("Errore, la finestra è più grande della lista di dati")
        
        medie_mobile = []
        for i in range(len(data) - self.window + 1):

            medie_mobile.append(self.media(data[i:i+self.window]))
        
        return medie_mobile
        
# elementi = MovingAverage(2)
# print(f"Media mobile = {elementi.compute([2,4,8,16])}")



            

    