import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog',
                   'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'name': ['Daisy', 'Bella', 'Noodle', 'Charlie', 'Max', 'Molly', 'Draco', 'Kenzo',  'Milo', 'Cooper'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

animals = pd.DataFrame(data, index=labels)

if __name__ == '__main__':
    print('''
Zadanie 1: Tworzenie ramki danych [2 pkt]
Mając poniższy słownik danych data i listę indeksów wierszy labels, opisujących pacjentów gabinetu
weterynaryjnego, utwórz z nich ramkę danych o nazwie animals. Następnie wyświetl podsumowanie
podstawowych informacji o tej ramce danych i jej strukturze.
''')
    animals.info()
