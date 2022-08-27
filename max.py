

n=int(input("enter no:"))
i=1
while i<=n:
    max=int(input("enter the no:"))
    if max>=n:
        n=max
    i=i+1        
# print("minimum no is",n)
print("maximum no is",n)