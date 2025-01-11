from exercise_04 import animals

print(
    '''
Zadanie 5: Zapisywanie danych do pliku CSV [3 pkt]
Mając ramkę danych animals z poprzedniego
zadania, wykonaj w podanej kolejności poniższe kroki:
a) zamień w kolumnie 'species' ciągi znaków na pisane samymi wielkimi literami,
b) zapisz tę ramkę danych do pliku CSV o nazwie 'animals.csv' – spraw, by nie zawierał on niejawnych
(numerycznych) indeksów wierszy,
c) odpowiednim poleceniem systemu operacyjnego wyświetl zawartość utworzonego pliku.
'''
)

# a) zamień w kolumnie 'species' ciągi znaków na pisane samymi wielkimi literami,
animals['species'] = animals['species'].str.upper()

# b) zapisz tę ramkę danych do pliku CSV o nazwie 'animals.csv' – spraw, by nie zawierał
# on niejawnych (numerycznych) indeksów wierszy,
animals.to_csv('animals.csv', index=False)

# c) odpowiednim poleceniem systemu operacyjnego wyświetl zawartość utworzonego pliku.
# $ cat animals.csv
if __name__ == '__main__':
    print('''
    $ cat animals.csv
    ''')
    print('''
    species,name,age,visits,price,total
    DOG,Buddy,5.5,2,20,40
    DOG,Cooper,3,1,10,10
    DOG,Charlie,5,3,20,60
    DOG,Draco,4.5,1,20,20
    DOG,Milo,7,2,20,40
    DOG,Noodle,0.5,2,10,20
    DOG,Max,5,3,20,60
    CAT,Bella,3,3,20,60
    CAT,Kenzo,NaN,1,10,10
    CAT,Molly,2,3,20,60
    CAT,Draco,NaN,1,10,10
    CAT,Daisy,2.5,1,10,10
    ''')
