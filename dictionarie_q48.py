d={1:'red',2:'green',3:'black',4:'white',5:'black'}
for i in d:
    c=0
    for j in d[i]:
        c=c+1
print(d[i],'=',c)