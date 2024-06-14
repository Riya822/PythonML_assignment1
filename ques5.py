#Write a program that takes a string input from the user and writes it to a text file
s=input("Enter a string :")
with open('abc.txt', 'w') as abc: 
    abc.write(s)
