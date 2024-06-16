#Write a program that copies the contents of one text file to another
with open('first.txt','r') as file1,open('second.txt','a') as file2: 
    for line in file1: 
        file2.write(line)
