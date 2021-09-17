def lesson():
    try:
        n_1 = int(input("Введите первое число: "))
        n_2 = int(input("Введите второе число "))
        result = n_1 / n_2
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
        return
    return result


print(lesson())

