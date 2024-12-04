print('Esercizio 2: estendere l oggetto CSVFile')

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
            print("Errore")
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

class NumericalCSVFile(CSVFile):

    def __init__(self,name):

        super().__init__(name)

    def __str__(self):
        
        return super().__str__
    
    def get_data2(self):

        values = []
        origin_list = super().get_data()
        for line in origin_list:
            if line[0] != 'Date': 
                try:
                    value = float(line[1])
                    values.append([line[0], value])
                except ValueError as e: 
                    print('Errore nel convertire il valore:', line[1])
                    print('La linea verrà saltata')
        return values
    
file = NumericalCSVFile('shampoo_sales.csv')
print(f'{file.get_data2()}')