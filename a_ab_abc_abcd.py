
n=int(input("enter no of rows"))
i=1
while i<=n:
    j=1
    k=ord("a")
    while j<=i:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()