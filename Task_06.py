# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

from random import randint

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
data = list(my_favorite_songs.items())
K1, V1 = data [randint(0, len(my_favorite_songs)-1)]


K2, V2 = data [randint(0, len(my_favorite_songs)-1)]


K3, V3 = data [randint(0, len(my_favorite_songs)-1)]
print(f'Случайные песни: {my_favorite_songs[K1]},{my_favorite_songs[K2]},{my_favorite_songs[K3]}')
if V1!=V2!=V3:
    total_leng = V1 + V2 + V3

    print(f'Три песни звучат {"%.2f" % total_leng} минут')
