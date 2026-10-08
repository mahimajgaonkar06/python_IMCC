import random


num=int(input("enter any number 1 to 10: "))
guess=random.randint(1,10)

if num==guess:
    print("correct-YOU HAVE EARNED A REWARD")
else:
    print("wrong guess")