# Задача 1. Конвертация

EUR = 1
usd = 1.25 * EUR
rub = 60.87 * usd

buy = int(input('Стоимость покупки в евро: '))
print('Стоимость в рублях:', round(buy * rub, 4))





# Задача 2. Грубая математика

# from math import floor, ceil, log, exp

# count_nums = int(input('Введите кол-во чисел: '))

# for count in range(count_nums):
#     num = float(input('Введите число: '))
#     if num >= 0:
#         num = ceil(num)
#         print(f'x = {num} log(x) = {log(num)}')
#     else:
#         num = floor(num)
#         print(f'x = {num} exp(x) = {exp(num)}')





# Задача 3. Аналог Steam

# from math import ceil

# size = int(input('Укажите размер файла для скачивания: '))
# speed = int(input('Какова скорость вашего соединения: '))

# try:
#     for sec in range(1, ceil(size / speed) + 1):
#         download = sec * speed
#         progress = ceil(download / size * 100)
#         if download == ceil(size / speed) * speed:
#             download, progress = size, 100
#         print(f'Прошло {sec} сек. Скачано {download} из {size} Мб ({progress}%)')

# except ZeroDivisionError:
#     print('Отсутствует подключение к интернету! Проверьте сетевое соединение!')




# Задача 4. Первая цифра

# num = float(input('Введите число: '))
# print('Первая цифра после десятичной точки:', int(num * 10 % 10))





# Задача 5. Вот это объёмы!

# from math import pi

# V_EARTH = 1.08321 * 10 ** 12 # км3
# num = float(input('Введите радиус случайной планеты: '))

# v_planet = 4 * pi * num**3 / 3

# try:
#     if V_EARTH > v_planet:
#         print(f'Объём планеты Земля больше в {round(V_EARTH / v_planet, 3)} раз')
#     else:    
#         print(f'Объём планеты Земля меньше в (1/{round(V_EARTH / v_planet, 3)}) = {round(1 / (V_EARTH / v_planet), 3)} раз')

# except ZeroDivisionError:
#     print(f'Объём планеты Земля больше в {V_EARTH} раз')