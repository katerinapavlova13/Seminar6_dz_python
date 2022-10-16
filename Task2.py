#1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# Для N = 5: 1. -3. 9. -27. 81.

n = int(input("Введите число: "))

# def posled(n):
#     list = []
#     for i in range(0, n):
#         list.append((-3) ** i)
#     return list
# list = posled(n)
# print(list)

# ============== map and lambda ==========================
new_list = list(map(lambda x: (-3)**x, range(n)))
print(new_list)