"""
task 10.6
Напишите функцию get_chess(a), 
которая принимает на вход длину стороны квадрата a 
и возвращает двумерный массив формы (a, a), 
заполненный 0 и 1 в шахматном порядке. 
В левом верхнем углу всегда должен быть ноль.

Примечание. 
воспользуйтесь функцией np.zeros, 
а затем с помощью срезов без циклов 
задайте необходимым элементам значение 1.

В Python для получения каждого второго элемента 
используется срез [::2]. 
Подумайте, как грамотно применить этот принцип к двумерному массиву.

Пример

get_chess(1)
# array([[0.]])

get_chess(4)
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])
"""
import numpy as np

def get_chess(a):
    print(f'    def a={a}=')
    arra = np.zeros((a, a)) # создали массив заполненный нулями
    arra[::2, 1::2] = 1 # в чётных строках И на НЕчетные позиции вводим 1
    arra[1::2, ::2] = 1 # в нечётных строках И на четные позиции вводим 1
    
    return arra



arr_tmp = get_chess(1)
# array([[0.]])
print(f' get_chess(1)={arr_tmp}')
# array([[0.]])

arr_tmp = get_chess(4)
print(f' get_chess(4)={arr_tmp}')
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])')

get_chess(4)
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])