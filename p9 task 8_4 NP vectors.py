"""
task 8.4
Векторы в геометрии называются сонаправленными, 
если они коллинеарны и их направления совпадают. 
Отметим, что прямые, на которых лежат сонаправленные вектора,
всегда по определению являются параллельными.
На рисунке ниже представлен пример сонаправленных векторов a, b и c:

Однако на практике не всегда есть возможность нарисовать вектора, 
чтобы понять, являются ли они сонаправленными. 

Поэтому есть несколько математических способов 
определить сонаправленность векторов. Один из них: 
сумма длин сонаправленных векторов должна быть 
равной длине суммы двух векторов.

С помощью этого критерия среди векторов 
a, b и c (которые приведены в файле выше) 
найдите пару сонаправленных векторов.
"""
import numpy as np

# from hidden import *
a=[23, 34, 27]
b=[-54,   1,  46]
c=[46, 68, 54]
# print(f'a={a}')
# print(f'b={b}')
# print(f'c={c}')

vec1 = np.array(a)
vec2 = np.array(b)
vec3 = np.array(c)
# _length_vec1 = np.sqrt(np.sum(vec1 **2)) # длина вектора
length_vec1 = np.linalg.norm(vec1) # длина вектора
length_vec2 = np.linalg.norm(vec2)
length_vec3 = np.linalg.norm(vec3)
# print(f'a={a} vec1= {vec1}  length_vec1={length_vec1} _length_vec1={_length_vec1}')
print(f'a={a} vec1= {vec1}  length_vec1={length_vec1}')
print(f'b={b} vec2= {vec2}  length_vec2={length_vec2}')
print(f'c={c} vec3= {vec3}  length_vec3={length_vec3}')


sum_1 = np.linalg.norm(vec1) + np.linalg.norm(vec2)
l1_l2 = np.linalg.norm(vec1+vec2)
sum_2 = np.linalg.norm(vec1) + np.linalg.norm(vec3)
l1_l3 = np.linalg.norm(vec1+vec3)
sum_3 = np.linalg.norm(vec2) + np.linalg.norm(vec3)
l2_l3 = np.linalg.norm(vec2+vec3)
print(f'    sum_1={sum_1}  l1_l2={l1_l2}')
print(f'    sum_2={sum_2}  l1_l3={l1_l3}')
print(f'    sum_3={sum_3}  l2_l3={l2_l3}')


"""
task 8.5
Найдите пару векторов, расстояние между которыми больше 100.
"""
distance_l1_l2 = np.linalg.norm(vec1 - vec2)
distance_l1_l3 = np.linalg.norm(vec1 - vec3)
distance_l2_l3 = np.linalg.norm(vec2 - vec3)
print(f'    distance_l1_l2={distance_l1_l2}')
print(f'    distance_l1_l3={distance_l1_l3}')
print(f'    distance_l2_l3={distance_l2_l3}')


"""
task 8.6
Найдите пару перпендикулярных векторов 
с помощью скалярного произведения 
(оно должно быть равно нулю).
"""
scalar_l1_l2 = np.dot(vec1, vec2)
scalar_l1_l3 = np.dot(vec1, vec3)
scalar_l2_l3 = np.dot(vec2, vec3)
print(f'    scalar_l1_l2={scalar_l1_l2}')
print(f'    scalar_l1_l3={scalar_l1_l3}')
print(f'    scalar_l2_l3={scalar_l2_l3}')