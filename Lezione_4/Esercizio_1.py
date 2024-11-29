print('Esercizio 1: creare un oggetto CSVFile')

class CSVFile ():
    
    def __init__(self,name):
        
        self.name = name
    
    def __str__(self):
        
        return 'File: "{}"'.format(self.name)
    
    def get_data(self):
        phrases = []
        with open(self.name, 'r') as my_file:
            for line in my_file:
                elements = line.strip().split(',')
                if elements[0] != 'Date':
                    phrases.append(elements)
        return phrases

file = CSVFile('shampoo_sales.csv')
print(f'{file.get_data()}')

    
        