#def print_employee(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"=",v)
# print_employee(id=100,nat_place="THRISSUR",job="kakkanad",salary=34000)



employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}
}
def print_employee(**kwargs):#Create a fn print_employee -> calling  fn print_employee(id=1000) it will name of that ewmployree
    id=kwargs["id"]
    if id in employees:
        print(employees[id]["name"])
    else:
        print("invalid")
print_employee(id=1001)
