my_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)