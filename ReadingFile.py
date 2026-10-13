count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
# writing into file
with open("egFile1.txt","w") as f:
    f.write("hello , this is the first file. /n Finding how many vowels are there")
# reading into file
with open("egFile1.txt","r") as f:
    data=f.read()
    
    for i in data:
        if i in vowels:
            count+=1

print("total vowels in file: ",count)


    