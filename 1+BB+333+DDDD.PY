
# 1 
# B B 
# 3 3 3 
# D D D D 
# 5 5 5 5 5 
i=1
while i<=5:
    j=1
    while j<=i:
        if i==2:
            print(chr(66),end=" ")
        elif i==4:
            print(chr(68),end=" ")
        else:
            print(i,end=" ")
        j=j+1
    i=i+1
    print()

