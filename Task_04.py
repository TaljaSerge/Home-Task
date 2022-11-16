#Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]



from random import randint
a_dict_ = {}

for a in my_favorite_songs: # перебор значений списка
    key = a[0] # ключ
    arr = [a[1]] # значение
    a_dict_[key] = arr # добавление

data = list(a_dict_.items())
K1, V1 = data [randint(0, len(a_dict_)-1)]


K2, V2 = data [randint(0, len(a_dict_)-1)]


K3, V3 = data [randint(0, len(a_dict_)-1)]
print(f'Случайные песни: {a_dict_[K1]},{a_dict_[K2]},{a_dict_[K3]}')
if V1!=V2!=V3:
    total_leng = V1 + V2 + V3

    print(f'Три песни звучат {"%.2f" % sum(total_leng)} минут')





