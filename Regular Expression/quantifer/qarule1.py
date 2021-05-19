import re
x="a+" #a including  group
matcher=re.finditer(x,"abt c@5aakaaaaaz")
for match in matcher:
    print(match.start())
    print(match.group())