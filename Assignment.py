my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list[2] = 15
print(my_list)
my_list.remove(my_list[-1])
print(my_list)
my_list.sort()
print(my_list)
# index = my_list.index(30) - 30 was already removed hence the program crashes
index = my_list.index(20)
print(index)

