numbers = [2, 1, 0, -1, -2]
print('Изначальный список:', numbers) 
count = 0

for index in range(len(numbers)):
    while True:
        for num1 in numbers[index + 1:]:
            if numbers[index] > num1:
                count += 1
        if count > 0:
            numbers.insert(index + count, numbers.pop(index))
            count = 0
        else: break
        
print('Отсортированный список:', numbers)