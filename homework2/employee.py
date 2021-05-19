employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
 {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
   {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}
]
#print employee name only in map
# ename=list(map(lambda name:name["name"],employees))
# print(ename)
# empname=list(map(lambda emp:emp["name"],employees))
# print(empname)
# # print all employee name into uppercase map(0
# uname=list(map(lambda name:name["name"].upper(),employees))
# print(uname)
# #print employee details whose name starinting with 'a' ==a filter()
# aname=list(filter(lambda name:name["name"][0]=='a',employees))
# print(aname)
# #print employee details whose salary>23000
# sal=list(filter(lambda salary:salary["salary"]>23000,employees))
# print(sal)
# # print employee details whose designation==developer
# designation=list(filter(lambda designation:designation["designation"]=='developer',employees))
# print(designation)
#print develpper above 25000
desi=list(filter(lambda emp:emp["designation"]=="developer" and emp["salary"]>24000,employees))
print(desi)
names=list(filter(lambda  name:name["designation"]=="developer" and name["salary"]>23000, employees))
print(names
      )