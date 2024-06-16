#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
str=input("Enter a string :")
pre=input("Enter prefix :")
suf=input("Enter suffix :")
if str.startswith(pre) and str.endswith(suf):
    print("It starts with given prefix and ends with given suffix")
else :
    print("It does not starts with given prefix and ends with given suffix")
