l=[[1,'lean castro','v'],[2,'lula powwell','v'],[3,'brian howell','vi'],[4,'lynne faster','vi'],[5,'zachary sion','vii']]
dict={}
for i in l:
    b={i[0]:i[i:]}
    dict.update(b)
print(dict)
