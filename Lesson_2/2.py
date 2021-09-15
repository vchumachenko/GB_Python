elem = input("Введите элементы списка: ").split()
elem[:-1:2], elem[1::2] = elem[1::2], elem[:-1:2]
print(elem)
