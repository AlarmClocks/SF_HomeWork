ЗАДАНИЕ 2.3

from hidden import clients
from collections import Counter

c = Counter(clients)
print(c.most_common(1))
ЗАДАНИЕ 2.4

from hidden import clients
from collections import Counter
c = Counter(clients)
print(c[953421102])
ЗАДАНИЕ 2.5

from hidden import clients
from collections import Counter
c = Counter(clients)
print(len(list(c)))
ЗАДАНИЕ 2.8

from hidden import mystery
print(mystery['any_key'])
# deque([])
Вернуться в юнит 2 →

3. Модуль Collections. Deque и OrderedDict
ЗАДАНИЕ 3.2

from collections import OrderedDict
temps.sort(key=lambda x: x[1], reverse=True)
od = OrderedDict(temps)
print(od)
ЗАДАНИЕ 3.5

from hidden import users
from collections import deque
users = deque(users)
user_id = users.popleft()
print(user_id)
ЗАДАНИЕ 3.6

from hidden import users
from collections import deque
users = deque(users)
user_id = users.popleft()
# Окончание копии предыдущего решения
users.rotate(-5)
user_id = users.pop()
print(user_id)
ЗАДАНИЕ 3.7

from hidden import users
from collections import deque
users = deque(users)
user_id = users.popleft()
users.rotate(-5)
user_id = users.pop()
# Окончание копии предыдущего решения
print(users.count(user_id))
Вернуться в юнит 3 →

4. Модуль Collections. Закрепление знаний
ЗАДАНИЕ 4.3

from collections import deque

def brackets(line):
    # Напишите тело функции
    stack = deque()
    for i in line:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False
ЗАДАНИЕ 4.4

north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
print(len(north_list))
# 500
print(len(south_list))
# 478
print(len(center_list))
# 548
ЗАДАНИЕ 4.5

from collections import Counter
north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
 
c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
 
print(n.most_common()[-1])
# ('Cheese', 10)
ЗАДАНИЕ 4.6

from collections import Counter
north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
print(c - n)
# Counter({'Meat': 31, 'Cheese': 29, 'Bread': 23,
# 'Chips': 22, 'Milk': 21, 'Ketchup': 19, 'Chocolate': 2})
ЗАДАНИЕ 4.7

from collections import Counter
north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
print(c - (n + s))
# Counter()
print(n - (s + c))
# Counter({'Cola': 6})
print(s - (c + n))
# Counter()
ЗАДАНИЕ 4.8

from collections import Counter
north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)
print((s + c + n).most_common()[1])
# ('Bread', 240)
ЗАДАНИЕ 4.9

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)
ЗАДАНИЕ 4.10

from collections import deque, defaultdict

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
Вернуться в юнит 4 →

6. Модуль NumPy. Массивы
ЗАДАНИЕ 6.8

print(mystery.ndim)
ЗАДАНИЕ 6.9

print(max(mystery.shape))
ЗАДАНИЕ 6.10

print(mystery.size)
ЗАДАНИЕ 6.11

print(mystery.dtype)
# float16
ЗАДАНИЕ 6.12

print(mystery.itemsize * mystery.size)
# 420
Вернуться в юнит 6 →

7. Модуль NumPy. Действия с массивами
ЗАДАНИЕ 7.2

try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery
# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]
# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]
# В переменную line_4 сохраните строку 4
line_4 = mystery[3]
# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:, -2]
# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
# Результат сохраните в переменную part
part = mystery[1:4, 2:5]
#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[::-1, -1]
# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()
ЗАДАНИЕ 7.4

try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery
import numpy as np
# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)
# Скопируйте массив `mystery` в массив `mystery_new`. Заполните пропущенные
# значения в массиве `mystery_new` нулями
mystery_new = mystery
mystery_new[nans_index] = 0
# Поменяйте тип данных в массиве mystery на int32
mystery_int = np.int32(mystery)
# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)
# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3), order='F')
#  Сохраните в переменную col столбец 2
col = table[:, 1]
Вернуться в юнит 7 →

8. Модуль NumPy. Операции с векторами
ЗАДАНИЕ 8.4

a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])
 
len_a = np.linalg.norm(a)
len_b = np.linalg.norm(b)
len_c = np.linalg.norm(c)
 
len_a_b = np.linalg.norm(a + b)
len_b_c = np.linalg.norm(b + c)
len_a_c = np.linalg.norm(a + c)
 
print(len_a_b == len_a + len_b)
# False
print(len_b_c == len_b + len_c)
# False
print(len_a_c == len_a + len_c)
# True
ЗАДАНИЕ 8.5

a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])
 
len_a_b = np.linalg.norm(a - b)
len_b_c = np.linalg.norm(b - c)
len_a_c = np.linalg.norm(a - c)
 
print(len_a_b)
# 85.901105930017
print(len_b_c)
# 120.6358155772986
print(len_a_c)
# 49.13247398615299
ЗАДАНИЕ 8.6

import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])
 
dot_a_b = np.dot(a, b)
dot_b_c = np.dot(b, c)
dot_a_c = np.dot(a, c)
 
print(dot_a_b)
# 34
print(dot_b_c)
# 68
print(dot_a_c)
# 4828
ЗАДАНИЕ 8.7

from hidden import mystery
import numpy as np
print(np.min(mystery))
# 5
ЗАДАНИЕ 8.8

from hidden import mystery
import numpy as np
print(np.mean(mystery))
# 490.368
ЗАДАНИЕ 8.9

from hidden import mystery
import numpy as np
print(np.median(mystery))
# 491.0
ЗАДАНИЕ 8.10

from hidden import mystery
import numpy as np
print(np.std(mystery))
# 289.01097656663495
Вернуться в юнит 8 →

9. Модуль NumPy. Случайные числа
ЗАДАНИЕ 9.6

# Не забудьте импортировать numpy и сразу задать seed 2021
import numpy as np
np.random.seed(2021)
# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand()
# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)
# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))
# В переменную even сохраните чётные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)
# Скопируйте even в переменную mix. Перемешайте числа в mix так,
# чтобы массив mix изменился
mix = even
np.random.shuffle(mix)
# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, replace=False, size=3)
# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
Вернуться в юнит 9 →

10. Модуль NumPy. Закрепление знаний
ЗАДАНИЕ 10.5

from hidden import x, y
# Пишите здесь команды, который помогут
# найти ответы на вопросы
import numpy as np
print(np.int64(x) + np.int64(y))
# 4294954884
ЗАДАНИЕ 10.6

import numpy as np

def get_chess(a):
    arr = np.zeros((a, a))
    arr[1::2, ::2] = 1
    arr[::2, 1::2] = 1
    return arr
ЗАДАНИЕ 10.7

import numpy as np

def shuffle_seed(array):
    seed = np.random.randint(2 ** 32)
    np.random.seed(seed)
    result = np.random.permutation(array)
    return result, seed
ЗАДАНИЕ 10.8

import numpy as np

def min_max_dist(*vectors):
    dists = list()
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            dists.append(np.linalg.norm(vectors[i] - vectors[j]))
    return (min(dists), max(dists))
ЗАДАНИЕ 10.9

import numpy as np

def any_normal(*vectors):
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if np.dot(vectors[i], vectors[j]) == 0:
                return True
    return False
ЗАДАНИЕ 10.10

import numpy as np

def get_loto(num):
    loto = np.random.randint(1, 101, size=(num, 5, 5))
    return loto
ЗАДАНИЕ 10.11

import numpy as np

def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
    res = np.array(res)
    return res