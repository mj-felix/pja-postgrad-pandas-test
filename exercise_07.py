from exercise_06 import weather

print(
    '''
Zadanie 7: Operacje na typach danych [5 pkt] Mając ramkę danych weather z poprzedniego zadania,
wykonaj w podanej kolejności poniższe kroki:
a) przekształć dane w kolumnach 'RainToday' i 'RainTomorrow' na typ logiczny (boolean), odwzoro
wując wartości 'Yes' na True i 'No' na False,
b) przekształć dane w kolumnach, zawierających dane o kierunku wiatru, na typ kategoryczny
(category),
'''
)

# a) przekształć dane w kolumnach 'RainToday' i 'RainTomorrow' na typ logiczny (boolean),
# odwzorowując wartości 'Yes' na True i 'No' na False,
weather[['RainToday', 'RainTomorrow']] = weather[[
    'RainToday', 'RainTomorrow']].eq('Yes')

# b) przekształć dane w kolumnach, zawierających dane o kierunku wiatru, na typ kategoryczny
# (category),
wind_direction_columns = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
print('>>> Removing NA values in Wind Direction Columns. More analysis required why these are there. '
      'Either becasue the speed of wind is 0 or for some other reason/no reason')
weather[wind_direction_columns] = weather[wind_direction_columns].fillna(
    'N/A or missing')
weather[wind_direction_columns] = weather[wind_direction_columns].astype(
    'category')

print('\nc) wyświetl informacje o zmodyfikowanej ramce danych i jej strukturze,')
weather.info()

print('\nd) wyświetl wiersze, zawierające informacje o pogodzie w pierwszej dekadzie lutego 2008,')
date_mask = (weather['Date'].between('2008-02-01', '2008-02-10'))
first_decade_feb_2008 = weather[date_mask]
print(first_decade_feb_2008)


print(
    '''

e) wyświetl wiersze, zawierające informacje o obserwacjach, w dniach, w których wiatr o godzinie
dziewiątej wiał z kierunków południowozachodnich.
'''
)
sw_wind_days = weather[weather['WindDir9am'] == 'SW']
print(sw_wind_days)
