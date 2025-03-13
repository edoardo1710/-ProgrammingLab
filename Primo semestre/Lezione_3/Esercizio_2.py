print('Esercizio 2: Definire una funzione che prende come input un file e conta quante volte ogni parola è presente')

import re

def openFile(path_file):
    phrases = []
    with open(path_file, 'r') as my_file:
        for line in my_file:
            elements = re.findall(r'\b\w+\b', line)
            phrases.extend(elements)
    return phrases

def counter(phrases,my_word):
    count = 0
    for phrase in phrases:
        if phrase == my_word:
            count += 1
    return count

phrases = openFile('Prova.txt')
my_word = 'mondo'
print(f'La parola "{my_word}" è presente nel file {counter(phrases,my_word)} volte')
