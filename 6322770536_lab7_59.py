print("Shopping List");print("this program stores your shopping list and then displays it")
listshop=[]
x=" "
while x!="":
    x=input("Please enter an item for your list: ")
    listshop.append(x)
del listshop[-1]
print()
print("Shopping List")
print()
for i in listshop:
    print(i)
