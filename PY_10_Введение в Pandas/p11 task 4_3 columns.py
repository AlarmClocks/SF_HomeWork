"""
task 4.3
Преобразуйте столбец SellerG 
с наименованиями риелторских компаний в таблице melb_df следующим образом: 
оставьте в столбце только 49 самых популярных компаний, 
а остальные обозначьте как 'other'.

Найдите, 
во сколько раз минимальная цена объектов недвижимости, 
проданных компанией 'Nelson', 
больше минимальной цены объектов, 
проданных компаниями, обозначенными как 'other'. 
Ответ округлите до десятых.

task 4.2
Напишите функцию get_weekend(weekday), 
которая принимает на вход элемент столбца WeekdaySale и возвращает 1, 
если день является выходным,
и 0 — в противном случае, 
и создайте столбец Weekend в таблице melb_df с помощью неё.

Примените эту функцию к столбцу 
и вычислите среднюю цену объекта недвижимости, 
проданного в выходные дни. 
Результат округлите до целых.

===
#   task 3.3
# Создайте в таблице melb_df признак WeekdaySale (день недели). 
# Найдите, сколько объектов недвижимости было продано в выходные (суббота и воскресенье),
# результат занесите в переменную weekend_count. 
# В качестве ответа введите результат вывода переменной weekend_count.
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
display(melb_df['WeekdaySale'])
saturday_sale = melb_df[(melb_df['WeekdaySale'] == 5)].shape[0]
# sunday_sale = (melb_df['WeekdaySale'] == 6)
sunday_sale = melb_df[(melb_df['WeekdaySale'] == 6)].shape[0]
print(f'saturday_sale={saturday_sale}')
print(f'sunday_sale={sunday_sale}')

weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
print(weekend_count)
"""
import pandas as pd
import time # Import time module
 
start = time.time() # record start time

melb_data = pd.read_csv('PY_10_Введение в Pandas/.jpnb_checkpoints/data/melb_data_ps.csv', sep=',')
# melb_data.head()

melb_df = melb_data.copy()
# melb_df.info()
# melb_df.describe(include=['object'])
print('===')

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
melb_df.info()
print('===')


"""
task 4.2

def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else: 
        return 0
    
    
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
print(round(melb_df[melb_df['Weekend']==1]['Price'].mean(), 2))
"""

# popular_seler = melb_df['SellerG'].value_counts() # list of 268 rows
popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
print(f'popular_seler={popular_seler}')

# заменяем значения улиц, не попавших в список популярных на строку 'other'
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_seler else 'other') 

# popular_trader = melb_df['SellerG'].value_counts() # list of 268 rows
# print(f'popular_trader={popular_trader}')


min_sale_nelson = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min() 
min_sale_other = melb_df[melb_df['SellerG'] == 'other']['Price'].min() 
print(f'min_sale_nelson={min_sale_nelson}')
print(f'min_sale_other={min_sale_other}')
print('nelson/other=', round(min_sale_nelson/min_sale_other, 1))

end = time.time() # record end time
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
