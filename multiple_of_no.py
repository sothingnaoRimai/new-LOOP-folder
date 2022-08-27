
num=int(input("enter no:-"))
new_str=""
while num>0:
    n=num%10
    new_str=str(n*n)+new_str
    num=num//10
print(new_str)



# take user input and if i put 5 i want output 25 in this form 5 = 25
num=int(input("enter no:-"))
i=1
while i<num:
    i=i+1
    n=num%10
    # num=num//10
    # print(num,"=",num*num)
print(n,"=",n*n)