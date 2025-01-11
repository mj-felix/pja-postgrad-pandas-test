import pandas as pd


# a) wczytaj jego zawartość do ramki danych weather,
weather = pd.read_csv('weather.csv')

# b) usuń z otrzymanej ramki danych kolumnę 'Location',
weather.drop('Location', axis=1, inplace=True)

# c) zmodyfikuj kolumnę 'Date' tak, by zawierała ona standardowe znaczniki czasowe,
weather['Date'] = pd.to_datetime(weather['Date'])

if __name__ == '__main__':
    print(
        '''
Zadanie 6: Wczytywanie danych z pliku CSV [4 pkt]
Mając plik CSV o nazwie 'weather.csv' (możesz go pobrać stąd), wykonaj w podanej kolejności
poniższe kroki:
a) wczytaj jego zawartość do ramki danych weather,
b) usuń z otrzymanej ramki danych kolumnę 'Location',
c) zmodyfikuj kolumnę 'Date' tak, by zawierała ona standardowe znaczniki czasowe,
'''
    )

    print('\nd) wyświetl informacje o zmodyfikowanej ramce danych i jej strukturze')
    weather.info()

    print('\noraz jej ostatnich 7 wierszy.')
    print(weather.tail(7))
