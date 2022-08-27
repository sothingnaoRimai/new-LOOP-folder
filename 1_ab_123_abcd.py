
# 1
# A B 
# 1 2 3 
# A B C D 
# 1 2 3 4 5 
n=6
i=1
while i<n:
    j=1
    k=ord("A")
    while j<=i:
        if i%2!=0:
            print(j,end=" ")
        else:
            print(chr(k),end=" ")
            k+=1
        j+=1
    i+=1
    print()
