
p="python"
l=len(p)
i=0
while i<l:
    k=l
    while k<=i:
        print(" ",end=" ")
        k=k-1
    a=i
    while a>=0:
        print(p[a],end=" ")
        a=a-1
    i=i+1
    print()
