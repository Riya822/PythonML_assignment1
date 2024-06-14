#Write a program that reads the content of a text file and prints it to the console
with open("abc.txt",'r') as abc:
    content = abc.read()
    print("File Content:\n", content)
  
