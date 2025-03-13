
class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, file_name):
        """Costruttore

        Parametri: 
            file_name (path del file): elenco data (YYYY-MM) e numero di passeggeri (in migliaia)
        """

        if not isinstance(file_name, str):
            raise ExamException("Il parametro passato non è del tipo richiesto, ci si aspetta una stringa (path del file).")

        self.file_name = file_name
        

    def get_data(self):
        """Metodo 'get_data'

        Controlli:
            Alza eccezzione se il file non è apribile
            Alza eccezzione se l'anno non è un valore numerico
            Alza eccezzione se il mese non è un valore numerico
            Alza eccezzione se il mese non è esistente
            Le righe che non hanno un valore in 'passengers' vengono ignorate

        Output:
            lista di liste contentente, per ogni elemento, una riga del file
        """
        try:
            file = open(self.file_name, 'r')
        except:
            raise ExamException("Errore nell'apertura del file")
        
        try:
            data = file.read().splitlines()
        except:
            raise ExamException("Errore nella lettura del file.")
        
        time_series_list = []

        for line in data:
            elements = line.strip().split(',')

            if elements[0] != 'date':
                control_date = elements[0]
                year_str, month_str = elements[0][:4], elements[0][5:7]

                if year_str.isdigit() is False:
                    raise ExamException("Valore anno non valido")
                
                if month_str.isdigit() is False:
                    raise ExamException("Valore mese non valido")
                
                year, month = int(year_str), int(month_str)

                if (month < 1) or (month > 12):
                    raise ExamException("Mese non esistente")

                if year < 1903:
                    raise ExamException("Gli aerei in quell'anno non sono ancora stati inventanti.")

                if elements[1].isdigit():
                    time_series_list.append([elements[0], int(elements[1])])
            
            file.close()

        return time_series_list


def media(data):
    """Funzione 'media'

    Parametri:
        list (lista): lista contenente tutti i valori di un singolo anno

    Output: 
        Media della lista
    
    """
    if not isinstance(data, list):
        raise ExamException("Il parametro passato non è del tipo richiuesto, ci si aspetta una lista.")

    return (sum(data) / len(data))

def compute_variations(time_series, first_year, last_year):
    """Funzione 'compute_variations'

    Parametri:
        time_series (lista di liste): lista di liste della classe
        first_year (str): anno di partenza
        last_year (str): anno di arrivo
    
    Controlli:
        first_year e last_year devono essere interi e contenuti nel file
        first_year deve essere minore o uguale di last_year
        controlli vari sull'indice 'i' durante l'iterazione

    Output:
        my_dictionary: dizionario con la differenza delle media di due anni adiacenti
    """
    try:
        first_year = int(first_year)
    except ValueError:
        raise ExamException("Valore inserito per il primo anno non valido")
    
    try:
        last_year = int(last_year)
    except ValueError:
        raise ExamException("Valore inserito per l'ultimo anno non valido")

    control_1 = time_series[0]
    control_2 = control_1[0]

    if first_year < int(control_2[:4]):
        raise ExamException("Anno di partenza inserito non contenuto nel file")
    
    control_1 = time_series[len(time_series)-1]
    control_2 = control_1[0]

    if last_year > int(control_2[:4]):
        raise ExamException("Anno di arrivo inserito non contenuto nel file")

    if last_year < first_year:
        raise ExamException("Il primo anno non può essere maggiore dell'ultimo")
    
    years_averages = []

    i = 0
    while first_year <= last_year:
        list_control = []
        check_years_1 = time_series[i]
        check_years_2 = check_years_1[0] # Indicatore dell'anno

        if int(check_years_2[:4]) < first_year:
            i += 1
        
        elif int(check_years_2[:4]) == first_year:

            while int(check_years_2[:4]) == first_year:
                list_control.append(time_series[i][1])
                i += 1

                try:
                    check_years_2 = time_series[i][0]
                except IndexError:
                    break
            
            years_averages.append([first_year, media(list_control)])
            first_year += 1
        
        elif int(check_years_2[:4]) > first_year:
            years_averages.append([first_year, 0])
            first_year += 1

    my_dictionary = {}

    if len(years_averages) == 1:
        key = f"{first_year - 1}"
        my_dictionary[key] = years_averages[0][1]
    else:
        i = 0

        while i <= (len(years_averages) - 1):
            time_controller_1 = years_averages[i]

            try:
                time_controller_2 = years_averages[i+1]
            except IndexError:
                break
            
            if time_controller_1[1] == 0:
                j = i+1
                
                try:
                    time_controller_1 = years_averages[j]
                except IndexError:
                    break

                while time_controller_1[1] == 0:
                    j += 1
                    
                    try:
                        time_controller_1 = years_averages[j]
                    except IndexError:
                        break

            if time_controller_2[1] != 0:
                diff = time_controller_2[1] - time_controller_1[1]
                key = f"{time_controller_1[0]}-{time_controller_2[0]}"
                my_dictionary[key] = round(diff, 2)
                i += 1

            if time_controller_2[1] == 0:
                j = i+1

                try:
                    time_controller_2 = years_averages[j+1]
                except IndexError:
                    break    

                while time_controller_2[1] == 0:
                    j += 1

                    try:
                        time_controller_2 = years_averages[j+1]
                    except IndexError:
                        break
                
                diff = time_controller_2[1] - time_controller_1[1]
                key = f"{time_controller_1[0]}-{time_controller_2[0]}"
                my_dictionary[key] = round(diff, 2)
                i = j+1

    return my_dictionary

name = 'data.csv'
time_series_file = CSVTimeSeriesFile(name)
time_series = time_series_file.get_data()

dict = compute_variations(time_series, "1949", "1962")

print("{")
for k,v in dict.items():
    print(f"    {k}: {v}")
print("}")

