"""
task 2.4
В аптеку поступают партии лекарств. 
Их названия находятся в списке names, 
количество единиц товара находится в списке counts.

Например:
names = ['chlorhexidine', 'cyntomycin', 'afobazol'] 
counts = [15, 18, 7]

Напишите функцию create_medications(names, counts), 
которая создает Series medications, 
индексами которой являются названия лекарств names,
а значениями - их количество в поставке counts.

также напишите функцию get_percent(medications, name), 
которая возвращает долю количества товара c именем name
от общего количества товаров в поставке в процентах.

Примечание. 
Не забудьте ипортировать библиотеки.

Пример:
names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
medications = create_medications(names, counts)

print(get_percent(medications, "chlorhexidine")) #37.5


"""
import numpy as np
import pandas as pd

def create_medications(names, counts):
    # создает Series medications, 
    # индексами которой являются названия лекарств names,
    # а значениями - их количество в поставке counts
    print(f'    +def names={names}=    counts={counts}=')
    
    """
    medications = pd.Series(data = counts, index = names, name = 'medications')
    print(f'    +def medications={medications}=')
    Ожидаемый ответ:
    chlorhexidine    26
    cyntomycin       18
    afobazol          7
    dtype: int64

    Ваш ответ:
    chlorhexidine    26
    cyntomycin       18
    afobazol          7
    Name: medications, dtype: int64
    """
    medications = pd.Series(data = counts, index = names)
    print(f'    +def medications={medications}=')

    return medications


def get_percent(medications, name):
    # возвращает долю количества товара c именем name
    # от общего количества товаров в поставке в процентах
    print(f'    ++def medications={medications}=')
    print(f'    ++def name={name}=')
    print(f'    ++def medications.loc[name]={medications.loc[name]}=')
    print(f'    ++def sum(medications)={sum(medications)}=')
    
    percent = (medications.loc[name]/sum(medications) * 100)
    print(f'    ++def percent={percent}=')
    
    return percent


names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

medications = create_medications(names, counts)
print('===')
print(get_percent(medications, "chlorhexidine")) #37.5
