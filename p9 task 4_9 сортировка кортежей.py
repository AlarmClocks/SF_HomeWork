"""
task 4.9
Дан список кортежей ratings с рейтингами кафе. 
Кортеж состоит из названия и рейтинга кафе.
Необходимо отсортировать список кортежей по убыванию рейтинга. 
Если рейтинги совпадают, 
то отсортировать кафе дополнительно по названию в алфавитном порядке.

Получите !!!словарь cafes!!! с упорядоченными ключами из отсортированного списка, 
где ключи — названия кафе, 
а значения — их рейтинг.
"""
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

print('task 4.9')
print(f'ratings == {ratings}==')
print('next==')
print(f'sorted(ratings) == {sorted(ratings)}==')
print('next==')

# слак ratings_sort = ratings.sort(key=lambda elem: (-elem[1], elem[0]))
# поиск sorted_by_second = sorted(data, key=lambda tup: tup[1])
# +!!!+ ratings_sort = sorted(ratings, key=lambda tup: tup[1], reverse=True) == ratings_sort = sorted(ratings, key=lambda tup: -tup[1])
# ratings_sort = sorted(ratings, key=lambda elem: -elem[1])
ratings_sort = sorted(ratings, key=lambda elem: (-elem[1], elem[0]))
print(f'ratings.sort(key=lambda... == {ratings_sort}==')
print('next==')

# работает!
# они хотят через другой инструмент
# cafes = dict(ratings_sort)
from collections import OrderedDict
# ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
cafes = OrderedDict(ratings_sort)
print(f'cafes == {cafes}==')

print('next==')

