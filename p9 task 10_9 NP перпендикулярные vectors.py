"""
task 10.9
Напишите функцию any_normal, 
которая принимает на вход неограниченное число векторов через запятую. 
Гарантируется, что все векторы, которые передаются, одинаковой длины.

Функция возвращает True, 
если есть хотя бы одна пара перпендикулярных векторов. 
Иначе возвращает False.

Пример
vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True

"""
import numpy as np

def any_normal(*vectors):
    print(f'    def vectors={vectors}=')
    
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if np.dot(vectors[i], vectors[j]) == 0:
                # перпендикулярные вектора
                print(f'    def перпендикулярные вектора vectors[i]={i} && vectors[j]={j}=')
                return True
    return False


vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True
