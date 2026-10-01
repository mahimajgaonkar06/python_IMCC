for i in range(1,4):
    for j in range(i,4):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()

for i in range(2, 0, -1):

    for j in range(i, 4):
        print(" ", end="")

    for k in range(1, 2*i):
        print("*", end="")

    print()