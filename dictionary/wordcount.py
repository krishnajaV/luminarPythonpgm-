count={}
data="heelloo hhi helloooo"
words=data.split(" ")
for i in words:
    if i not in count:
        count.update({i:1})
    else:
        val=int(count[i])
        val+=1
        count.update({i:val})
print(count)
