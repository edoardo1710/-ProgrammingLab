
import Model as m
# import matplotlib.pyplot as plt

class TrendModel(m.Model):

    def control(self, data):
        
        if len(data) == 0:

            raise TypeError("Errore, lista vuota")

    def compute_avg_variation(self, data):

        prev_value = None
        variazioni = []
        for item in data:

            if prev_value is not None:

                variazioni.append(item - prev_value)
            prev_value = item
        
        media_var = sum(variazioni)/len(variazioni)
        return media_var
    
    def predict(self, data):
        
        self.control(data)
        prediction = data[-1] + self.compute_avg_variation(data)
        return prediction

class FitTrendModel(TrendModel):

    def __init__(self, n):

        super().__init__(n)

    def fit(self, data):

        self.historical_avg_variation = self.compute_avg_variation(data)

    def predict(self, data):

        self.control(data)
        prediction = data[-1] + (self.compute_avg_variation(data) + self.historical_avg_variation) / 2
        return prediction
    






        
        
    



        
        
        
        

        

