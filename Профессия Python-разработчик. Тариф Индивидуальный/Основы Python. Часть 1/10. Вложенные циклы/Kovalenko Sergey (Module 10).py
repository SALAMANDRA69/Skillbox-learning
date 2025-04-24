# Задание 1. Тестовое задание

height = 6 # КОЛ-ВО СТРОК
for row in range(height):
    for coll in range(height):
        print(coll + coll + row, end='\t')
    print()



# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ ЗАДАЧИ 1

# height = 6 # КОЛ-ВО СТРОК
# for row in range(height):
#     for coll in range(row, row + 11, 2):
#         print(coll, end='\t')
#     print()





# Задание 2. Лестница

# number = int(input('Введите число: '))

# for row in range(number): # range(1, number + 1):
#     for coll in range(row + 1): # "+ 1" delete
#         print(row + 1, end='\t') # "+ 1" delete
#     print()





# Задание 3. Рамка

# width = int(input('Введите ширину рамки: '))
# height = int(input('Введите высоту рамки: '))

# for row in range(1, height + 1):
#     for coll in range(1, width + 1):
#         if coll == 1 or coll == width:
#             print('|', end='')
#         elif row == 1 or row == height:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()    



# ЭТА ЖЕ ЗАДАЧА С ОДНИМ ЦИКЛОМ for

# width = int(input('Введите ширину рамки: '))
# height = int(input('Введите высоту рамки: '))

# for row in range(height):
#     if row == 0 or row + 1 == height:
#         print(f'|{'-' * (width - 2)}|')
#     else:
#         print(f'|{' ' * (width - 2)}|')





# Задание 4. Простые числа

# count_numbers = int(input('Введите количество чисел: '))
# count_simple_num = 0

# for number in range(count_numbers):
#     input_num = int(input('Введите число: '))
#     for divider in range(2, input_num + 1): # МОЖНО -> range(2, input_num):
#         if input_num % divider == 0 and input_num != divider: # ТОГДА УБРАТЬ -> and input_num != divider
#             break
#         elif divider == input_num: # ДОБАВИТЬ -> or divider == 2
#             count_simple_num += 1

# print('Количество простых чисел в последовательности:', count_simple_num)





# Задание 5. Наибольшая сумма цифр

# count_nums = int(input('Введите количество чисел: '))
# max_sum_num, value = 0, 0

# for number in range(count_nums):
#     input_num = int(input('Введите число: '))
#     sum_num = 0 
#     for str_num in str(input_num):
#         sum_num += int(str_num)
#         if sum_num > max_sum_num:
#             max_sum_num = sum_num
#             value = input_num
       
# print(f'Число {value} имеет максимальную сумму цифр: {max_sum_num}' )





# Задание 6. Треугольник из хештегов

# height = int(input('Введите высоту пирамиды: '))
# for row in range(height):
#     print(f'{' ' * (height - row - 1)} {'#' * (row * 2 + 1)}')