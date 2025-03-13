print('Esercizio 1: modificare l oggetto CSVFile')

class CSVFile ():
    
    def __init__(self,name):
        
        self.name = name
    
    def __str__(self):
        
        return 'File: "{}"'.format(self.name)
    
    def get_data(self):

        try:
            file_parametro = open(self.name)
            parametro_come_stringa = file_parametro.read()
        except FileNotFoundError as e:
            print("File non trovato")
            print("Verrà utilizzato il file 'shampoo_sales.csv'")
            phrases = []
            with open('shampoo_sales.csv', 'r') as my_file:
                for line in my_file:
                    elements = line.strip().split(',')
                    if elements[0] != 'Date':
                        phrases.append(elements)
            return phrases
        else:
            phrases = []
            with open(self.name, 'r') as my_file:
                for line in my_file:
                    elements = line.strip().split(',')
                    if elements[0] != 'Date':
                        phrases.append(elements)
            return phrases

file = CSVFile('shampoo_sales.csv')
print(f'{file.get_data()}')
