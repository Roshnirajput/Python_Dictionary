d={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
max=0
smx=0
temx=0
for i in d:
    if  d [i]>max:
      max=d[i]
for j in d:
    if d [j]>smx and d[j]<max:
        smx=d[j]
for k in d:
    if d [k]>temx and d [k]<smx:
        tmax=d[k]
print(max)
print(smx)
print(tmax)
