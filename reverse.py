num=int(input("enter binary no:-"))
i=0
b=[]
while num>0:
    d=num%2
    b.append(d)
    num=num//2
b.reverse()
print(d)
for i in range(d+1):
    print(i,end=" ")
