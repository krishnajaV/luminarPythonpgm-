import re
r=open("phone","r")
f=open("phe","w")
x = '[+][9][1]\d{10}$'
for i in r:
    number=i.rstrip("\n")
    match=re.fullmatch( x, number)
    if match is not None:
        f.write(number)
        f.write("\n")



