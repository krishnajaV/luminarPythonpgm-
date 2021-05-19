import re
x="[0-9]" #0-9
matcher=re.finditer(x,"abt c@5k2z")
for match in matcher:
    print(match.start())
    print(match.group())