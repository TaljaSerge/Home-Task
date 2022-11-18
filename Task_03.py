# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом


months_day_count = {'1':  31,
                    '2':  28,
                    '3':  31,
                    '4':  30,
                    '5':  31,
                    '6':  30,
                    '7':  31,
                    '8':  31,
                    '9':  30,
                    '10': 31,
                    '11': 30,
                    '12': 31,
                    }


user_input = input("Введите, пожалуйста, номер месяца: ")

month = int(user_input)

if 1 <= month <= 12:
        day_count = months_day_count[user_input]
        print('Вы ввели', month)
        print('Кол-во дней в месяце:', day_count)
else:
        print('Месяца с таким номер не существует.')


# Хорошо. Есть еще вариант
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))




