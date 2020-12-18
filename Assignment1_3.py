tup=(9,9,9,9,9)
flag=0
for i in tup:
    if tup[0]==i:
        continue
    else:
        print("False")
        flag=1
        break
if flag==0:
    print("True")
    
