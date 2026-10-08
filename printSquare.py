
# printing n number of squares 
s=int(input("enter Starting number: "))
n=int(input("Enter ending number: "))
sq=0
for i in range(s,s+n+1):
    sq=i**2
    print("square: ",sq)
