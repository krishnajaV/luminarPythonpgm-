import re
x="\w" #all words except special charater
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())