
# https://www.programmareinpython.it/esercizi-python/

print("Esercizio 1: Il Linguaggio dei Furfanti")

class GeneralException(Exception):
    pass

def is_vocal(letter):
    """Funzione 'is_vocal'

    Parametri:
        letter (elemento di stringa): lettera in esame
    
    Output:
        False se la lettera è vocale, True altrimenti
    """

    if (letter == "a") or (letter == "e") or (letter == "i") or (letter == "o") or (letter == "u"):
        return False
    else:
        return True

def rövarspråket_transaltor(string):
    """Funzione 'rövarspråket_transaltor'

    Parametri:
        string (str): stringa in esame

    Output:
        new_string (str): stringa convertita
    """

    # Controllo se 'string' è effettivamente una stringa
    if not isinstance(string, str):
        raise GeneralException("L'input iserito non è una stringa")
    
    # Riduzione e minuscola di tutte le lettere di 'string'; creazione di 'string_list', che verrà poi convertita a stringa
    string = string.lower()
    string_list = []

    for letter in string:

        # Controllo se 'letter' è effettivamente una lettera
        if letter.isalpha() is False:
            raise GeneralException(f"Il carattere preso in esame ({letter}) non è una lettera")
        
        # Se 'letter' è una consonante viene aggiunto a 'string_list' la lettera, la vocale 'o' e di nuovo la lettera, altrimenti solo la lettera
        if is_vocal(letter) is True:
            string_list.append(letter)
            string_list.append("o")
            string_list.append(letter)
        else:
            string_list.append(letter)

    # 'new_string' è la stringa creata da 'string_list' attraverso il metodo '.join()'
    string_list[0] = string_list[0].upper() 
    new_string ="".join(string_list)

    return new_string

# Ciclo per l'inserimento dell'input
while True:
    string = input("Inserire la parola da convertire: ")
    print("Elaborazione...")
    print(f"Stringa convertita: {rövarspråket_transaltor(string)}")

    i = str(input("Si desidera continuare? ")).upper()

    # Entra nel ciclo se la risposta è diversa da 'si' o 'no'
    if (i != "SI") or (i != "NO"):
        
        while (i != "SI") and (i != "NO"):
            i = input("Risposta non accettata. \n Inserire una risposta valida: ").upper()

    if (i == "NO"):
        break
