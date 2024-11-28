money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

number_of_months = 0
budget = money_capital    # Оставшиеся деньги

while budget >= spend - salary:
    number_of_months += 1  # Первый месяц без долга
    budget = budget + salary  # Получили зп
    budget = budget - spend   # Потратились
    spend *= 1 + increase #Теперь месячные расходы увеличиваются

print("Количество месяцев, которое можно протянуть без долгов:", number_of_months)
