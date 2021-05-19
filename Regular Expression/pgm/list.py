# import re
# f=open("luminar","r")
# x='[L][U][M]\d{2}[p][y]\d{3}'
# for i in f:
#     m=re.findall( x , i )
#     if i is not None:
#         print(m)




import re
f2=open("lumi","w")
x='([L][U][M]\d{2}[P][Y]\d{3}$)'
f=open("luminar","r")

for i in f:
    data=i.rstrip("\n")
    m=re.fullmatch( x , data )
    if m is not None:
        f2.write(data)
        f2.write("\n")
#WTWY
#