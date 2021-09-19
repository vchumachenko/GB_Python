def my_func(inp):
    i = inp.split()
    s = 0

    for el in i:
        if el:
            try:
                if el == "q":
                    return s, False
                else:
                    s += float(el)
            except ValueError:
                continue

    return s, True


x = True
my_sum = 0
while x:
    inp = input("""Введите числа. Чтобы остановить подсчет введите "q": """)
    cs, x = my_func(inp)
    my_sum += cs
    print("Сумма чисел: ", my_sum)
print("Общая сумма: ", my_sum)
