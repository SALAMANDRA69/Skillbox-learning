text = input('Введите текст: ')
previous_letter, next_letter = 0, 0

for letter in text + ' ':
    if letter == ' ':
        if next_letter > previous_letter:
            previous_letter = next_letter
        next_letter = 0
    else: next_letter += 1
    
print(f'Самое длинное слово, букв: {previous_letter}.')