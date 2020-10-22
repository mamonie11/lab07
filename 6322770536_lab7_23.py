x=""
listeven=[]
listodd=[]
while x!=0:
    x = int(input("Enter an integer(0 to exit): "))
    if x%2==0:
        listeven.append(x)
    else:
        listodd.append(x)
else:
    del listeven[-1]
        
print("-------------------------")
print("The number of even integer is ",len(listeven))
print("The number of odd integer is ",len(listodd))
