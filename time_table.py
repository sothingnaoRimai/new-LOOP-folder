a=int(input("enter no"))
b=int(input("enter no"))
i=a
while i<=b:
    j=a
    while j<=10:
        print(i,"*",j,"=",i+j)
        j=j+1
    i=i+1
    print()