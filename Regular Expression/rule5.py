import re
x="[a-zA-Z]" #both a to z and A-Z are checked
matcher=re.finditer(x,"abt c@5kLz")
for match in matcher:
    print(match.start())
    print(match.group())