# print("Esercizio: funzione che somma i valori numerici del file 'shampoo_sales.csv'")

def sum_csv(file_name):
    with open(file_name,'r') as my_file:
        values = [] 
        for line in my_file:
            line = line.split(',')
            if line[0] != 'Date': 
                try:
                    values.append(float(line[1]))
                except ValueError: 
                    print('Errore nel convertire il valore:', line[1])
        my_file.close()
    somma = sum(values)
    return somma

file_name = 'shampoo_sales.csv'
print(f'Risultato: {sum_csv(file_name)}')