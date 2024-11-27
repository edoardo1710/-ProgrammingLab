# print('Esercizio 3: creare un dizionario con key le iniziali di ogni parola e value le parole più lunghe che cominciano con quella lettera')

def openFile(path_file):
    phrases = []
    with open(path_file, 'r') as my_file:
        for line in my_file:
            line = line.replace('?', ' ').replace('!', ' ').replace('.',' ')
            elements = line.strip().split(' ')
            phrases.extend(elements)
    return phrases

def word_lenght(phrases):
    words = {}
    for word in phrases:
        if word[0] not in words.keys():
            words[word[0]] = word
        elif len(word) > len(words[word[0]]):
            words[word[0]] = word
    return words

phrases = openFile('Prova.txt')
print(f'{phrases}')
dictionary = word_lenght(phrases)
print(f'{dictionary}')