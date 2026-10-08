stud={
        101:{"name":"aditi","scores":[20,30,20]},
        102:{"name":"sam","scores":[50,85,75]},
        103:{"name":"rohan","scores":[30,90,95]}

}

for i,details in stud.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["average"]=avg
    details["passed"]=avg>=50
    print(details["passed"])

# to print names of passed students

for i , details in stud.items():
    if details["passed"]:
        print(details["name"])

stud[104]={"name":"neha","scores":[85,65,74]}