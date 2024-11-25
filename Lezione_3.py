print('Esercizio di prova')
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

print(f'Valori vendite: {sum_csv(values)}')
print('Esercizio 1')

phrases = []  # Initialize a new list to hold phrases
with open('Prova.txt', 'r') as my_file:
    for line in my_file:
        elements = line.strip().split(' ')
        if elements[0] != 'Date':  # Assuming 'Date' is not part of actual text
            phrases.extend(elements)  # Add words to the list

my_word = 'C'

# Function to count occurrences of a letter in a list of phrases
def conta_parole(phrases, my_word):
    count = 0
    for phrase in phrases:
        count += phrase.count(my_word)  # Use .count() for substring matching
    return count

# Printing the result
print(f'La lettera "{my_word}" è stata trovata {conta_parole(phrases, my_word)} volte.')

print('Esercizio 2')
phrases.clear()
with open('Prova.txt', 'r') as my_file:
    for line in my_file:
        elements = line.strip().split(' ')
        if elements[0] != 'Date':
            phrases.extend(elements)

my_word = 'mondo'

def conta_parole(phrases, my_word):
    count = 0
    for word in phrases:
        count += word.count(my_word)
    return count

print(f'La parola "{my_word}" è stata trovata {conta_parole(phrases, my_word)} volte.')
print('Esercizio 3')

