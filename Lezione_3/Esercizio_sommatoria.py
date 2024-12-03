# print('Esercizio di prova: definire una funzione che sommi i valori di tutte le vendite presenti nel file')

values = []
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    elements = line.strip().split(',')
    if elements[0] != 'Date':
        date = elements[0]
        value = float(elements[1])
        values.append(value)
my_file.close()

def sum_csv(values):
    total = 0
    for i in values:
        total += i
    return total

# print(f'Valori vendite: {sum_csv(values)}')