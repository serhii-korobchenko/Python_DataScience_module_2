import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pd.set_option('display.max_columns', None)
#Проведите анализ файла 2017_jun_final.csv. Файл содержит результаты опроса разработчиков в июне 2017 года.

# Прочитайте файл 2017_jun_final.csv с помощью метода read_csv
df = pd.read_csv('2017_jun_final.csv')
print(df.info())

# Прочитайте полученную таблицу используя метод head
pd.set_option('display.max_columns', None)
print(df.head(10))

# Определите размер таблицы с помощью метода shape
print(df.shape)

# Определите типы всех столбцов с помощью dataframe.dtypes
print(df.dtypes)


# Посчитайте, какая доля пропусков содержится в каждой колонке (используйте методы isnull и sum)
print(df.isna().sum())

# Удалите все столбцы с пропусками, кроме столбца "Язык.программирования"
colomn_list = df.dropna(axis='columns').columns.to_list()
colomn_list.append('Язык.программирования')
print (colomn_list)
df = df[(colomn_list)].copy()
print(df)

# Опять посчитайте, какая доля пропусков содержится в каждой колонке и убедитесь, что остался только столбец "Язык.программирования"
print(df.isna().sum())

# Определите новый размер таблицы с помощью метода shape
print(df.shape)

# Создайте новую таблицу python_data в которой будут только строки со специалистами указавшими язык программирования Python
new_table = df.dropna()
print (new_table)

# Определите размер таблицы python_data с помощью метода shape
print(new_table.shape)

# Используя метод groupby выполните группировку по столбцу "Должность"
print(df.groupby(by="Должность"))

# Создайте новый DataFrame, где для сгруппированных данных по столбцу "Должность", выполните агрегацию данных с помощью метода agg и найдите минимальное и максимальное значение в столбце "Зарплата.в.месяц"
grouped_position = df.groupby(by="Должность").agg(['max', 'min'])
print (grouped_position['Зарплата.в.месяц'])

# Создайте функцию fill_avg_salary которая будет возвращать среднее значение заработной платы в месяц. Используйте ее для метода apply и создайте новый столбик "avg"
def fill_avg_salary(salary):
    return np.mean(salary)

grouped_position['avg'] = df.groupby(by="Должность")['Зарплата.в.месяц'].apply(fill_avg_salary)
print (grouped_position[['Зарплата.в.месяц','avg']])
# Создайте описательную статистику с помощью метода describe для нового столбца.
print (grouped_position['avg'].describe())


# Сохраните полученную таблицу в CSV файл
table_for_csv = grouped_position[['Зарплата.в.месяц','avg']]
print(table_for_csv)
table_for_csv.to_csv('result.csv', index=True)