
# Create a new file and write text
with open("myfile4.txt", "w") as f:
    f.write("Python is easy and Python is interesting")

# Reading the file
with open("myfile4.txt", "r") as f:
    data = f.read()

# Spliting content into words and store in a list
words = data.split()

# Total number of words
print("Total number of words:", len(words))

# Print unique words
unique = []

for i in words:
    if i not in unique:
        unique.append(i)

print("Unique words:", unique)
