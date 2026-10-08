text=input("enter a string: ")

#uppercase
result=text.upper()
print(result)

# lower
result=text.lower()
print(result)

#capitalize
result=text.capitalize()
print(result)

# strip
result=text.strip()
print(result)

# count
result=text.count("a")
print(result)

# find
result=text.find("python")
print(result)

# replace
result=text.replace("python","Java")
print(result)

# startswith endswith
result=text.startswith("h")
result=text.endswith(".")
print(result)

# split
result=text.split("/")
print(result)

#join
text2=["welcome","to","the","world","of","Python"]
result=text2.join()
print(result)

# partition
result=text.partition("come")
print(result)