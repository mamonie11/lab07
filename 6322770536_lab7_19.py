digit=int(input("Enter an integer number: "))

def startwithX():
    x=0
    y=0
    while x<digit:
        print("x",end=" ")
        x+=1
        if x==digit:
            break
        print("o",end=" ")
        x+=1

def startwithO():
    x=0
    y=0
    while x<digit:
        print("o",end=" ")
        x+=1
        if x==digit:
            break
        print("x",end=" ")
        x+=1


if (digit%2)!=0:
    line=0
    while line<digit:
        startwithX(),print(end="\n")
        line+=1
        if line==digit:
            break
        startwithO(),print(end="\n")
        line+=1

elif (digit%2)==0:
    line=0
    while line<digit:
        startwithO(),print(end="\n")
        line+=1
        if line==digit:
            break
        startwithX(),print(end="\n")
        line+=1