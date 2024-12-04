
class InvalidName(Exception):
    pass

class CSVFile ():
    
    def __init__(self,name):
        
        self.name = name
        if not isinstance(self.name,str):
            raise InvalidName('Stupidino')
    
    def __str__(self):
        
        return 'File: "{}"'.format(self.name)
    
    def get_data(self,start,end):

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
            phrases_def = []
            pos = 0
            for elements in phrases:
                if pos>start and pos<end:
                    phrases_def.append(elements)
                pos += 1 
            return phrases_def
        else:
            phrases = []
            with open(self.name, 'r') as my_file:
                for line in my_file:
                    elements = line.strip().split(',')
                    if elements[0] != 'Date':
                        phrases.append(elements)
            phrases_def = []
            pos = 0
            for elements in phrases:
                if pos>=start and pos<=end:
                    phrases_def.append(elements)
                pos += 1 
            return phrases_def
    
file = CSVFile('shampoo_sales.csv')
print(f'{file}')
start_str = input('Inserisci la partenza: ')
start = int(start_str)
end_str = input("Inserisci l'arrivo: ")
end = int(end_str)
if end<start:
    raise Exception("Il valore della partenza deve essere minore di quello dell'arrivo")
elif start<0
    raise Exception("Valore di partenza indefinito")
# elif end>fil
print(f'{file.get_data(start,end)}')