#Write a python program that calculates the sum of the digits of a given number
num=int(input("Enter a number :"))
sum=0
while num>0:
    d=num%10
    sum+=d
    num//=10
print("sum of the digit :",sum)
