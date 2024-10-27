money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0

while True:
    budget = money_capital + salary

    if budget >= spend:
        count += 1
        money_capital += salary - spend
        spend *= (1 + increase)
    else:
        break


print("Количество месяцев, которое можно протянуть без долгов:", count)
