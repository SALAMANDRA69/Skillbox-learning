# Задача 1. Сумма чисел

# def summa_n(num: int) -> None:
#     sum = int((1 + num) * num / 2)
#     print(f'Сумма чисел от 1 до {num} равна {sum}')


# number = abs(int(input('Введите число: ')))
# if number: summa_n(number)





# Задача 2. Функция в функции

# def positive() -> None:
#     print('Положительное')


# def negative() -> None:
#     print('Отрицательное')


# def test() -> None:
#     number = int(input('Введите число: '))
#     if number > 0:
#         positive()
#     elif number < 0:
#         negative()
#     else:
#         pass

# test()





# Задача 3. Апгрейд калькулятора

def sum_nums(num: int) -> None:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print('Сумма цифр:', sum)


def max_num(num: int) -> None:
    max = 0
    while num > 0:
        if num % 10 > max:
            max = num % 10
        num //= 10
    print('Максимальная цифра:', max)    


def min_num(num: int) -> None:
    min = 9
    while num > 0:
        if num % 10 < min:
            min = num % 10
        num //= 10
    print('Минимальная цифра:', min)


def calculator() -> None:
    while True:
        try:
            number = int(input('Введите число: '))
            action = int(input('''
Введите номер действия:
1 - сумма цифр
2 - максимальная цифра
3 - минимальная цифра: '''))
            if action == 1:
                sum_nums(number)
            elif action == 2:
                max_num(number)
            elif action == 3:
                min_num(number)
            else:
                print(f'\nКоманда "{action}" отсутсвует!\n')
        except ValueError:
            print('\nВы ввели недопустимое значение!\n')

calculator()





# Задача 4. Текстовый редактор

# def count_letters(line: str, figure: int, letter: str) -> None:
#     print(f'\nКоличество цифр {figure}: {line.count(str(figure))}')
#     print(f'Количество букв {letter}: {line.count(letter)}')


# def text_editor() -> None:
#     try:
#         line = input('Введите текст: ')
#         figure = int(input('Какую цифру ищем? '))
#         letter = input('Какую букву ищем? ')
#         if letter.isdigit(): # К СОЖАЛЕНИЮ НЕ УЧИТЫВАЕТ ИНЫЕ СИМВОЛЫ
#             raise ValueError(f'Вы ввели "{letter}", когда необходимо букву!') 
#         count_letters(line, figure, letter)
#     except ValueError as error:
#         print('\nВы ввели недопустимое значение! Ошибка:', error)

# text_editor()





# Задача 5. Недоделка

# def rock_paper_scissors(user_win) -> int:
#     from random import choice
#     print('''\n«Камень, ножницы, бумага»
# Для выхода из игры, введите: Выход''')
#     while True:
#         choices_list = {'камень': 0, 'ножницы': 1, 'бумага': 2}
#         try:
#             user_choice = input('\nВведите - камень, ножницы или бумага: ').lower()
#             if not user_choice in choices_list:
#                 if user_choice == 'выход':
#                     return user_win
#                 else:
#                     raise ValueError('Вы ввели недопустимое значение!')
#             ai_choice = choice(list(choices_list.values()))
#             result = (choices_list[user_choice] - ai_choice) % 3
#             if result == 0:
#                 print('Ничья')
#             elif result == 1:
#                 print('Вы победили!')
#                 user_win += 1
#             else:
#                 print('Компьютер победил')
#         except ValueError as error:
#             print(error)


# def guess_the_number(user_win) -> int:
#     from random import randint
#     print('''\n«Угадай число»
# Для выхода из игры, введите: Выход''')
#     activ_game = True
#     while activ_game:
#         ai_random_num = randint(1, 10)
#         print(f'\nЯ загадал целое число от 1 до 10 (включительно)')
#         while True:
#             try:
#                 user_choice = input('Ты загодал число: ').lower()
#                 if user_choice != 'выход' and not (user_choice.isdigit() == True):
#                     raise ValueError('Вы ввели недопустимое значение!')
#                 elif user_choice == 'выход':
#                     activ_game = False
#                     return user_win
#                 elif int(user_choice) > ai_random_num:
#                     print('Не верно! Моё число меньше.')
#                 elif int(user_choice) < ai_random_num:
#                     print('Не верно! Моё число больше.')
#                 else:
#                     print('Вы угадали!')
#                     user_win += 1
#                     break
#             except ValueError as error:
#                 print(error)
    

# def app() -> None:
#     win = 0
#     while True:
#         print(f'''
# ГЛАВНОЕ МЕНЮ

# Мои победы: {win}

# ВЫБЕРИТЕ ИГРУ ИЛИ ВЫХОД: 
# 1 - «Камень, ножницы, бумага»
# 2 - «Угадай число»
# 0 - Выйти из раздела "Главное меню"                                     
#         ''')
#         try:
#             selection_game = int(input('Введите номер команды: '))
#             if selection_game == 1:
#                 win = rock_paper_scissors(win)
#             elif selection_game == 2:
#                 win = guess_the_number(win)
#             elif selection_game == 0:
#                 print('\nСпасибо за уделенное время! До свидания.')
#                 break
#             else:
#                 print('Такой команды нет!')
#         except ValueError:
#             print('Вы ввели недопустимое значение!')

# app()










# --------------------------------------------------------------------------------------------------------------------------



# def numeral_count(count):
#     max = 0     
#     for i in range(count):
#         num = int(input('Введите число: '))
#         if len(str(max)) < len(str(num)):
#             max = num
#     return max

# count_nums = int(input('Введите кол-во задач: '))


# print(f'Первая задача на обработку: {numeral_count(count_nums)}')







