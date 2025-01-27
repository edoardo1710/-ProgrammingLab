
class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, file_name):
        """Costruttore

        Parametri: 
            file_name (lista): elenco data (YYYY-MM) e numero di passeggeri (in migliaia)
        """
        
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
            open(self.file_name, 'r')
        except:
            raise ExamException("Errore nell'apertura del file")
        
        time_series_list = []

        with open(self.file_name, 'r') as my_file:

            for line in my_file:
                elements = line.strip().split(',')

                if elements[0] != 'date':
                    control_date = elements[0]

                    if control_date[:4].isdigit() is False:
                        raise ExamException("Valore anno non valido")
                    
                    if control_date[5:7].isdigit() is False:
                        raise ExamException("Valore mese non valido")
                    
                    control_month = int(control_date[5:7])
                    if (control_month < 1) or (control_month > 12):
                        raise ExamException("Mese non esistente")

                    if elements[1].isdigit():
                        elements[1] = int(elements[1])
                        time_series_list.append(elements)
        
        return time_series_list

def media(list):
    """Funzione 'media'

    Parametri:
        list (lista): lista contenente tutti i valori di un singolo anno

    Output: 
        Media della lista
    
    """
    media = sum(list)/len(list)
    
    return media

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
    except:
        raise ExamException("Valore inserito per il primo anno non valido")
    
    try:
        last_year = int(last_year)
    except:
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
    list_control = []
    while first_year <= last_year:
        check_years_1 = time_series[i]
        check_years_2 = check_years_1[0] # Indicatore dell'anno

        if int(check_years_2[:4]) < first_year:
            i += 1
        
        if int(check_years_2[:4]) == first_year:

            while int(check_years_2[:4]) == first_year:
                list_control.append(check_years_1[1])
                i += 1
                try:
                    check_years_1 = time_series[i]
                    check_years_2 = check_years_1[0]
                except IndexError:
                    break
            
            years_averages.append([first_year, media(list_control)])
            first_year += 1
        
        if int(check_years_2[:4]) > first_year:
            years_averages.append([first_year, 0])
            first_year += 1

    my_dictionary = {}

    if len(years_averages) == 1:
        key = f"{first_year-1}"
        control = years_averages[0]
        my_dictionary[key] = control[1]
    else:
        i = 0
        while i <= (len(years_averages)-1):
            time_controller_1 = years_averages[i]

            try:
                time_controller_2 = years_averages[i+1]
            except IndexError:
                break
            

            if time_controller_2[1] != 0:
                diff = time_controller_2[1] - time_controller_1[1]
                diff = round(diff, 2)
                key = f"{time_controller_1[0]}-{time_controller_2[0]}"
                my_dictionary[key] = diff
                i += 1

            if time_controller_2[1] == 0:
                j = i+1
                time_controller_2 = years_averages[j+1]

                while time_controller_2[1] == 0:
                    j += 1
                    time_controller_2 = years_averages[j+1]
                
                diff = time_controller_2[1] - time_controller_1[1]
                diff = round(diff, 2)
                key = f"{time_controller_1[0]}-{time_controller_2[0]}"
                my_dictionary[key] = diff
                i = j+1

    return my_dictionary

