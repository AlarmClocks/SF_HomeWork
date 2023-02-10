"""
task 9.6
Задайте seed = 2021.
Сохраните в переменные необходимые значения.
Примечание 1. 
Не меняйте названия переменных и 
последовательность генерации случайных чисел в задании.
Примечание 2. 
Не забудьте импортировать numpy и сразу задать seed = 2021

В simple сохраните случайное число в диапазоне от 0 до 1

Сгенерируйте 120 чисел в диапазоне от -150 до 2021, 
сохраните их в переменную randoms

Получите массив из случайных целых чисел от 1 до 100 (включительно)
из 3 строк и 2 столбцов. 
Сохраните результат в table

В переменную even сохраните четные числа от 2 до 16 (включительно)

Скопируйте even в переменную mix. Перемешайте числа в mix так, 
чтобы массив изменился

Получите из even 3 числа без повторений. 
Сохраните их в переменную select

Получите переменную triplet, 
которая должна содержать перемешанные значения 
из массива select (сам select измениться не должен)

"""
import numpy as np
np.random.seed(2021)

# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand() 
print(f'simple={simple}') 

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, 
# сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)
print(f'randoms={randoms}') 

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. 
# Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))
print(f'table={table}') 

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)
print(f'even={even}') 

# Скопируйте even в переменную mix. Перемешайте числа в mix так, 
# чтобы массив изменился
# mix = np.random.permutation(even) # Чтобы получить новый перемешанный массив, а исходный оставить без изменений
"""
mix = np.empty_like(even)
mix[:] = even
print(f'1 mix={mix}') 
mix = np.random.shuffle(mix)
Ожидаемый ответ: [ 6 10  2  8 14 16  4 12]
Ваш ответ: None
"""
mix = np.empty_like(even)
mix = np.random.permutation(even)
print(f'1 mix={mix}') 
print(f'2 mix={mix}') 
print(f'    as viewTest even={even}') # проверка на наличие изменений

# Получите из even 3 числа без повторений. 
# Сохраните их в переменную select
select = np.random.choice(even, size=3, replace=False)
print(f'select={select}') 
#print(f'    as viewTest even={even}') # проверка на наличие изменений

# Получите переменную triplet, 
# которая должна содержать перемешанные значения 
# из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
print(f'triplet={triplet}') 
print(f'    as viewTest select={select}') # проверка на наличие изменений
print(f'    as viewTest even={even}') # проверка на наличие изменений

"""
import numpy as np
np.random.seed(2021)

# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand() 

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, 
# сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. 
# Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)

# Скопируйте even в переменную mix. Перемешайте числа в mix так, 
# чтобы массив изменился
mix = np.empty_like(even)
mix = np.random.permutation(even)


# Получите из even 3 числа без повторений. 
# Сохраните их в переменную select
select = np.random.choice(even, size=3, replace=False)

# Получите переменную triplet, 
# которая должна содержать перемешанные значения 
# из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)

"""