x = ""
list1=[]
while x!="exit":
    x = input('Enter name (enter "exit" to end): ')
    if (x.islower())==True:
        a=x.capitalize()
        list1.append(a)
del list1[-1]
print(list1)
