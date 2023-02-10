"""
task 10.8
Напишите функцию min_max_dist(*vectors), 
которая принимает на вход неограниченное число векторов через запятую. 
Гарантируется, что все векторы, 
которые передаются, одинаковой длины.

Функция возвращает 
минимальное и максимальное расстояние между векторами
в виде кортежа.

Пример
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)

???
как вариант подумать о применении ???
называется это list comprehension [лист компрехеншн]. 
Нужно запомнить, так как это очень часто встречается/

это сокращенное воспроизведение цикла for в который вложен другой цикл for
Смотрите, это можно записать как
for bill in north:
    for elem in bill:
         north_list.append(elem)
а так мы всю строчку закрываем в квадратные скобочки, 
т.е. это теперь у нас список [list]
а потом заполняем этот списком элементами - elem при этом из берем из
for bill in north - где bill это будет вложенный список
а потом из этого вложенного списка уже вытаскиваем elem через for elem in bill

north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]

"""
import numpy as np

def min_max_dist(*vectors):
    print(f'    def vectors={vectors}=')
    
    distances = list() # создали новый пустой список
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            distances.append(np.linalg.norm(vectors[i] - vectors[j]))
    
    print(f'    def distances={distances}=')
    min_dist = min(distances)
    max_dist = max(distances)
    print(f'    def min_dist={min_dist}=    max_dist={max_dist}=')
    
    return min_dist, max_dist
    # return (min(distances), max(distances))


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)