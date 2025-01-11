from exercise_03 import animals

# These modifications need to be outside of if __name__ == '__main__' block to be persisted for exercise_05
animals_a = animals.reset_index(inplace=False, drop=True)
animals_b = animals_a.set_index('name', inplace=False)
animals_c = animals_b.drop('Max', inplace=False)
animals_d = animals_c.reset_index(inplace=False)
animals = animals_d

if __name__ == '__main__':
    print(
        '''
    Zadanie 4: Indeksowanie ramek danych [4 pkt]
    Mając ramkę danych animals z poprzedniego zadania, wykonaj w podanej kolejności poniższe kroki,
    po każdym z nich wyświetlając otrzymany wynik:
    '''
    )

    print('\na) przywróć ramce danych domyślny indeks całkowity, sprawiając jednocześnie,'
          'by nie została dodana nowa kolumna z wcześniejszymi wartościami indeksu,')
    print(animals_a)

    print('\nb) utwórz indeks z kolumny \'name\',')
    print(animals_b)

    print('\nc) usuń z ramki danych wiersz, zawierający informacje o psie, wabiącym się Max,')
    print(animals_c)

    print('\nd) przywróć ramce danych domyślny indeks całkowity, sprawiając jednocześnie,'
          'by z istniejącego indeksu uczynić kolumnę danych w ramce.')
    print(animals_d)
