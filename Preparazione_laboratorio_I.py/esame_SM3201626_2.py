class ExamException(Exception):
    pass

class CSVTemperatureFile():

    def __init__(self, file_name):
        """Costruttore

        Parametri:
            file_name (file path): elenco con data (YYYY-MM)e temperature medie del mese
        """

        # Controllo: se 'file_name' non è una stringa allora alza un'eccezzione
        if not isinstance(file_name, str):
            raise ExamException("Il parametro passato alla classe non è del tipo richiesto, ci si aspetta una stringa (path del file).")
        
        self.file_name = file_name

    def is_integer(element):
        """Metodo 'is_integer'
        
        Parametri:
            element : elemento passato da 'get_data'

        Output:
            True se il numero è intero, altrimenti False
        """
        try:
            int(element)
            return True
        except ValueError:
            return False

    def get_data(self):
        """Metodo 'get_data'

        Parametri:
            self.file_name (file_path)

        Output:
            temperature_file_list (list): lista di liste contenete la coppia 'date-temperature'
        """

        # Controllo: se il file non è apribile alza un'eccezzione
        try:
            file = open(self.file_name, 'r')
        except IOError:
            raise ExamException("Errore nell'apertura del file")
        except FileNotFoundError:
            raise ExamException("Il file non esiste")
        
        # Controllo: se il file non è leggibile alza un'eccezzione
        try:
            data = file.read().splitlines()
        except IOError:
            raise ExamException("Errore nella lettura del file")

        # 'temperature_file_list' è la lista di liste
        temperature_file_list = []

        for line in data:

            # Se la linea è vuota viene saltata
            if line:
                elements = line.strip().split(',')

                # Se la linea è quella di intestazione viene saltata
                if elements[0] != 'date':
                    
                    # 'date' contiene il valore dell'anno e del mese separati
                    date = elements[0].strip().split('-')

                    # Controllo: se il valore dell'anno non è un intero alza un'eccezzione
                    try:
                        year = int(date[0])
                    except:
                        raise ExamException("Valore inserito per l'anno non valido")
                    
                    # Controllo: se il valore dell'anno non è nella forma YYYY alza un'eccezzione
                    if len(date[0]) < 4:
                        raise ExamException("Il valore dell'anno dev'essere in forma YYYY")
                    
                    # Controllo: se il valore del mese non è un intero alza un'eccezzione
                    try:
                        month = int(date[1])
                    except:
                        raise ExamException("Valore inserito per il mese non valido")
                    
                    # Controllo: se il valore del mese non è nella forma MM alza un'eccezzione
                    if len(date[1]) < 2:
                        raise ExamException("Il valore del mese dev'essere in forma MM")
                    
                    # Controllo: se il valore del mese non rappresenta un mese esistente alza un'eccezzione
                    if (month < 1) or (month > 12):
                        raise ExamException("Il valore del mese deve rappresentare un mese esistente")
                    
                    # Se il valore di 'temperature' è un intero allora può essere aggiunto a 'temperature_file_list'
                    if CSVTemperatureFile.is_integer(elements[1]):
                        temperature_file_list.append([elements[0], int(elements[1])])

        file.close()
        return temperature_file_list

def average(data):

    return sum(data)/len(data)

