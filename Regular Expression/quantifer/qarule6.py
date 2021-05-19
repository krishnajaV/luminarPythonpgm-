import re
x='^a'# check starting letter a
r="aaaa aabc cga"
matcher=re.finditer( x , r)
for match in matcher:
    print(match.start())
    print(match.group())