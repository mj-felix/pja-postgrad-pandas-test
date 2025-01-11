from exercise_01 import animals

# These modifications need to be outside of if __name__ == '__main__' block to be persisted for exercise_04
# a) dodaj do niej wiersz o indeksie 'k', zawierający informacje o nowym zwierzęciu –
# psie, wabiącym się Buddy, w wieku 5.5 roku, któy odwiedził gabinet 2 razy w zwykłym trybie,
animals.loc['k'] = ['dog', 'Buddy', 5.5, 2, 'no']

# b) dodaj do niej kolumnę 'price', zawierającą wartość 10 dla pacjentów zwykłych
# i 20 dla pacjentów priorytetowych,
animals['price'] = animals['priority'].map({'no': 10, 'yes': 20})

# c) dodaj do niej kolumnę 'total', zawierajacą całkowity koszt wszystkich wizyt,
animals['total'] = animals['visits'] * animals['price']

# d) usuń z niej kolumnę 'priority',
animals.drop(columns=['priority'], inplace=True)

# e) zmień nazwę kolumny 'animal' na 'species',
animals.rename(columns={'animal': 'species'}, inplace=True)

if __name__ == '__main__':
    print(
        '''
    Zadanie 3: Operacje na wierszach i kolumnach [5 pkt]
    Mając ramkę danych animals z poprzedniego zadania, w podanej poniżej kolejności:
    a) dodaj do niej wiersz o indeksie 'k', zawierający informacje o nowym zwierzęciu – psie, wabiącym
    się Buddy, w wieku 5.5 roku, któy odwiedził gabinet 2 razy w zwykłym trybie,
    b) dodaj do niej kolumnę 'price', zawierającą wartość 10 dla pacjentów zwykłych i 20 dla pacjentów
    priorytetowych,
    c) dodaj do niej kolumnę 'total', zawierajacą całkowity koszt wszystkich wizyt,
    d) usuń z niej kolumnę 'priority',
    e) zmień nazwę kolumny 'animal' na 'species',
    f) wyświetl otrzymaną ramkę danych.
    '''
    )

    # f) wyświetl otrzymaną ramkę danych.
    print(animals)
