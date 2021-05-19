import re
x="a*" #count including  zero number of a
matcher=re.finditer(x,"abt c@5aakaaaaaz")
for match in matcher:
    print(match.start())
    print(match.group())