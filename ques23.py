#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
choice=input("Enter type of temperature you are going to enter f(fahrenheit) or c(celsius) :")
if choice=='c':
    celsius=float(input("Enter temperature :"))
    fahrenheit = (celsius *(9/5)) + 32
    print("Temperature in fahrenheit :",fahrenheit)
elif choice=='f':
    fahrenheit=float(input("Enter temperature :"))
    celsius=(fahrenheit-32)*(5/9)
    print("Temperature in fahrenheit :",celsius)
else:
    print("Enter correct typr of temperature")
