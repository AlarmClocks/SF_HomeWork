ЗАДАНИЕ 0.5

simplelist = [19, 242, 14, 152, 142, 1000]
sum(simplelist)/len(simplelist)
Вернуться в юнит 0 →

2. Pandas.Series
ЗАДАНИЕ 2.4

import pandas as pd
def create_medications(names, counts):
    medications = pd.Series(index=names, data=counts)
    return medications
def get_percent(medications, name):
    return(medications.loc[name]/sum(medications) * 100)
Вернуться в юнит 2 →

3. Pandas.DataFrame
ЗАДАНИЕ 3.5

import pandas as pd
def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        },
        index = years
    )
    return df
def get_profit(df, year):
    if year in df.index:
        profit = df.loc[year, 'Income'] - df.loc[year, 'Expenses']
    else:
        profit=None
    return profit
Вернуться в юнит 3 →

5. Знакомимся с данными: недвижимость
ЗАДАНИЕ 5.1

melb_data.loc[15, 'Price']
ЗАДАНИЕ 5.2

melb_data.loc[90, 'Date']
ЗАДАНИЕ 5.3

round(melb_data.loc[3521, 'Landsize'] / melb_data.loc[1690, 'Landsize'])
Вернуться в юнит 5 →

6. Исследование структуры DataFrame
ЗАДАНИЕ 6.8

melb_data.describe(include=['object'])
ЗАДАНИЕ 6.9

melb_data['Type'].value_counts(normalize=True)
Вернуться в юнит 6 →

7. Статистические методы
ЗАДАНИЕ 7.2

melb_data['Propertycount'].max()
ЗАДАНИЕ 7.3

round(melb_data['Distance'].std())
ЗАДАНИЕ 7.4

building_median = melb_data['BuildingArea'].median() 
building_mean =  melb_data['BuildingArea'].mean()
deviance = abs(building_median - building_mean)/building_mean
print(round(deviance * 100, 2))
ЗАДАНИЕ 7.6

melb_data['Bedroom'].mode()
Вернуться в юнит 7 →

8. Фильтрация данных в DataFrame
ЗАДАНИЕ 8.1

melb_data[melb_data['Bathroom'] == 0].shape[0]
ЗАДАНИЕ 8.2

melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3e6)].shape[0]
ЗАДАНИЕ 8.3

melb_data[(melb_data['BuildingArea'] == 0)]['Price'].min()
ЗАДАНИЕ 8.4

round(melb_data[(melb_data['Price']<1e6) & ((melb_data['Rooms']>5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean())
ЗАДАНИЕ 8.5

melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)]['Regionname'].mode()
Вернуться в юнит 8 →

9. Закрепление знаний
ЗАДАНИЕ 9.1

student_data.shape[0]
ЗАДАНИЕ 9.2

student_data.loc[155, 'writing score']
ЗАДАНИЯ 9.3, 9.4, 9.5

student_data.info()
ЗАДАНИЕ 9.6

int(student_data['math score'].mean())
ЗАДАНИЕ 9.7

student_data['race/ethnicity'].mode()
ЗАДАНИЕ 9.8

round(student_data[student_data['test preparation course'] == 'completed']['reading score'].mean())
ЗАДАНИЕ 9.9

student_data[student_data['math score'] == 0].shape[0]
ЗАДАНИЕ 9.10

student_data[student_data['lunch'] == 'standard']['math score'].mean()
student_data[student_data['lunch'] == 'free/reduced']['math score'].mean()
ЗАДАНИЕ 9.11

student_data["parental level of education"].value_counts(normalize=True)
ЗАДАНИЕ 9.12

a = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
b = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean()
print(round(abs(a - b)))