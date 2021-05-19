import re
x="[A-Z]" #a to z
matcher=re.finditer(x,"abt c@5Lkz")
for match in matcher:
    print(match.start())
    print(match.group())