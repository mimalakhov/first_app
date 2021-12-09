import random

'''Приложение реализует игру "Русская рулетка". 
Если рандомное число совпадёт с нулём, то в домашней директории бесконечно будут создаваться текстовые файлы. 
В противном случае не произойдёт ничего'''

choice=random.randint(0, 5)
if choice == 0: #Плохой исход
    print("Bang!")
    num = 1
    while True: 
        path = "hahaha" + str(num) + ".txt"
        open(path, "w")
        num = num + 1
else: #Хороший исход
    print("You win")