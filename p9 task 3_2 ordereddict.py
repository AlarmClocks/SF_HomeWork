"""
task 3.2
Дан список из кортежей temps. 
На первом месте в кортеже указан год в виде строки, 
а на втором — средняя температура января в Петербурге в указанном году.

Напишите функцию check(temps), 
которая будет выводить словарь, 
в котором ключи — годы, 
а значения — показатели температуры. 
!!! Ключи необходимо отсортировать в порядке убывания 
соответствующих им температур.

Пример списка temps:
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

Пример вывода:
OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

Пример
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
# Сортируем по второму значению из кортежа, то есть по возрасту
ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(ordered_client_ages)
"""

from collections import deque
from collections import OrderedDict

def check(temps):
    temps.sort(key=lambda x: x[1], reverse=True)
    print(f'temps.sort=={temps}==')
    temp_orderdict = OrderedDict(temps)
    print(temp_orderdict)

    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(f'ordered_temp=={ordered_temp}==')

    return temp_orderdict

# ordered_temp = OrderedDict(sorted(temps, key=lambda x: x[1]))
# print(f'ordered_temp=={ordered_temp}==')

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
print(f'temps=={check(temps)}== None')
# check(temps)


"""
правильное
from collections import OrderedDict
def check(temps):
    temps.sort(key=lambda x: x[1], reverse=True)
    temp_orderdict = OrderedDict(temps)
    print(temp_orderdict)

а это НЕ правильно 
# Введите свое решение ниже
from collections import OrderedDict
def check(temps):
    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(ordered_temp)


Общая статистика
Всего тестов: 2. Пройдено: 0. Не пройдено: 2.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест не пройден ✗

Формулировка:

* Уточнение от автора задачи: Проверяем корректность решения

* Имя проверяемого метода/функции: check

* Аргументы, передаваемые в метод/функцию:


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]


* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите свое решение ниже
from collections import OrderedDict
def check(temps):
    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(ordered_temp)

 

check(temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)])


Ожидаемый ответ:

OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

Ваш ответ:

OrderedDict([('2001', -2.5), ('2002', -4.4), ('2000', -4.4), ('2003', -9.5)])
Тест 2
Тест не пройден ✗

Формулировка:

* Уточнение от автора задачи: Проверяем корректность решения

* Имя проверяемого метода/функции: check

* Аргументы, передаваемые в метод/функцию:


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5), ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4), ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8), ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7), ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5), ('2020', 1.5)]


* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите свое решение ниже
from collections import OrderedDict
def check(temps):
    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(ordered_temp)

 

 
Общая статистика
Всего тестов: 2. Пройдено: 0. Не пройдено: 2.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест не пройден ✗

Формулировка:

* Уточнение от автора задачи: Проверяем корректность решения

* Имя проверяемого метода/функции: check

* Аргументы, передаваемые в метод/функцию:


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]


* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите свое решение ниже
from collections import OrderedDict
def check(temps):
    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(ordered_temp)

 

check(temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)])
Ожидаемый ответ:
OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])
Ваш ответ:
OrderedDict([('2001', -2.5), ('2002', -4.4), ('2000', -4.4), ('2003', -9.5)])


Тест 2
Тест не пройден ✗

Формулировка:

* Уточнение от автора задачи: Проверяем корректность решения

* Имя проверяемого метода/функции: check

* Аргументы, передаваемые в метод/функцию:


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5), ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4), ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8), ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7), ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5), ('2020', 1.5)]


* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите свое решение ниже
from collections import OrderedDict
def check(temps):
    ordered_temp = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(ordered_temp)

 

check(temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5), ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4), ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8), ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7), ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5), ('2020', 1.5)])
Ожидаемый ответ:
OrderedDict([('2020', 1.5), ('2005', -1.6), ('2008', -1.7), ('2007', -2.4), ('2001', -2.5), ('2015', -2.7), ('2018', -2.9), ('2009', -3.5), ('2017', -3.9), ('2000', -4.4), ('2002', -4.4), ('2012', -4.9), ('2011', -5.8), ('2006', -5.9), ('2013', -6.1), ('2019', -6.5), ('2014', -6.9), ('2004', -8.2), ('2003', -9.5), ('2016', -11.2), ('2010', -12.1)])
Ваш ответ:
OrderedDict([('2020', 1.5), ('2005', -1.6), ('2008', -1.7), ('2007', -2.4), ('2001', -2.5), ('2015', -2.7), ('2018', -2.9), ('2009', -3.5), ('2017', -3.9), ('2002', -4.4), ('2000', -4.4), ('2012', -4.9), ('2011', -5.8), ('2006', -5.9), ('2013', -6.1), ('2019', -6.5), ('2014', -6.9), ('2004', -8.2), ('2003', -9.5), ('2016', -11.2), ('2010', -12.1)])
 


"""

