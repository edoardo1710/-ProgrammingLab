print('Definire una funzione che prende come input un file, rimuove tutte le righe duplicate,scrive il risultato in un nuovo file chiamato unique.txt.')

def openFile(path_file):
    sentences = []
    with open(path_file, 'r') as my_file:
        for line in my_file:
            line = line.replace('?', '.').replace('!', '.')
            elements = line.strip().split('.')
            sentences.extend(elements)
    return sentences

def duplicate(sentences):
    new_sentences = []
    for sentence in sentences:
        frase = sentence
        if frase not in new_sentences:
            new_sentences.append(frase)
        if sentence not in new_sentences:
            new_sentences.append(sentence)
    return new_sentences
            
            

sentences = openFile('Prova.txt')
print(f'{sentences}')
new_sentences = duplicate(sentences)
print(f'{new_sentences}')
# my_file = open('unique.txt', 'a')
# my_file.write(new_sentences)
# my_file.close