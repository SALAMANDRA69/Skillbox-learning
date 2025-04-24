# Задача 1. «Я стал новым пиратом!»

words = []
find_word = 'Карамба'
for number in range(10):
    word = input(f'Введите слово {number + 1}: ')
    words.append(word.lower())
print(f'Слово {find_word} крикнули: {words.count(find_word.lower())} раз(а)')

# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
words = input('Введите слова через пробел: ').lower().split() # СЛОВ МОЖНО ВВОДИТЬ КАК БОЛЬШЕ ТАК И МЕНЬШЕ 10
print(f'Слово {find_word} крикнули: {words.count(find_word.lower())} раз(а)')





# Задача 2. Театр

# row = int(input('Введите кол-во рядов: '))
# seat = int(input('Введите кол-во сидений в ряде: '))
# distance = int(input('Введите кол-во метров между рядами: '))

# print('\nСцена', end='\n' * 2)

# for number_row in range(row):
#     print('=' * seat, '*' * distance, '=' * seat,)





# Задача 3. Марсоход-2

# width = 0, 20
# height = 0, 20
# position = [8, 10]
# count_move = 0   

# while True:
#     print(f'[Программа]: Марсоход находится на позиции {position[0]}, {position[1]}, введите команду: ')
#     command = input('[Оператор]: ')
    
#     if command == 'A' and position[0] - 1 >= width[0]:
#         position[0] -= 1
#     elif command == 'D' and position[0] + 1 <= width[1]:
#         position[0] += 1
#     elif command == 'S' and position[1] - 1 >= height[0]:
#             position[1] -= 1
#     elif command == 'W' and position[1] + 1 <= height[1]:
#             position[1] += 1

#     # ВЫХОД ИЗ ЦИКЛА С ДОПОЛНЕНИЕМ :)

#     # if command in ('A', 'D', 'S', 'W'):
#     #     count_move += 1
#     #     if count_move == 20:
#     #         print('У Вас зокончелись бесплатные ходы. Купите подписку, что бы продолжить игру!')
#     #         break
    




# Задача 4. Великий и могучий

# text = input('Введите текст: ').split(' ')
# print(f'Самое длинное слово, букв: {len(max(text))}.')





# Задача 5. Коровы

# milk = 0
# stalls = input('Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:\n')
# for number, stall in enumerate(stalls, start=1):
#     if stall == 'b':
#         milk += number * 2
# print('Произведено молока за день:', milk)