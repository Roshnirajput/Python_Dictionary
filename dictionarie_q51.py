d={'v':[1,4,6,10],'vi':[1,4,12],'vii':[1,3,8]}
for i in d.keys():
    d[i]=[i for i in d[i] if i%2==0]
print(d)