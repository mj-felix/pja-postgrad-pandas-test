from exercise_01 import animals

print('''
Zadanie 2: Wybieranie danych z ramki danych [6 pkt]
Mając ramkę danych animals z poprzedniego zadania, wybierz z niej, a następnie wyświetl:
''')

print('\na) pierwsze 3 wiersze')
selected_rows_a = animals.head(3)
print(selected_rows_a)

print("\nb) kolumny 'animal' i 'age',")
selected_columns_b = animals[['animal', 'age']]
print(selected_columns_b)

print("\nc) dane z wierszy 3, 4 i 8, zawarte w kolumnach 'visits' i 'priority',")
selected_rows_c = animals.iloc[[2, 3, 7]][['visits', 'priority']]
print(selected_rows_c)

print('\nd) wiersze, w których liczba wizyt wynosi więcej niż 2,')
selected_rows_d = animals[animals['visits'] > 2]
print(selected_rows_d)

print('\ne) wiersze, w których zwierzęciem jest kot i ma mniej niż 4 lata,')
selected_rows_e = animals[(animals['animal'] == 'cat') & (animals['age'] < 4)]
print(selected_rows_e)

print('\nf) wiersze, w których wiek zwierzęcia mieści się w przedziale od 2 do 4 lat (włącznie).')
selected_rows_f = animals[animals['age'].between(2, 4)]
print(selected_rows_f)
