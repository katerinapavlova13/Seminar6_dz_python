# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = "text.txt"
dataTxt = " "

with open(path, "r", encoding="UTF-8") as file:
    dataTxt = file.read()
    dataTxt = dataTxt.split()
print(dataTxt)

findTxt = input("Введите текст для удаления: ")
# resultTxt = []
# for word in dataTxt:
#     if findTxt not in word:
#         resultTxt.append(word)
# print(resultTxt)

# ========= lambda and filter =========
dataTxt = list(filter(lambda x: findTxt not in x, dataTxt))
print(dataTxt)
