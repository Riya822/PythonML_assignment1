#Write a python program that calculates the factorial of a given number
num=int(input("enter a number :"))
fact=1
while num>1 :
    fact*=num
    num-=1
print("Factorial is",fact)
