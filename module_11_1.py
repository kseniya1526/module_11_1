import pandas as pd
import numpy as np
import requests


"""Numpy - содержит многомерные структуры данных и большую библиотеку функций,
 которые эффективно работают с этими структурами данных. 
 Отлично подходит для обработки больших объемов данных"""
numbers = [15, 16, 17, 18, 19, 20, 21]

number = np.array(numbers)
max_number = np.max(numbers)
min_number = np.min(numbers)
sum_number = np.sum(numbers)
mean_number = np.mean(numbers)
prod_number = np.prod(numbers)

print(f'Максимальное число: {max_number}')
print(f'Минимальное число: {min_number}')
print(f'Сумма чисел: {sum_number}')
print(f'Среднее значение: {mean_number}')
print(f'Произведение чисел: {prod_number}')

"""Requests — это библиотека в Python, которая позволяет взаимодействовать с веб-ресурсами и глобальной сетью.
Она предоставляет разработчику обширный выбор функций для работы со всеми видами HTTP-запросов."""

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")

"""Pandas — это библиотека в Python, которая предназначена для анализа уже структурированных данных. Функциональность 
pandas включает в себя преобразование данных. Например, при помощи pandas можно сортировать строки и выделять 
подмножества, вычислять сводную статистику, например, среднее значение, изменять формы фреймов и объединять их."""

Data = [1, 8, 4, 5, 6, 7, 9]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")