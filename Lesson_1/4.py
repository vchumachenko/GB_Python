n = int(input("Введите целое положительное число: "))
r = 0
while n > 10:
    d = n % 10
    n //= 10
    if d > r:
        r = d
print(r)
