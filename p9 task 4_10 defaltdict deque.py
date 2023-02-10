"""
task 4.10
Напишите функцию task_manager(tasks), 
которая принимает список задач tasks для нескольких серверов. 
Каждый элемент списка состоит из 
кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).

Функция должна создавать словарь
и заполнять его задачами по следующему принципу: 
название сервера — ключ, по которому хранится очередь задач для конкретного сервера.

Если поступает задача без высокого приоритета 
(последний элемент кортежа — False), добавить номер задачи в конец очереди. 
Если приоритет высокий, добавить номер в начало.

Для словаря используйте defaultdict, для очереди — deque.

!!!Функция возвращает полученный словарь с задачами.

Пример
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})


ИзСлака
обратимся к заданию, у нас в качестве результата работы функции 
должна возвращаться следующая структура:
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]), 'office': deque([36871, 40690, 33850])})
Поэтому при создании объекта defaultdict 
в круглых скобках необходимо передать параметр deque.
result = defaultdict(deque)
Далее нам необходимо организовать цикл по элементам списка (кортежам). 
В данном цикле мы проверяем какой приоритет у задачи 
(третий элемент каждого кортежа - булево значение).
for task in tasks:
    # если приоритет высокий (true)
    if task[-1]:
        # по ключу названия сервера добавляем номер задачи в начало очереди
        result[task[1]].appendleft(task[0])
    else:
        # иначе добавляем номер задачи в конец очереди
        result[task[1]].append(task[0])
"""
from collections import deque
from collections import defaultdict
from collections import OrderedDict

def task_manager(tasks):
    print(f'    def task_manager(tasks) == {tasks}==')
    servers = defaultdict(deque) # создаем новый пустой словарь = список очередей
        
    for task, server, priority in tasks:
        print(f'        task={task}=    server={server}=    priority={priority}')
        if priority == True:
            servers[server].appendleft(task)
        else:
            servers[server].append(task)
            
    # ordered_servers = OrderedDict(sorted(servers, key=lambda x: x[0]))
    # print(f'    finish servers == {ordered_servers}==')
    #finish servers == defaultdict(<class 'collections.deque'>, {'office': deque([36871, 40690, 33850]), 'voltage': deque([41667, 35364])})==
    
    return servers


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})