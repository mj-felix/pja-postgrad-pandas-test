from exercise_08 import employees

print(
    '''
Zadanie 9: Zapisywanie danych do pliku MS Excel [2 pkt]
Mając ramkę danych employees z poprzed
niego zadania, wykonaj w podanej kolejności poniższe kroki:
'''
)

print('a) utwórz z niej ramkę danych o nazwie emp_finance, wybierając pracowników działu finasowego, '
      'zarabiających powyżej 20000,')
print('Filling NaN in Income with median ...')
median_income = employees['Income'].median()
emp_finance = employees.copy()
emp_finance['Income'] = emp_finance['Income'].fillna(median_income)
emp_finance = emp_finance[(emp_finance['Department'] == 'Finance') &
                          (emp_finance['Income'] > 20000)]

print('\nb) zapisz ramkę danych emp_finance do skoroszytu MS Excel o nazwie \'emp_finance.xlsx\', '
      'umieszczając dane w arkuszu o nazwie \'employee_finance\'.')
emp_finance.to_excel('emp_finance.xlsx', sheet_name='employee_finance')
print("File 'emp_finance.xlsx' has been created with 'employee_finance' sheet")
