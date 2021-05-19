import re
x="[abc]"
matcher=re.finditer(x,"abaabbab")
for match in matcher:
    print("match availanble",match.start())
    print("group",match.group())
    count=+1
print("count=",count)
