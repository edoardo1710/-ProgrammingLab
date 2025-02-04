
class ExamException(Exception):
    pass

class AnalizzatoreVendite():

    def __init__(self, file_name):
        """Costruttore

        Parametri:
            file_name (str): pathe del file 'vendite.csv'
        """

        # Controllo se il nome del file vine passato come stringa
        if not isinstance(file_name, str):
            raise ExamException(f"Il parametro inserito non è del tipo richiesto, bensì del tipo '{type(file_name)}'; ci si aspetta una stringa (pathe del file)")
        
        self.file_name = file_name
    
    def carica_dati(self):
        """Metodo 'carica_dati'
        
        Output:
            vendita (list): lista di liste contenente le righe del file
        """

        # Controllo se il file è apribile e leggibile
        try:
            with open(self.file_name, 'r') as file:
                data = file.read().splitlines()
        except FileNotFoundError:
            raise ExamException("Errore nell'apertura del file")
        except IOError:
            raise ExamException("Errore nella lettura del file")
        
        vendita = []

        for line in data:
            elements = line.strip().split(',')

            if elements[0] != 'ID':

                # Se la riga è vuota non verrà aggiunta a 'vendita'
                if line:
                    
                    # Controllo se l'ID è un numero intero maggiore di zero
                    try:
                        ID = int(elements[0])

                        if ID <= 0:
                            raise ExamException("L'ID dev'essere rappresentato da un numero maggiore di zero")
                    except ValueError:
                        raise ExamException(f"L'ID dell'elemento in analisi ({elements[0]}) non è valido")
                    
                    # Controllo se il nome del prodotto è una stringa non numerica, quindi se rappresenta un prodotto valido
                    if not isinstance(elements[1], str) or elements[1].isdigit():
                        raise ExamException(f"Il prodotto inserito all'ID {ID} non è valido")
                    
                    # Controllo se la quantità è un numero intero maggiore o uguale a 0
                    try:
                        Quantità = int(elements[2])

                        if Quantità < 0:
                            raise ExamException("La quantità del prodotto dev'essere un numero intero maggiore o uguale a 0")
                    except ValueError:
                        raise ExamException(f"La quantità inserità per il prodotto '{elements[1]}' non è valida")
                    
                    # Controllo se il prezzo è un numero reale maggiore o uguale a 0
                    try:
                        Prezzo = float(elements[3])

                        if Prezzo < 0:
                            raise ExamException("Il prezzo del prodotto dev'essere un numero intero maggiore o uguale a 0")
                    except ValueError:
                        raise ExamException(f"Il prezzo inserito per il prodotto '{elements[1]}' non è valido")
                    
                    # Controllo che la data sia sottoforma di stringa
                    if not isinstance(elements[4], str):
                        raise ExamException(f"La data inserita all'ID {ID} non è valida")
                    
                    # Controllo se l'anno è un numero intero maggiore o uguale a 2000 (qui ipotizziamo che il file tenga conto delle vendita a partire dal 2000)
                    try:
                        year = int(elements[4][:4])

                        if year < 2000:
                            raise ExamException("Il file tiene conto delle vendite dopo il 2000")
                    except ValueError:
                        raise ExamException(f"Il valore inserito per l'anno ({elements[4][:4]}) non è valido")

                    # Controllo se ci sono '-' per separare gli indicatori temporali (YYYY,MM,DD)
                    if (elements[4][4] != '-') or (elements[4][7] != '-'):
                        raise ExamException("Per separare i vari indicatori temporali (YYYY,MM,DD) deve esserci '-', mentre in questo caso non è così")
                    
                    # Controllo se il mese è un numero intero compreso tra 1 e 12
                    try:
                        month = int(elements[4][5:7])

                        if (month < 1) or (month > 12):
                            raise ExamException(f"Il mese inserito ({month}) non esiste")
                    except ValueError:
                        raise ExamException(f"Il valore inserito per il mese ({elements[4][5:7]}) non è valido")
                    
                    # Controllo se il giorno è un numero intero
                    try:
                        day = int(elements[4][8:10])

                        # Controllo se il giorno è valido, cioè compreso tra 1 e 31
                        if (day < 1) or (day > 31):
                            raise ExamException(f"Il giorno inserito ({day}) non esiste")
                        
                        # Controllo se il giorno esiste nei mesi con 30 giorni e non 31
                        if ((month == 4) or (month == 6) or (month == 9) or (month == 11)) and day > 30:
                            raise ExamException(f"Il mese corrispondente non ha più di 30 giorni")
                        
                        # Controllo se fabbraio ha massimo 29 giorni e se negli anni bisestili ne ha 28
                        if (month == 2) and (day > 29):
                            raise ExamException("Il mese di febbraio non ha più di 29 giorni")
                        elif (year % 4 != 0) and (month == 2) and (day > 28):
                            raise ExamException("Il mese di febbraio ha 29 giorni solo negli anni bisestili")
                    except ValueError:
                        raise ExamException(f"Il valore inserito per il mese ({elements[4][5:7]}) non è valido")
                    
                    vendita.append([ID,elements[1],Quantità,Prezzo,elements[4]])

        return vendita
    
    def totale_per_prodotto(self, lista_vendite):
        """Metodo 'totale_per_prodotto'

        Parametri:
            lista_vendite (list): lista con tutte le vendite

        Output:
            messaggio a schermo con il totale delle vendite per ogni prodotto
        """
        
        # 'vendita_dict' è un dizionario con all'interno le vendite totali per ogni prodotto
        vendita_dict = {}

        for item in lista_vendite:

            if item[1] not in vendita_dict.keys():
                vendita_dict[item[1]] = (item[2] * item[3])
            else:
                vendita_dict[item[1]] += (item[2] * item[3])
        
        # Il dizionario viene riordinato a seconda del valore delle vendite
        sorted_by_values = dict(sorted(vendita_dict.items(), key=lambda item: item[1]))

        print("Totale vendite per prodotto: ")
        for k,v in sorted_by_values.items():
            print(f"{k}: €{v}")

    def incasso_totale(self, lista_vendite):
        """Metodo 'incasso_totale'

        Parametri:
            lista_vendite (list): lista con tutte le vendite

        Output:
            messaggio a schermo con il totale delle vendite del negozio
        """
        
        # In 'incasso_totale' sarà conservato il valore totale delle vendite del negozio
        incasso_totale = 0

        for item in lista_vendite:
            incasso_totale += (item[2] * item[3])

        print(f"Incasso totale: €{incasso_totale}")
                    
name = "vendite.csv"
analizzatore = AnalizzatoreVendite(name)
lista_vendite = analizzatore.carica_dati()

for item in lista_vendite:
    print(f"{item}")

analizzatore.totale_per_prodotto(lista_vendite)
analizzatore.incasso_totale(lista_vendite)
                    

                    

                    
