
class Model():

    def __init__(self, n):
        
        self.window = n

    def fit (self, data):

        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')
    
    def evaluate(self, data):

        fit_len = int(0.7 * len(data))
        data_fit = data[:fit_len]
        data_test = data[fit_len:]
        
        try:

            self.fit(data_fit)
        except Exception as e:

            if isinstance(e,NotImplementedError):
                pass
            else:
                raise Exception('Il metodo fit è implementato ma' +
                'ha sollevato una eccezione {}'.format(e))

        errors = []
        for i in range(len(data_test) - self.window):

            predict_value = self.predict(data_test[i:i+self.window])
            errors.append(abs(predict_value - data_test(self.window + i)))

        mae_error = sum(errors) / len(errors)
        return mae_error


        
    
