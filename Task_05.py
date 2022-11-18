# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000

months = 12
debt = 0
i = 0

while i <= months-1:
    debt += expenses - salary
    expenses *= 1.03
    i += 1
print(f'Необходимо в долг взять {"{0:.2f}".format(debt)} рублей')

# Отлично
