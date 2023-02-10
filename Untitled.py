"""
task 4.9
Дан список кортежей ratings с рейтингами кафе. 
Кортеж состоит из названия и рейтинга кафе.
Необходимо отсортировать список кортежей по убыванию рейтинга. 
Если рейтинги совпадают, 
то отсортировать кафе дополнительно по названию в алфавитном порядке.

Получите словарь cafes с упорядоченными ключами из отсортированного списка, 
где ключи — названия кафе, 
а значения — их рейтинг.
"""
import numpy as np
a = np.int8(25)
print(a)
b = np.float16(25)
print(np.finfo(np.float16))
print(np.iinfo(np.int64))
# np.iinfo(np.int8)
# 340282366920938463463374607431768211455
# 1.7014118346046923e+38 = 170141183460469231731687303715884105728
# 170141183460469231731687303715884105727
# ответ = 0
c = int((2 ** 128)/2 - 1)
print(c)
d = (2 ** 128)/2 - 1
print(d)

print(np.sctypeDict)
print(len(np.sctypeDict))
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
print('next==')
a = -456
a.to_bytes(8, byteorder='big', signed=True)
print(a.to_bytes(8, byteorder='big', signed=True))
print('next==')
print(np.uint8(-456))
print('next==')

arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
print(step)
print('after np.linspace(-6, 21, 60, endpoint=True==')
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)

print(None == None)
print(np.nan == np.nan)
print(None is None)
print(np.nan is np.nan)
print(np.nan == None)
print(np.isnan(np.nan))