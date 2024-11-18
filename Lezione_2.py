print('Esercizio 1')
print('Lequivalente di {A} minuti è {B}h:{C}min'.format(A=538,B=12,C=32))
print('Esercizio 2')
my_p = 'a'
my_word = "abba"

def conta_lettere(my_p, my_word):
    my_val = 0
    for i in my_word:
        if i == my_p:  
            my_val += 1
    print(f'La lettera "{my_p}" è contenuta {my_val} volte in "{my_word}"')

conta_lettere(my_p, my_word)

print('Esercizio 3')
def palindromo(my_word):
        for i in range(len(my_word)//2):
             if my_word[i]!=my_word[-(i + 1)]:
                  return False
        return True

if palindromo(my_word)==False:
     print(f'La stringa "{my_word}" non è palindroma')
else:
     print(f'La stringa "{my_word}" è palindroma')

print('Esercizio 4')
my_l1 = 3
my_l2 = 2
my_l3 = 1
def triangolo(my_l1,my_l2,my_l3):
     if (my_l1+my_l2>my_l3) and (my_l1+my_l3>my_l2) and (my_l2+my_l3>my_l1):
          if my_l1==my_l2==my_l3:
               print('Il triangolo è equilatero')
          elif(my_l1==my_l2) or (my_l1==my_l3) or (my_l2==my_l3):
               print('Il triangolo è iscoscele')
          else:
               print('Il triangolo è scaleno')
     else:
        print('I lati non possono formare un triangolo')

triangolo(my_l1,my_l2,my_l3)
          
print('Esercizio 5')
my_list = [1,2,3,4,5]
i = 3
j = 7
def scambio(my_list,i,j):
     if (i<len(my_list)) and ((j<len(my_list))):
          scamb = my_list[i]
          my_list[i] = my_list[j]
          my_list[j] = scamb
     else:
          print('Valori inseriti non validi')
     return my_list

print(f'Vecchia lista: "{my_list}"; nuova lista: "{scambio(my_list,i,j)}"')

print('Esercizio 6')
my_numb = 0
def factorial(my_numb):
     if (my_numb==0): return 1
     else: return my_numb*(factorial(my_numb-1))

print(f'Valore del fattoriale di {my_numb} = {factorial(my_numb)}')

print('Esercizio 7')
my_list2 = [6,7,8,9,10,11,12]
def ricorrenza_list(my_list, my_list2):
    if len(my_list2) > len(my_list):
        my_list, my_list2 = my_list2, my_list
    
    for i in my_list2:
        if i in my_list:
            return True
    return False

if (ricorrenza_list(my_list,my_list2)==False):
     print('Le due liste non hanno ricorrenze')  
else:
     print('Le due liste hanno ricorrenze')  
  
print('Esercizio 8')
my_list3 = [1,1,1,2]
def danum_alet(my_list3):
    for index in range(len(my_list3)):  # Loop over the indices
        if my_list3[index] == 1:
            my_list3[index] = 'uno'
        elif my_list3[index] == 2:
            my_list3[index] = 'due'
        elif my_list3[index] == 3:
            my_list3[index] = 'tre'
        elif my_list3[index] == 4:
            my_list3[index] = 'quattro'
        elif my_list3[index] == 5:
            my_list3[index] = 'cinque'
        elif my_list3[index] == 6:
            my_list3[index] = 'sei'
        elif my_list3[index] == 7:
            my_list3[index] = 'sette'
        elif my_list3[index] == 8:
            my_list3[index] = 'otto'
        elif my_list3[index] == 9:
            my_list3[index] = 'nove'
    return my_list3

print(f'Valori numerici: {my_list3}; valori in lettera: {danum_alet(my_list3)}')