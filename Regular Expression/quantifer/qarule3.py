import re
x="a?" #count a as each including zero number of a
matcher=re.finditer(x,"abaaaa")
for match in matcher:
    print(match.start())
    print(match.group())