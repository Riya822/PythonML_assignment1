#Write a python program that counts the occurrences of a specific element in a list
lst=[5,79,8,5,66,52,3,5]
x=int(input("enter number to be counted :"))
count = 0
for ele in lst:
    if (ele == x):
        count = count + 1
print("count of ",ele,"is :",count)
