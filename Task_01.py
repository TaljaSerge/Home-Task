# Задача 1
# Есть строка с перечислением песен

from tkinter import N


my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

my_favorite_songs = my_favorite_songs.split(",")

print(f' Первая песня - {my_favorite_songs[0]}\n Последняя песня - {my_favorite_songs[-1]}\n Вторая песня - {my_favorite_songs[1]}\n Вторая песня c  конца- {my_favorite_songs[-2]}')





# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.