films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []

try:
    count_films = int(input('Сколько фильмов хотите добавить? '))
    for _ in range(count_films):
        add_film = input('Введите название фильма: ')
        if add_film in favorite_films:
            print(f'Ошибка: фильм {add_film} уже есть в списке!')
        elif add_film in films:
            favorite_films.append(add_film)
        else:
            print(f'Ошибка: фильма {add_film} у нас нет :(')
    print('Ваш список любимых фильмов:', ', '.join(favorite_films))
except ValueError as error:
    print('Вы ввели не верное значение!')

    
