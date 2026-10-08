s="mahi"
vowels=['a','e','i','o','u','A','E','I','O','U']

for i in s:
    if i in vowels:
        s=s.replace(i,"z")

print(s)
