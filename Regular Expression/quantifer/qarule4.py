import re
x="a{2}" #2 no of position
r="aaaa aabc cga"
matcher=re.finditer( x , r)
for match in matcher:
    print(match.start())
    print(match.group())