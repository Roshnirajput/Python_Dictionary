d={'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
for j in d:
    print(j, end='')
print('')
i=0
while i<len(d):
    for k in d:
        print(d[k][i],end='')
    print()
    i=i+1