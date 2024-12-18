
class TrendModel():

    def __init__(self):
        
        pass

    def predict(self, data):
        
        if len(data) == 0:

            raise TypeError("Errore, lista vuota")
        
        prev_value = data[0]
        sum = 0
        for i in range(1, len(data), 1):

            print(f"Somma = {sum}, prev_value = {prev_value}")
            sum += (data[i]-prev_value)
            prev_value = data[i]
        
        prediction = prev_value + (sum/(len(data)-1))
        return prediction

model = TrendModel()
print(f"Predizione = {model.predict([8, 19, 31, 41, 50, 52, 60])}") 

            
        






