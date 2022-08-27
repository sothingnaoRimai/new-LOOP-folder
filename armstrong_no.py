#  The Armstrong number in python is the number in which the sum of each digit
# #  powered to the total number of digits is the same as the given number. i.e.
# #  for a given number say 153, 1^3 + 5^3 + 3^3 is equal to 153. Take another 
# # example, say, 1634 = 1^4 +6^4 +3^4 + 4^4 is an Armstrong number.
# #  0, 1, 153, 370, 371 and 407 1000 to 9999  1634, 8208 and 9474
num=int(input("enter the no"))
length=len(str(num))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**length
    temp=temp//10
if sum==num:
    print(num,"is armstrong")
else:
    print(num,"is not an armstrong")

