print("=====MAIN MENU=====")
print("1. Addition")
print("2. Subtraction")
print("3. Exit")
z=0
x=""
y=""
a=int(input("Select an operation (1-3):" ))
if a==3:
    print("Bye!!!")
else:
    x,y=input("Enter two numbers: ").split()

if a==1:
    x=int(x)
    y=int(y)
    z=x+y
    print(x,"+",y,"=",z)
elif a==2:
    x=int(x)
    y=int(y)
    if x>=y:
        z=x-y
        print(x,"-",y,"=",z)
    else:
        z=y-x
        print(y,"-",x,"=",z)

    
