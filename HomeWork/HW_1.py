# Прочитайте данные с помощью метода read_html из таблицы "Коефіцієнт народжуваності в регіонах України (1950—2019)" по ссылке
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C"
url = "population.html"
tmp = pd.read_html(url)
df = tmp[8]

pd.set_option('display.max_columns', None)

# Вывести первые строки таблицы с помощью метода head
print(df.head(5))

# Определите количество строк и столбцов в датафрейме (атрибут shape)
print(df.shape)

# Замените в таблице значения "—" на значения NaN
df = df.replace(['—'], np.nan)
print(df)

# Определите типы всех столбцов с помощью dataframe.dtypes
print(df.dtypes)

# Замените типы не числовых колонок на числовые. Подсказка - это колонки где находился символ "—"

df = df.astype({"2014": float, "2019": float})
print(df.dtypes)

# Посчитайте, какая доля пропусков содержится в каждой колонке (используйте методы isnull и sum)
print(df.isna().sum())

# Удалите из таблицы данные по всей стране, последняя строчка таблицы
df = df.iloc[:-1].copy()
print (df)

# Замените отсутствующие данные в столбцах средними значениями по этим столбцам (метод fillna)
mean_colomns = df.mean().to_dict()
df = df.fillna(value=mean_colomns).copy()
print(df)

# Получите список регионов, где уровень рождаемости в 2019 году был выше среднего по Украине
mean_Ukraine_2019 = df['2019'].mean()
print (mean_Ukraine_2019)
# class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
regions = df[(df['2019']>mean_Ukraine_2019)]
list_regions = regions['Регіон'].to_list()
print(list_regions)


# В каком регионе была самая высокая рождаемость в 2014 году?
high_fertility_2014 = df['2014'].max()
print(high_fertility_2014)
high_fertility_2014_region = df[(df['2014']==high_fertility_2014)]
region_name = high_fertility_2014_region['Регіон'].to_list()[0]
print(region_name)



# Постройте столбцовую диаграмму рождаемости по регионам в 2019 году

list_regions = df['Регіон'].to_list()


grafic = df[["2019"]].plot(kind = 'bar')
grafic.set_xticklabels(list_regions)

#plt.xlabel("Regions")
plt.show()

# Работа сдается в виде Jupyter файла Hw2.1.ipynb






