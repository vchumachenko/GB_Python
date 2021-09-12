plus = int(input("Введите выручку:"))
minus = int(input("Введите расходы: "))

profit = plus - minus

if plus > minus:
    print(f"Прибыль. Рентабельность выручки: {profit / plus * 100}%. ")
    workers = int(input("Введите количество работников: "))
    print(f"Рентабельность на одного сотрудника: {profit / plus * 100 / workers}%")
else:
    print("Убыток")