sizes_rollers = []
sizes_legs = []

count_rollers = int(input('Количество роликов: '))
for roller in range(count_rollers):
    size = int(input(f'Размер пары {roller + 1}:'))
    sizes_rollers.append(size)

count_humans = int(input('Количество людей: '))
for human in range(count_humans):
    size = int(input(f'Размер ноги человека {human + 1}:'))
    sizes_legs.append(size)

for size in sizes_rollers:
    for size_leg in sizes_legs:
        if size == size_leg:
            pass
# Наибольшее количество людей, которые могут взять ролики: 2