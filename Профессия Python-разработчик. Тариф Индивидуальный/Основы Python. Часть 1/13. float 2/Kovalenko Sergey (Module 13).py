# Задача 1. Урок информатики — 2

# def convert(num: float) -> str:
#     if 0 < num < 1:
#        return f'x = {float(str(num).lstrip('0').lstrip('.')) / 10} * 10 ** -{len(str(num)) - 3}'
#     elif num > 1:
#         return f'x = {num / 10 ** (len(str(num)) - 3)} * 10 ** {len(str(num)) - 3}'
#     else:
#         return 'Вы ввели число меньше нуля!'
    
# number = float(input('Введите число: '))
# result = convert(number)
# print(result)




# Задача 2. Функция максимума

# def maximum_of_two(num_1: int, num_2: int) -> int:
#     return max(num_1, num_2)

# def maximum_of_three(num_1: int, num_2: int, num_3: int) -> int:
#     return maximum_of_two(maximum_of_two(num_1, num_2), num_3)

# number_1 = int(input('Введите число: '))
# number_2 = int(input('Введите число: '))
# number_3 = int(input('Введите число: '))

# max_number = maximum_of_three(number_1, number_2, number_3)
# print('Самое большое число:', max_number)




# Задача 3. Число наоборот

# def get_reverse_number(first_num: int, second_num: int) -> tuple:
#     return int(str(first_num)[::-1]), int(str(second_num)[::-1])

# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))

# first_reverse_number, second_reverse_number =  get_reverse_number(first_number, second_number)
# print('Первое число наоборот:', first_reverse_number)
# print('Второе число наоборот:', second_reverse_number)




# Задача 4. Недоделка-2

# def count_numbers(temp: int) -> int:
#     num_count = 0
#     while temp > 0:
#         num_count += 1
#         temp = temp // 10
#     return num_count


# def change_number(number: int) -> int:
#     last_digit = number % 10
#     first_digit = number // 10 ** (count_numbers(number) - 1)
#     between_digits = number % 10 ** (count_numbers(number) - 1) // 10
#     number = last_digit * 10 ** (count_numbers(number) - 1) + between_digits * 10 + first_digit
#     return number


# def main() -> None:

#     first_n = int(input("Введите первое число: "))
#     if count_numbers(first_n) < 3:
#         print("В первом числе меньше трёх цифр.")
#     else: 
#         print('Изменённое первое число:', change_number(first_n))

#         second_n = int(input("\nВведите второе число: "))
#         if count_numbers(second_n) < 4:
#             print("Во втором числе меньше четырёх цифр.")
#         else:
#             print('Изменённое второе число:', change_number(second_n))

#             print('\nСумма чисел:', change_number(first_n) + change_number(second_n))

# main()
        
        
        
# Задача 5. Маятник

# def the_numbers_of_swings_the_pendulum(initial_amplitude: float, amplitude_stop: float) -> int:
#     attenuation_pendulum = 8.4 / 100
#     count = 0
#     current_amplitude = initial_amplitude
#     while current_amplitude > amplitude_stop:
#         count += 1
#         current_amplitude = current_amplitude - (current_amplitude * attenuation_pendulum)

#     return count


# initial_amplitude = float(input('Введите начальную амплитуду: '))
# if initial_amplitude > 0:
#     amplitude_stop = float(input('Введите амплитуду остановки: '))
#     if amplitude_stop < initial_amplitude:
#         print(f'Маятник считается остановившимся через {the_numbers_of_swings_the_pendulum(initial_amplitude, amplitude_stop)} колебаний')










