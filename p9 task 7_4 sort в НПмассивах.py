"""
task 7.4
Вам дан массив mystery:
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

Получите булевый массив nans_index 
с информацией о np.nan в массиве mystery: 
True - значение пропущено, 
False - значение не пропущено

В переменную `n_nan сохраните число пропущенных значений

Скопируйте массив mystery в массив mystery_new. 
Заполните пропущенные значения в массиве mystery_new нулями

Поменяйте тип данных в массиве mystery на int32 
и сохраните в переменную mystery_int

Отсортируйте значения в массиве по возрастанию
и сохраните результат в переменную array

Сохраните в массив table двухмерный массив, 
полученный из массива array. 
В нём должно быть 5 строк и 3 столбца. 
Причём порядок заполнения должен быть по столбцам!
Например,
 1, 2, 3, 4 -> 1    3
               2    4
Сохраните в переменную col средний столбец из table

Примечание. Не меняйте названия переменных.
"""
import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)


"""
Получите булевый массив nans_index 
с информацией о np.nan в массиве mystery: 
True - значение пропущено, 
False - значение не пропущено
"""
nans_index = np.isnan(mystery)
print(f'nans_index={nans_index}') # np.nan >> True
print('next==')


"""
В переменную n_nan сохраните число пропущенных значений
var = np.count_nonzero(np.isnan(mystery))
n_nan = mystery.size - var
print(f'n_nan{n_nan} = mystery.size{mystery.size} - var{var}') # 


n_nan = mystery.size - np.count_nonzero(np.isnan(mystery))
Ожидаемый ответ: 3
Ваш ответ: 12
"""
var = np.count_nonzero(np.isnan(mystery))
n_nan = mystery.size - var
print(f'n_nan{n_nan} = mystery.size{mystery.size} - var{var}') # n_nan12 = mystery.size15 - var3
n_nan = mystery.size - np.count_nonzero(np.isnan(mystery))
print(f'n_nan={n_nan}') # 
print('next==')


"""
Скопируйте массив mystery в массив mystery_new. 
Заполните пропущенные значения в массиве mystery_new нулями
"""
mystery_new = np.empty_like(mystery)
mystery_new[:] = mystery
mystery_new[np.isnan(mystery_new)] = 0
print(f'mystery_new={mystery_new}')
# print(f'mystery={mystery}') # проверка ВДРУГ внесли изменения
print('next==')



"""
Поменяйте тип данных в массиве mystery на int32 
и сохраните в переменную mystery_int
"""
print(f'1+ mystery.dtype={mystery.dtype}')
print(f'1+ mystery={mystery}') 
# mystery = mystery.astype('int32') # change the dtype to 'int32'
# print(f'2 mystery={mystery}') 

  
mystery_int = np.empty_like(mystery)
mystery_int[:] = mystery
print(f'1+ mystery_int={mystery_int}')
print(f'1+ mystery_int.dtype={mystery_int.dtype}')
mystery_int = mystery_int.astype('int32') # change the dtype to 'int32'
print(f'2 mystery_int={mystery_int}')
print(f'2 mystery_int.dtype={mystery_int.dtype}')
print(f'3 mystery={mystery}') # проверка ВДРУГ внесли изменения
print(f'3 mystery.dtype={mystery.dtype}')
print('next==')


"""
Отсортируйте значения в массиве по возрастанию
и сохраните результат в переменную array

array = np.sort(mystery) 
Ожидаемый ответ:
[-26024. -17722. -16431.  -9212.  -6974.  -2365.      0.      0.      0.
  12279.  16132.  25933.  28745.  29810.  31244.]
Ваш ответ:
[-2147483648 -2147483648 -2147483648      -26024      -17722      -16431
       -9212       -6974       -2365       12279       16132       25933
       28745       29810       31244]
"""
# print(f'4 mystery={mystery}')
array_ = np.sort(mystery) 
print(f'5 np.sort(mystery)={array_}') 
array = np.sort(mystery_new) 
print(f'5+ np.sort(mystery_new)={array}') 
# print(f'6 mystery={mystery}') # проверка ВДРУГ внесли изменения

  
"""
Сохраните в массив table двухмерный массив, 
полученный из массива array. 
В нём должно быть 5 строк и 3 столбца. 
Причём порядок заполнения должен быть по столбцам!
Например,
 1, 2, 3, 4 -> 1    3
               2    4
Сохраните в переменную col средний столбец из table

table = array.reshape((5, 3),  order='F')
print(f'7 table = array.reshape={table}') 
Ожидаемый ответ:
[[-26024.  -2365.  16132.]
 [-17722.      0.  25933.]
 [-16431.      0.  28745.]
 [ -9212.      0.  29810.]
 [ -6974.  12279.  31244.]]
Ваш ответ:
[[-2147483648      -16431       16132]
 [-2147483648       -9212       25933]
 [-2147483648       -6974       28745]
 [     -26024       -2365       29810]
 [     -17722       12279       31244]]
 
print(f'col={col}') 
Ожидаемый ответ: [-2365.     0.     0.     0. 12279.]
Ваш ответ:  [-16431  -9212  -6974  -2365  12279] 
"""
# print(f'4 mystery={mystery}')
# table = array.reshape((5, 3))
table = array.reshape((5, 3),  order='F')
print(f'7 table = array.reshape={table}') 
col = table[:, 1]
print(f'col={col}')
# print(f'6 mystery={mystery}') # проверка ВДРУГ внесли изменения

"""
import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

nans_index = np.isnan(mystery)

# n_nan = mystery.size - np.count_nonzero(np.isnan(mystery))
n_nan = np.count_nonzero(np.isnan(mystery))

mystery_new = np.empty_like(mystery)
mystery_new[:] = mystery
mystery_new[np.isnan(mystery_new)] = 0

# mystery = mystery.astype('int32') # change the dtype to 'int32'
mystery_int = np.empty_like(mystery)
mystery_int[:] = mystery
mystery_int = mystery_int.astype('int32') # change the dtype to 'int32'

# array = np.sort(mystery) 
array = np.sort(mystery_new) 

table = array.reshape((5, 3),  order='F')
col = table[:, 1]
"""