shift = int(input('Сдвиг:' ))
numbers =  [1, 2, 3, 4, 5]
print('Изначальный список:', numbers)
for _ in range(shift):
    numbers.insert(0, numbers.pop())
print('Сдвинутый список:', numbers)