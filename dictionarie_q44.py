d={'scince':[88,89,62,95],'language':[77,78,84,80]}
l=[]
x,y=d.values()
for i in range(len(x)):
    for j,k in d.items():
        y=({j:k[i]})
        l.append(y)
print(l)
