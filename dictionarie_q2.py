b='w3resource'
i=0
d={}
while i<len(b):
      c=0
      j=0
      while j<len(b):
         if b[i]==b[j]:
            c+=1
         j=j+1
      if b[i] not in d:
         d[b[i]]=c
      i=i+1     
print(d)  