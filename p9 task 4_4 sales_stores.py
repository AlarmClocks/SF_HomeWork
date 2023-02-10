"""
task 4.4
В переменных center, south и north хранятся 
списки из перечней купленных позиций в трёх торговых точках, 
расположенных в разных районах города.

Вначале избавьтесь от излишней вложенности: 
в каждой переменной (center, south, north) 
должен храниться объединённый 
список купленных товаров без разбиения по чекам.

Пример: [['Milk', 'Bread'], ['Meat']] -> ['Milk', 'Bread', 'Meat']

После этого определите, в каком магазине было куплено больше всего товаров.

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

[['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips

"""

# from hidden import *
from collections import Counter

center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], ['Milk', 'Milk', 'Cheese']]
north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola']]
# print(f'center == {center}==')
# print(f'south == {south}==')
# print(f'north == {north}==')
# print('next==')

center_list = [elem for bill in center for elem in bill]
south_list = [elem for bill in south for elem in bill]
north_list = [elem for bill in north for elem in bill]
# print(f'center_list == {center_list}==')
# print(f'south_list == {south_list}==')
# print(f'north_list == {north_list}==')
# print('next==')

"""
Реальные данные

center_counter == 548 == 27 == Counter({'Bread': 95, 'Beer': 81, 'Chips': 61, 'Cola': 60, 'Meat': 46, 'Milk': 43, 'Cheese': 39, 'Chocolate': 35, 'Ketchup': 33, 'Soap': 28, 'Yoghurt': 27})==
south_counter == 478 == 24 ==Counter({'Bread': 73, 'Meat': 60, 'Beer': 60, 'Cola': 55, 'Milk': 46, 'Chocolate': 39, 'Yoghurt': 33, 'Cheese': 30, 'Ketchup': 30, 'Chips': 28, 'Soap': 24})==
north_counter == 500 == 10 ==Counter({'Cola': 121, 'Beer': 116, 'Bread': 72, 'Chips': 39, 'Chocolate': 33, 'Yoghurt': 30, 'Soap': 28, 'Milk': 22, 'Meat': 15, 'Ketchup': 14, 'Cheese': 10})==
task 4.8
center_counter + south_counter + north_counter == Counter({'Beer': 257, 'Bread': 240, 'Cola': 236, 'Chips': 128, 'Meat': 121, 'Milk': 111, 'Chocolate': 107, 'Yoghurt': 90, 'Soap': 80, 'Cheese': 79, 'Ketchup': 77})==
next==
task 4.7
total_counter == Counter({'Beer': 257, 'Bread': 240, 'Cola': 236, 'Chips': 128, 'Meat': 121, 'Milk': 111, 'Chocolate': 107, 'Yoghurt': 90, 'Soap': 80, 'Cheese': 79, 'Ketchup': 77})==
    elem

"""

center_counter = Counter(center_list)
south_counter = Counter(south_list)
north_counter = Counter(north_list)

print('task 4.5')
# print(f'center_counter == {sum(center_counter.values())} == {min(center_counter.values())} =={center_counter}==')
print(f'center_counter == {sum(center_counter.values())} == {min(center_counter.values())} == {center_counter}==')
print(f'south_counter == {sum(south_counter.values())} == {min(south_counter.values())} =={south_counter}==')
print(f'north_counter == {sum(north_counter.values())} == {min(north_counter.values())} =={north_counter}==')
print('next==')

print('task 4.6')
print('Beer center') if center_counter['Beer'] > north_counter['Beer'] else print('Beer north')
print('Cola center') if center_counter['Cola'] > north_counter['Cola'] else print('Cola north')
print('Bread center') if center_counter['Bread'] > north_counter['Bread'] else print('Bread north')
print('Yoghurt center') if center_counter['Yoghurt'] > north_counter['Yoghurt'] else print('Yoghurt north')
print('next==')

print('task 4.8')
print(f'center_counter + south_counter + north_counter == {center_counter + south_counter + north_counter}==')
print('next==')

print('task 4.7')
total_counter = center_counter + south_counter + north_counter
print(f'total_counter == {total_counter}==')
for elem in total_counter:
    if ((total_counter[elem]/2 < center_counter[elem])
        or (total_counter[elem]/2 < south_counter[elem])
        or (total_counter[elem]/2 < north_counter[elem])):
        print(f'    elem =={elem} ={total_counter[elem]}')
        print(f'    center_counter elem =={center_counter[elem]}')
        print(f'    south_counter elem =={south_counter[elem]}')
        print(f'    north_counter elem =={north_counter[elem]}')
        print(f'        +!+ ')
            
print('next==')


"""
task 4.5
Теперь получите объекты-счётчики (Counter) 
из каждого полученного в предыдущем задании списка покупок
и сохраните их в отдельные переменные 
(они пригодятся для выполнения следующих задач).

Сколько раз покупали самый редкий товар в магазине north? 
Запишите ответ в числовой форме.

task 4.6
Выберите товар, 
который в магазине center покупали чаще, чем в магазине north:
Beer
Cola
Bread
Yoghurt

task 4.7
Есть ли такой товар, 
который в одном из магазинов покупали чаще, 
чем в двух других вместе взятых? 
Если да, выберите магазин с настолько популярным товаром:

task 4.8
Определите суммарное число продаж каждого товара во всех магазинах,
сложив все объекты-счётчики. 
Сколько раз был куплен второй по популярности товар? 
Запишите ответ в числовой форме.

"""