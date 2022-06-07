d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d={}
for i in (d1,d2,d3):
    d.update(i)
print(d) 
 
# d.update(d2)
# d.update(d3)
# d.update(d1)
# print(d)

