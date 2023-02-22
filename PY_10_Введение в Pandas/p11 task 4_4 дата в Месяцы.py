"""
task 4.4
Представьте, что вы занимаетесь подготовкой данных о вакансиях с платформы hh.ru
В вашем распоряжении имеется таблица, 
в которой с помощью парсинга собраны резюме кандидатов. 
В этой таблице есть текстовый столбец «Опыт работы». 
Пример такого столбца представлен ниже в виде объекта Series. 
Структура текста в столбце фиксирована и не может измениться.

Напишите функцию get_experience(arg), 
аргументом которой является строка столбца с опытом работы. 
Функция должна возвращать опыт работы в месяцах. 
Не забудьте привести результат к целому числу.

Обратите внимание, 
что опыт работы может выражаться только в годах или только в месяцах. 
Учтите это при построении своей функции. 
Кроме того, учтите возможные вариации слов 
месяц (месяца, месяцев) 
и год (года, лет).

Примените вашу функцию к Series experience_col с помощью метода apply().
"""

import pandas as pd
import time # Import time module
 
start = time.time() # record start time

def get_experience(arg):
    print(f'arg={arg}')
    
    month_key_words = ['месяц', 'месяцев', 'месяца'] # варианты в резюме
    year_key_words = ['год', 'лет', 'года'] # варианты в резюме
    
    args_splited = arg.split(' ')
    
    month = 0
    year = 0
    for i in range(len(args_splited)):
        print(f'    i={i}  args_splited[i] ={args_splited[i]}')
        if args_splited[i] in month_key_words:
            month = args_splited[i-1]
            print(f'        month ={args_splited[i-1]}')
        if args_splited[i] in year_key_words:
            year = args_splited[i-1]
            print(f'        year ={args_splited[i-1]}')
    return int(year)*12 + int(month)


test_series_1 = pd.Series([
    'Опыт работы 8 лет 3 месяца',
    'Опыт работы 3 года 5 месяцев',
    'Опыт работы 1 год 9 месяцев',
    'Опыт работы 3 месяца',
    'Опыт работы 6 лет'
])

test_series_2 = pd.Series([
    'Опыт работы 5 лет',
    'Опыт работы 5 месяцев',
    'Опыт работы 1 год 1 месяц',
    'Опыт работы 3 месяца',
    'Опыт работы 7 лет'
])

print(test_series_1.apply(get_experience))
print('===')
print(test_series_2.apply(get_experience))
print('===')

end = time.time() # record end time
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")