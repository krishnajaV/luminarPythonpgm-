                      # def pattern():
#     for i in range(1,6):
#         for j in range(1,i+1):
#             print("*",end='')
#         print()
# pattern()

def pattern(n):
    for i in range(1,n):
        for j in range(1,i):
            print("*",end='')
        print()
pattern(6)