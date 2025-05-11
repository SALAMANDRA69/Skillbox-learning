shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300], 
    ['педаль', 100], ['седло', 1500], ['рама', 12000], 
    ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input('Название детали: ')
count_detail = 0
sum_detail = 0
for detail in shop:
    if detail[0] == name_detail:
        count_detail += 1
        sum_detail += detail[1]
        
print('Количество деталей:', count_detail)
print('Общая стоимость:', sum_detail)