
#finding out vowels from the sentence and counting the number of vowels in it

s=input("write a sentence: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in s:
    if i in vowels:
        count+=1

print("count of vowels: ",count)