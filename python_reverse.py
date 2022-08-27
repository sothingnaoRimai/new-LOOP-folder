
p="python"
l=len(p)
i=0
while i<l:
    j=l
    while j>=i:
        print(" ",end=" ")
        j=j-1
    a=i
    while a>=0:
        print(p[a],end=" ")
        a=a-1
    i=i+1
    print()