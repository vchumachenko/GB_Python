# f= input("Введите данные: ")
#
# with open("my_file", 'r+') as file_obj:
#     data = file_obj.writelines()
#
# while f in data:
#     f = input("Введите данные: ")
#     # file_obj.writelines(input("Введите данные, который нужно записать в файл: "))
a = []
while True:
    line = input("Введите данные: ")
    if line == '':
        exit()
    else:
        newline = line + '\n'
        a.append(newline)

    with open("my_file", "w") as file_obj:
        file_obj.writelines(a)
