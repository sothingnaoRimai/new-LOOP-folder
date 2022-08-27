n=5
i=1
while i<=n:
    j=n
    while j>=i:
        print("",end=" ")
        j=j-1
    a=1
    while a<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(a, end=" ")
        a=a+1
    i=i+1
    print()