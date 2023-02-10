"""
task 10.7
Вы разрабатываете приложение для прослушивания музыки. 
Конечно же, там будет доступна функция перемешивания плейлиста. 
Пользователю может настолько понравиться перемешанная версия плейлиста, 
что он захочет сохранить его копию. 
Однако вы не хотите хранить в памяти новую версию плейлиста, 
а просто хотите сохранять тот seed, с которым он был сгенерирован.

Для этого напишите функцию shuffle_seed(array), 
которая принимает на вход массив из чисел, 
генерирует случайное число 
для seed в диапазоне от 0 до 2**32 - 1 (включительно)
и возвращает кортеж: 
перемешанный с данным seed массив 
(исходный массив должен оставаться без изменений), 
а также seed, с которым этот массив был получен.

Пример
array = [1, 2, 3, 4, 5]
shuffle_seed(array)
# (array([1, 3, 2, 4, 5]), 2332342819)
shuffle_seed(array)
# (array([4, 5, 2, 3, 1]), 4155165971)
"""
import numpy as np

def shuffle_seed(array):
    print(f'    def array={array}=')
    
    seed = np.random.randint(2 ** 32, dtype = np.uint32) # генерирует случайное число 
    # для seed в диапазоне от 0 до 2**32 - 1 (включительно)
    
    np.random.seed(seed) # фиксируем используемый seed
    
    result = np.random.permutation(array) # перемешанный с данным seed массив
    
    print(f'    def seed={seed}=')
    print(f'    def result={result}=')
    return result, seed


array = [1, 2, 3, 4, 5]
shuffle_seed(array)
# print(shuffle_seed(array))
# arr_tmp = shuffle_seed(array)
# print(f' shuffle_seed[1, 2, 3, 4, 5]={arr_tmp}')
# (array([1, 3, 2, 4, 5]), 2332342819)
print('next==')

shuffle_seed(array)
# (array([4, 5, 2, 3, 1]), 4155165971)
