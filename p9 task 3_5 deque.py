"""
В Codeboard ниже в списке users содержатся номера пользователей, которые ожидают ответа от сервера (номера могут повторяться). 
Превратите этот список в очередь и выполните задания 3.5-3.7.

task 3.5
Извлеките элемент из начала очереди. 
Запишите полученное значение элемента в качестве ответа.

task 3.6
В уже модифицированной очереди 
переместите пять элементов из начала очереди в её конец. 
Извлеките последний элемент из очереди. 
Запишите полученное число в качестве ответа.

task 3.7
Сколько задач с тем номером, 
что был извлечён в предыдущем задании, 
осталось в модифицированной очереди? 
Запишите ответ в числовой форме.

!!! Примечание: 
Не забывайте добавлять print к своему коду, 
если хотите увидеть результат.

"""

# Следующая строка необходима для системной работы редактора.
# В ней импортируются объекты, которые могут вам понадобиться при выполнении некоторых заданий в процессе прохождения курса.
# Не удаляйте этот импорт!
# from hidden import *

# Ваш код здесь
from collections import deque

users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
print(f'users=={users}')

dq_users = deque(users)
print(f'dq=={dq_users}')

# task 3.5 Извлеките элемент из начала очереди. 
first_client = dq_users.popleft()
print("task 3.5 1st client:", first_client)
print(f'now dq=={dq_users}')

# task 3.6
# В уже модифицированной очереди 
# переместите пять элементов из начала очереди в её конец. 
# Извлеките последний элемент из очереди. 
# Запишите полученное число в качестве ответа.
# Отрицательное значение аргумента переносит
# n элементов из начала в конец
dq_users.rotate(-5)
print(f'now dq_users.rotate(-5)=={dq_users}')
last_client = dq_users.pop()
print("task 3.6 last client:", last_client)
print(f'after pop() dq=={dq_users}')

"""
print(f'users=={users}')

dq_users = deque(users)
print(f'dq=={dq_users}')

first_client = dq_users.popleft()
print("task 3.5 1st client:", first_client)
print(f'now dq=={dq_users}')

dq_users.rotate(-5)
print(f'now dq_users.rotate(-5)=={dq_users}')
last_client = dq_users.pop()
print("task 3.6 last client:", last_client)
print(f'after pop() dq=={dq_users}')

print("task 3.7 How much task:", dq_users.count(last_client))
"""


# task 3.7
# Сколько задач с тем номером, 
# что был извлечён в предыдущем задании, 
# осталось в модифицированной очереди? 
# Запишите ответ в числовой форме.
print("task 3.7 How much task:", dq_users.count(last_client))