# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)
print(sum(c.values()))
print(c.values())


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print('next 1')
print(f'counter_moscow=={counter_moscow}==')
print(f'counter_spb=={counter_spb}==')
print(counter_moscow + counter_spb)


counter_moscow.subtract(counter_spb)
print('next=')
print(f'counter_moscow=={counter_moscow}==')
print(f'counter_spb=={counter_spb}==')

print(*counter_moscow.elements())
print(list(counter_moscow))
print(dict(counter_moscow))
print(counter_moscow.most_common())

