#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
n1=float(input("enter a number :"))
n2=float(input("enter another number :"))
op=input("Enter operation :")
if op=='+':
    print("sum is :",n1+n2)
elif op=='-':
    print("difference is :",n1-n2)
elif op=='*':
    print("multiplicatio is :",n1*n2)
elif op=='/':
    print("divident is :",n1/n2)
