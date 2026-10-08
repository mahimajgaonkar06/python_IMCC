List=[2,4,1,5,3,7,6,8,0,9]
sum=0
# printing sum
for i in range(6,10):
    sum+=List[i]
print(sum)

# max min
List.sort()
print("min element: ",List[0])
print("max element: ",List[-1])

#inserting elem
new=List[3]%3
List.insert(6,new)
print(List)
