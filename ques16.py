#Write a program in python that counts the frequency of each character in a string
s=input("Enter a string :")
for i in s:
    frequency = s.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
