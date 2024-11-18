print('Esercizio 1')
print('Lequivalente di {A} minuti è {B}h:{C}min'.format(A=538,B=12,C=32))
print('Esercizio 2')
my_p = 'a'
my_word = "abcdeaaaaa"

def conta_lettere(my_p, my_word):
    my_val = 0
    for i in my_word:
        if i == my_p:  
            my_val += 1
    print(f'La lettera "{my_p}" è contenuta {my_val} volte in "{my_word}"')

conta_lettere(my_p, my_word)