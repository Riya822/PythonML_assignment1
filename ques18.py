#Write a python program that checks if two strings are anagrams of each other
s1=input("Enter first string :")
s2=input("Enter second string :")
if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams") 
else:
    print("The strings aren't anagrams")
