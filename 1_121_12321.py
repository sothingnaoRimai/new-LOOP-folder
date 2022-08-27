
#     1
#    121
#   12321
#  1234321
# 123454321
# row=int(input("enter no: "))
# for i in range(1,row+1):
#     for j in range(1,row+1-i):
#         print(' ',end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()



# # 1 
# # 1 2 1 
# # 1 2 3 2 1 
# # 1 2 3 4 3 2 1 
# # 1 2 3 4 5 4 3 2 1 
row=int(input("enter no: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()