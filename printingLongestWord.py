
open("myFile3.txt","x")

with open("myfile3.txt", "w") as f:
    f.write("Python is easy to learn")

with open("myfile3.txt", "r") as f:
    sent = f.read()

words = sent.split()
print("List of words:", words)

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
