
#  if a no. is divisible by the sum of its digit eg 156
n=int(input("enter no:"))
num1=n
s=0
rem=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
if num1%s==0:
    print(num1,"is harshad number")
else:
    print("It is not harshad number")
