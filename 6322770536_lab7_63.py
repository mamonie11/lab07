x=""
list1=[]
list2=[]
while x!="done":
    x=input("enter name: ")
    list1.append(x)
    list1.count(x)
    if list1.count(x)>1:
        list2.append(x)
        
del list1[-1]
print("name list is",sorted(list(set(list1))))
print("duplicated name list is",sorted(list2))
        
