a = 42
b = "Hello, world!"
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)

my_list.append(my_list) # так делть нельзя!!! добавлять список сам в себя
print(my_list)
