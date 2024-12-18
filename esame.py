
class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, window):        
        """Costruttore.

        params:
            window (int) : dimensione della finestra per la media mobile

        raises:
            se window non appartiene ai naturali
        """
        
        if not isinstance(window, int):
            raise ExamException("Errore, il valore della finestra deve essere un numero naturale")
        
        if window <= 0:
            raise ExamException("Errore, il valore della finestra non essere minore o uguale a zero")

        self.window = window
    
    def media (self, data):
        return float(sum(data)) / float(len(data))

    def compute (self, data):
        
        if not isinstance(data, list):
            raise ExamException("Errore, il dato fornito non è una lista")
        
        for x in data:
            if not isinstance(x, (int, float)):
                raise ExamException("Errore, la lista contiene valori non numerici")
        
        if len(data) == 0:
            raise ExamException("Errore, la lista è vuota")
        
        if self.window == 1:
            return data

        if self.window > len(data):
            raise ExamException("Errore, la finestra è più grande della lista di dati")
        
        medie_mobile = []

        for i in range(len(data) - self.window + 1):
            medie_mobile.append(self.media(data[i : i + self.window]))
        
        return medie_mobile
        

#elementi = MovingAverage()
# print(f"Media mobile = {elementi.compute([2,4,8,16])}")