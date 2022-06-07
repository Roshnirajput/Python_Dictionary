d={'5001':['mothe','scionce'],'5002':['moth','english']}
for i in d:
    str =""
    for j in i:
        if j!="":
            str +=j
    print(str,d[i])
