import random

choice=random.randint(0, 5)
if (choice == 0):
    print("Bang!")
    num=1
    while (num<5):
        path="hahaha"+str(num)+".txt"
        open(path, "w")
        num=num+1
    
else:
    print("You win")