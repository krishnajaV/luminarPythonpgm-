low=int(input("enter thelowerlimit"))
upp=int(input("enter the upperlimit"))
evesum=0
oddsum=0
for i in range(low,upp,1):
  if(i%2==0):
     evesum=evesum+i

  else:
    oddsum=oddsum+i
print("odd sum is",oddsum)
print("even sum is ",evesum)

