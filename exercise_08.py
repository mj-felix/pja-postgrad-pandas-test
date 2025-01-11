import pandas as pd

# a) wczytaj z niego arkusz 'employee_details' do ramki danych emp_det,
# zaś arkusz 'performance' do ramki danych emp_perf,
emp_det = pd.read_excel('employee.xlsx', sheet_name='employee_details')
emp_perf = pd.read_excel('employee.xlsx', sheet_name='performance')

# b) przekształć w tych ramkach danych kolumnę 'name' na indeks,
emp_det = emp_det.set_index('name')
emp_perf = emp_perf.set_index('name')

# c) połącz je kolumna po kolumnie do ramki danych o nazwie employees,
employees = pd.concat([emp_det, emp_perf], axis=1)

# d) zameń nazwy kolumn tak, by zaczynały się od wielkiej litery,
employees.columns = employees.columns.str.capitalize()
# Assumption: index to be capitalised as well.'
employees.index.name = employees.index.name.capitalize()

if __name__ == '__main__':
    print(
        '''
    Zadanie 8: Wczytywanie danych z pliku MS Excel [5 pkt] Mając skoroszyt MS Excel o nazwie
    'employee.xlsx' (możesz go pobrać stąd), wykonaj w podanej kolejności poniższe kroki:
    a) wczytaj z niego arkusz 'employee_details' do ramki danych emp_det, zaś arkusz 'performance' do
    ramki danych emp_perf,
    b) przekształć w tych ramkach danych kolumnę 'name' na indeks,
    c) połącz je kolumna po kolumnie do ramki danych o nazwie employees,
    d) zameń nazwy kolumn tak, by zaczynały się od wielkiej litery,
    '''
    )
    print('Assumption: index to be capitalised as well.')

    print('\ne) wyświetl informacje o zmodyfikowanej ramce danych i jej strukturze oraz jej zawartość.\n')
    employees.info()
    print(employees)
