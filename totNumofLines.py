
# open("myFile2.txt","x")
with open("myfile2.txt","w")as f:
    data=f.writelines("hello this is second file\n reading lines from file into list,\n Printing the total num of lines.\n adding a fourth line.")
    
with open("myFile2.txt","r") as f:
    Lines=f.readlines()
    
print("total num of lines: ",len(Lines))

print("second line: ",Lines[1])
print("4th line: ",Lines[3])

    