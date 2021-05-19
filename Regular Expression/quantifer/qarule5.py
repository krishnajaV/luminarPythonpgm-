import re
x="a{2,3}" #minimum 2 a and maximum 3a
r="aaaa aabc cga"
matcher=re.finditer( x , r)
for match in matcher:
    print(match.start())
    print(match.group())