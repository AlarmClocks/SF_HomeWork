"""
task 3.5
Вы работаете аналитиком в компании ScienceYou. 
Ваша задача — проанализировать чистую прибыль.
Доходы (income), 
расходы (expenses) и 
годы (years), 
соответствующие им, предоставлены вам в виде списков.

Например:
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

Создайте функцию create_companyDF(income, expenses, years), 
которая возвращает DataFrame, 
составленный из входных данных со столбцами 
Income и Expenses и индексами, 
соответствующими годам рассматриваемого периода.

Пример такого DataFrame представлен ниже.
    Income  Expenses
2018    478     156
2019    512     130
2020    196     270

Также напишите функцию get_profit(df, year), 
которая возвращает разницу между доходом и расходом, 
записанными в таблице df, за год year.

Примечание. 
-Если информация за запрашиваемый год не указана в вашей таблице, вам необходимо вернуть None.
-Не забудьте ипортировать библиотеки.

"""
import numpy as np
import pandas as pd


def get_profit(df, year):
    # возвращает разницу между доходом и расходом, 
    # записанными в таблице df, за год year.
    print(f'    ++def df={df}=    year={year}=')
    
    if year in df.index:
        profit = df.loc[year, 'Income'] - df.loc[year, 'Expenses']
    else:
        profit = None
    return profit

def create_companyDF(income, expenses, years):
    # возвращает DataFrame, 
    # составленный из входных данных со столбцами 
    # Income и Expenses и индексами, 
    # соответствующими годам рассматриваемого периода.
    print(f'    +def income={income}=    expenses={expenses}=    years={years}=')
    
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        #'Profit': (income - expenses)
        },
        index = years
    )
    
    # print(f'    +df={df}=')
    return df


income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]
#df = 0

df = create_companyDF(income, expenses, years)
# print('create_companyDF', create_companyDF(income, expenses, years))
print(f'df={df}=')
print('===')
print('===')
print('create_companyDF', get_profit(df, 2018))
print('===')
print('create_companyDF', get_profit(df, 2019))
print('===')
print('create_companyDF', get_profit(df, 2020))
print('===')
print('create_companyDF', get_profit(df, 2021))
print('===')