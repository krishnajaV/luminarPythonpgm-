s1={1,2,5,7,4,8,9,66,8,5,42,555}
odd=set()
even1=set()
for i in s1:
    if(i%2==0):
        even1.add(i)
    else:
        odd.add(i)

print("even number ",even1)
print("odd number",odd)
