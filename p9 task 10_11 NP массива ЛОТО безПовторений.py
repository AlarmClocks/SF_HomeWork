"""
task 10.11
Напишите функцию get_unique_loto(num). 
Она так же, как и функция в задании 49.9.10, 
генерирует num полей для игры в лото, 
однако теперь на каждом поле 5х5 числа не могут повторяться.

Функция также должна возвращать массив формы num x 5 x 5.

Пример
get_unique_loto(3)
Результат:

array([[[26, 91, 73,  7, 16],
       [46, 85, 78, 77, 51],
       [84, 86, 55, 71, 58],
       [17, 61, 50, 30, 97],
       [66, 29, 38, 41, 32]],

      [[49, 32,  3, 21, 85],
       [45,  8, 94, 46, 96],
       [41, 38, 58, 37, 98],
       [66, 77, 54, 80, 26],
       [62, 63, 72,  5, 43]],

      [[55, 60,  6, 80, 97],
       [23, 69, 94,  9, 24],
       [17, 98, 27, 63, 79],
       [84, 74, 51, 39, 54],
       [77, 30, 48, 75, 85]]])


"""
import numpy as np

def _get_unique_loto(num):
    print(f'    +def num={num}=')
    
    # ERROR array = np.random.randint(1, 101, size=(num, 5, 5), replace=False)
    print(f'    +def array={array}=')
    
    return array

def get_unique_loto(num):
    print(f'    +КолКарточек def num={num}=')
    all_digitals = np.arange(1, 101) # ВСЕ числа которые МОГУТ попасть
    print(f'    +def all_digitals={all_digitals}=')
    
    result = list() # пустой список для заполнения
    for i in range(num):
        result.append(np.random.choice(all_digitals, replace=False, size=(5, 5)))
    
    print(f'    +def result={result}=')
    
    res = np.array(result) # привели в красивый вид
    print(f'    +def res={res}=')
    return res

# get_loto(3)
print('next==')
get_unique_loto(3)