violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]]
favourites_songs = []

count_song = int(input('Сколько песен выбрать? '))

for num in range(count_song):
    add_song = input(f'Название {num + 1}-й песни: ')
    for song in violator_songs:
        if add_song in song:
            favourites_songs.append(song)

time_songs = 0
for time in favourites_songs:
    time_songs += time[1]
print(f'Общее время звучания песен — {time_songs} минуты')

