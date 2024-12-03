# print('Esercizio 1: conta quante volte una lettera è presente nel file')

phrases = []
with open('Prova.txt', 'r') as my_file:
    for line in my_file:
        elements = line.strip().split(' ')
        if elements[0] != 'Date':
            phrases.extend(elements)

# my_word = 'c'

def conta_parole(phrases, my_word):
    count = 0
    for phrase in phrases:
        count += phrase.count(my_word)
    return count

# print(f'La lettera "{my_word}" è stata trovata {conta_parole(phrases, my_word)} volte.')
