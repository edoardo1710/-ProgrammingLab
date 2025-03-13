print('Esercizio 4:Definire una funzione conteggio che prende come input un file e ritorna un dizionario con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia con quella parola. Considerare come inizio di frase qualsiasi parola che segue un punto, un punto esclamativo, un punto interrogativo o si trova all inizio del testo') 

def openFile(path_file):
    sentences = []
    with open(path_file, 'r') as my_file:
        for line in my_file:
            line = line.replace('?', '.').replace('!', '.')
            elements = line.strip().split('.')
            sentences.extend(elements)
    return sentences

def conteggio(sentences):
    words = {}
    for sentence in sentences:
        parole = sentence.split(' ')
        if parole[0] not in words.keys():
            words[parole[0]] = 1
        elif parole[0] in words.keys():
            words[parole[0]] +=1
    return words

sentences = openFile('Prova.txt')
print(f'{sentences}')
my_dict = conteggio(sentences)
print(f'{my_dict}')