arr=[2,3,4,5,6]
#map(function,iterable)
#iterable==map
squrelist=list(map(lambda num:num**2,arr))
print(squrelist)
lst=["ajay","arun","aby","binu"]
uppername=list(map(lambda name:name.upper(),lst))
print(uppername)
lst=["ajay","arun","aby","binu"]
op=list(filter(lambda name:name[0]=='a',lst))
print(op)








