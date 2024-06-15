#Write a python program that removes all punctuation from a given string.
s=input("Enter a string :")
print("The original string is : ",s)
punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ele in s:
    if ele in punc:
        s = s.replace(ele, "")
print("The string after punctuation filter : ",s)
