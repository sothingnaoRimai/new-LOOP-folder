


# 1 
# a b 
# 1 2 3 
# a b c d 
# 1 2 3 4 5 

n=5
i=1
while i<=n:
    j=1
    k=ord("a")
    while j<=i:
        if i%2!=0:
            print(j,end=" ")
        else:
            print(chr(k),end=" ")
            k=k+1
        j=j+1
    i=i+1
    print()