def compute_temperature_variations(temperature_series, first_year, last_year):

    # Controllo: se 'temperature_series' non contiene elementi alza un'eccezzione
    if len(temperature_series) == 0:
        raise ExamException("Il file non contiene elementi esclusa l'intestazione")

    # Controllo: se 'temperature_series' non è una lista alza un'eccezzione
    if not isinstance(temperature_series, list):
        raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta una lista (lista di liste).")

    # Controllo: se 'first_year' non è una stringa alza un'eccezzione
    if not isinstance(first_year, str):
        raise ExamException("Il parametro passato come anno di partenza non è del tipo richiesto, ci si aspetta una stringa.")

    # Controllo: se 'last_year' non è una stringa alza un'eccezzione
    if not isinstance(last_year, str):
        raise ExamException("Il parametro passato come anno di arrivo non è del tipo richiesto, ci si aspetta una stringa.")

    # Controllo: se il valore di 'first_year' non è nella forma YYYY alza un'eccezzione
    if len(first_year) < 4:
        raise ExamException("Il valore passato come anno di partenza dev'essere nella forma YYYY")
    
    # Controllo: se il valore di 'first_year' non è un intero alza un'eccezzione
    try:
        first_year = int(first_year)
    except:
        raise ExamException("Il valore passato come anno di partenza non è valido")

    # Controllo: se il valore di 'last_year' non è nella forma YYYY alza un'eccezzione
    if len(last_year) < 4:
        raise ExamException("Il valore passato come anno di arrivo dev'essere nella forma YYYY")
    
    # Controllo: se il valore di 'last_year' non è un intero alza un'eccezzione
    try:
        last_year = int(last_year)
    except:
        raise ExamException("Il valore passato come anno di arrivo non è valido")

    # Controllo: se il valore di 'last_year' è minore di quello di 'first_year' alza un'eccezzione
    if first_year > last_year:
        raise ExamException("Il valore dell'anno di arrivo non può essere minore di quello di partenza")
    
        # Si potrebbe anche evitare di alzare un'eccezzione scambiando i due valori nel modo seguente:
        # temp = first_year_int
        # first_year_int = last_year_int
        # last_year_int = temp
    
    # 'data_average_list' contiene la temperatura media di tutti gli anni compresi tra 'first_year' e 'last_year'
    data_average_list = []

    # 'temperature_series_iter' è l'iteratore di 'temperature_series'
    temperature_series_iter = iter(temperature_series)

    while first_year <= last_year:
        # Controllo: se si verifica un 'StopIteration' vuol dire che abbiamo "analizzato" tutti i dati
        try:
            item = next(temperature_series_iter)
        except StopIteration:
            break

        current_year = int(item[0][:4])

        # Se 'current_year' è minore di 'first_year' allora continuiamo con il prossimo elemento
        if current_year < first_year:
            continue
        # Se 'current_year' è uguale a 'first_year' possiamo cominciare ad analizzare i dati
        elif current_year == first_year:
            # 'temp_data_list' contiene tutti i valori di 'temperature' di un singolo anno
            temp_data_list = []

            while current_year == first_year:
                temp_data_list.append(item[1])

                # Controllo: se si verifica un 'StopIteration' vuol dire che abbiamo "analizzato" tutti i dati
                try:
                    item = next(temperature_series_iter)
                    current_year = int(item[0][:4])
                except StopIteration:
                    break

            # All'uscita dal ciclo 'while' viene incrementato 'first_year' e viene aggiunta la media a 'data_average_list'
            data_average_list.append([str(first_year), average(temp_data_list)])
            first_year += 1
        # Se 'current_year' è maggiore di 'first_year' allora c'è un anno senza dati che verrà escluso
        elif current_year > first_year:
            first_year += 1
    
    temperature_dictionary = {}

    i = 0

    # Caso particolare se 'first_year' e 'last_year' coincidono
    if len(data_average_list) == 1:
        key = first_year
        temperature_dictionary[key] = data_average_list[1]
    else:
        
        while i < (len(data_average_list)-1):

            # Controllo: se all'incremento di 'i' si verifica un 'IndexError' vuol dire che abbiamo "analizzato" tutti i dati
            try:
                # 'current_year' rappresenta l'anno, mentre 'next_year' l'anno successivo
                current_year = data_average_list[i][0]
                next_year = data_average_list[i+1][0]
            except IndexError:
                break
            
            key = f"{current_year}-{next_year}"
            temperature_dictionary[key] = round(data_average_list[i+1][1]-data_average_list[i][1],2)
            i += 1
    
    return temperature_dictionary

name = 'data.csv'
temperature_file = CSVTemperatureFile(name)
temperature_list = temperature_file.get_data()

# for item in temperature_list:
#     print(f"    {item}")

# data_list = compute_temperature_variations(temperature_list, "1949", "1960")
# for item in data_list:
#     print(f"    {item}")

temperature_dictionary = compute_temperature_variations(temperature_list, "1949", "1960")
for k,v in temperature_dictionary.items():
    print(f"    {k}: {v}")