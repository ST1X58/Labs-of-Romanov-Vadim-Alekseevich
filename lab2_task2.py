salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
podushka = 0
count_months = 10
count_months -=1
podushka = podushka + spend - salary
while count_months !=0:
    count_months -= 1
    spend = spend + spend * increase
    podushka = podushka + spend - salary


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",  int(podushka))
