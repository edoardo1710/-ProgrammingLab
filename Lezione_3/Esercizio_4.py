# print('Esercizio 4:Definire una funzione conteggio che prende come input un file e ritorna un dizionario con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia con quella parola. Considerare come inizio di frase qualsiasi parola che segue un punto, un punto esclamativo, un punto interrogativo o si trova all inizio del testo') 


def openFile(path_file):
    sentences = []
    with open(path_file, 'r') as my_file:
        for line in my_file:
            elements = line.strip().split('.')
            sentences.extend(elements)
    return sentences

def dividi(sentences):
    processed_sentences = []
    for sentence in sentences:
        sentence = sentence.rstrip('!?')
        processed_sentences.append(sentence)
    return processed_sentences

sentences = openFile('Prova.txt')
print(f'{sentences}')
processed_sentences = dividi(sentences)
print(f'{processed_sentences}')