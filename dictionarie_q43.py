d=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
k={}
s=" "
s1=""
for i in d:
    if i[0] not in k.keys():
        if i[0]=="yellow":
            s=s+i[0]
        elif i[0]=="blue":
            s1=s1+i[0]
            print(i[1],s,s1)
#        k.update({i[0]:[i[i]]})
#     elif i[0] in k.keys():
#           k[i[0]].append(i[i])
# print(k)