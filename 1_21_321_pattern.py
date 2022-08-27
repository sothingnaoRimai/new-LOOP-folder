
        # 1 
        # 2 1 
        # 3 2 1 
        # 4 3 2 1 
        # 5 4 3 2 1 
n=5
i=1
while i<=n:
    j=n-1
    while j>=1:
        print(" ",end=" ")
        j=j-1
    a=i
    while a>=1:
        print(a,end=" ")
        a=a-1
    i=i+1
    print()
