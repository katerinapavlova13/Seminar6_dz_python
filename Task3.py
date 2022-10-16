#2. Напишите программу, которая определит позицию второгo вхождения строки в списке
# либо сообщит, что ее нет.

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
str = input("Введите строку для поиска: ")

# list_index = []
# for i in range(len(my_list)):
#     if my_list[i] == str:
#         list_index.append(i)
# print(list_index)
# if len(list_index) > 1:
#     print(f"Второе вхождение эл-та {str} на позиции {list_index[1]}")
# else:
#     print("Нет второго вхождения!")

# ========= с использованием lambda, fiter, enumerate ==============
list_index = list(enumerate(my_list))
list_res = list(filter(lambda x: str in x, list_index))
if len(list_res) > 1:
    print(f"Второе вхождение эл-та {str}, в списке {my_list} на позиции {list_res[1][0]}")
else:
    print("Нет второго вхождения!")
