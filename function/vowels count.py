a=input("enter the string")
count=0
b="aeiou"
for i in a:
    if i in b:
        count=count+1
print(count)