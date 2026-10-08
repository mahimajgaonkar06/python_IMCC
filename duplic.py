
#removing duplicacy from list

org=[1,1,2,3,4,5,5,6,7,7]
new=[]

for i in org:
    if i not in new:
        new.append(i)

print("after removing: ",new)