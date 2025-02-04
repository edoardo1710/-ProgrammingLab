
class ExamException(Exception):
    pass

class FinancialAnalyzer():

    def __init__(self, transactions):
        """Costruttore

        Attributi:
            transactions (list): lista con ogni elemento un dizionario
        """

        # Effttuiamo ora una serie di controlli per verificare se l'input ha tutte le caratteristiche richieste

        # Controllo se 'transactions' è una lista
        if not isinstance(transactions, list):
            raise ExamException(f"Il parametro non è del tipo richiesto, bensì del tipo {type(transactions)}. Ci si aspetta una lista")
        
        if len(transactions) == 0:
            raise ExamException("La lista è vuota")
        
        for item in transactions:
            
            # Controllo se 'item' è un dizionario
            if not isinstance(item, dict):
                raise ExamException(f"L'elemento {item} non è del tipo richiesto, bensì del tipo {type(item)}. Ci si aspetta un dizionario")

            # Controllo se il dizionario al posto 'item' è vuoto; se si, viene rimosso dalla lista
            if len(item) == 0:
                print("Il dizionario inserito è vuoto...verrà rimosso dalla lista")
                transactions.remove(item)

            # Controllo se la key 'date' è presente
            try:
                date = item["date"]

                # Controllo se il valore associato a 'date' è una stringa
                if not isinstance(date, str):
                    raise ExamException(f"Il valore associato è del tipo {type(date)}...ci si aspetta una stringa")
                
                # Controllo se a 'date' è associato un valore; se no, viene rimosso 'item' dalla lista
                if len(date) == 0:
                    print("Alla chiave 'date' non è associato nessun valore...'item' verrà rimosso dalla lista")
                    transactions.remove(item)
            except KeyError:
                raise ExamException("Chiave 'date' non presente...impossibile proseguire")
            
            # Controllo se l'anno è nella forma YYYY
            if len(date[:4]) < 4:
                raise ExamException(f"L'anno deve essere nella forma YYYY, mentre in {date[:4]} non è così")
            
            # Controllo se l'anno è un numero intero
            try:
                Year = int(date[:4])
            except (ValueError,TypeError):
                raise ExamException("Valore inserito per l'anno non corretto. Ci si aspetta un valore intero")
            
            # Controllo se il mese è nella forma MM
            if len(date[5:7]) < 2:
                raise ExamException(f"Il mese deve essere nella forma MM, mentre in {date[5:7]} non è così")
            
            # Controllo se il mese è un numero intero
            try:
                Month = int(date[5:7])

                # Controllo se il mese esiste
                if (Month < 1) or (Month > 12):
                    raise ExamException(f"Il valore inserito per il mese {Month} non rappresenta un mese esistente")
            except (ValueError,TypeError):
                raise ExamException("Valore inserito per il mese non corretto. Ci si aspetta un valore intero")
            
            # Controllo se il giorno è nella forma DD
            if len(date[8:10]) < 2:
                raise ExamException(f"Il giorno deve essere nela forma DD, mentre in {date[8:10]} non è così")
            
            # Controllo se il giorno è un numero intero
            try:
                Day = int(date[8:10])

                # Controllo se il giorno è valido sia normalmente sia negli anni bisestili
                if (Day < 1) or (Day > 31):
                    raise ExamException("Un mese non può avere meno di un giorno o più di 31 giorni")
                elif (Year % 4 != 0) and (Month == 2) and (Day >= 29):
                    raise ExamException(f"Negli anni non bisestili febbario ha 28 giorni, mentre in questo caso ne ha {Day}")
            except (ValueError,TypeError):
                raise ExamException("Valore inserito per il giorno non corretto. Ci si aspetta un valore intero")

            # Controllo se la key 'amount' è presente
            try:
                amount = item["amount"]
            except KeyError:
                raise ExamException("Chiave 'amount' non presente...impossibile proseguire")
            
            # Controllo se il valore è valido o può essere convertito in un float, altrimento imposto 0 di default
            if not isinstance(amount, float):
                print(f"Valore inserito per 'amount' {amount} non valido...verrà provata la conversione in float")

                try:
                    float(amount)
                except:
                    print("Impossibile convertire il valore...verrà impostato 0 di default")
                    amount = 0
            
            # Controllo se la key 'category' è presente
            try:
                category = item["category"]

                # Controllo se il valore associato a 'category' è una stringa
                if not isinstance(category, str):
                    raise ExamException(f"Il valore associato è del tipo {type(category)}...ci si aspetta una stringa")
                
                # Controllo se a 'category' è associato un valore; se no, viene rimosso 'item' dalla lista
                if len(category) == 0:
                    print("Alla chiave 'category' non è associato nessun valore...'item' verrà rimosso dalla lista")
                    transactions.remove(item)
            except KeyError:
                raise ExamException("Chiave 'category' non presente...impossibile proseguire")
            
        self.transactions = transactions

    def calculate_total_balance(self):
        """Metodo 'calculate_total_balance'

        Attributi:
            self.transactions (list)
        
        Output:
            total_balance (float) = somma di tutti i valori di 'amount'
        """

        total_balance = 0

        for item in self.transactions:
            total_balance += item["amount"]
        
        return total_balance
    
    def calculate_balance_by_category(self):
        """Metodo 'balance_by_category'

        Attributi:
            self.transactions (list)
        
        Output:
            balance_by_category (dict): dizionario contenente la somma di tutti gli 'amount' per ogni rispettiva categoria
        """

        balance_by_category = {}

        for item in self.transactions:
            amount = item["amount"]
            category = item["category"]

            if category not in balance_by_category.keys():
                balance_by_category[category] = amount
            else:
                balance_by_category[category] += amount

        return balance_by_category
    
    def get_latest_transactions_by_category(self):

        latest_transactions_by_category = {}

        for item in self.transactions:
            category = item["category"]

            if category not in latest_transactions_by_category.keys():
                latest_transactions_by_category[category] = item
            else:
                date = item["date"]
                date_in_dict = latest_transactions_by_category[category]["date"]

                if int(date[:4]) > int(date_in_dict[:4]):
                    latest_transactions_by_category[category] = item
                elif (int(date[:4]) == int(date_in_dict[:4])) and (int(date[5:7] > int(date_in_dict[5:7]))):
                    latest_transactions_by_category[category] = item
                elif (int(date[:4]) == int(date_in_dict[:4])) and (int(date[5:7] == int(date_in_dict[5:7])))  and (int(date[8:10] > int(date_in_dict[8:10]))):
                    latest_transactions_by_category[category] = item
        
        return latest_transactions_by_category
                
