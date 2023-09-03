n=input("Enter the first word:  ")
nn=input("enter the second word:   ")
ans=input("enter the third word:   ")
l=[]
for i in n:
    l.append(i)

for i in nn:
    l.append(i)
    
l=list(set(l))
k={}
s="1234567890"
q=0
for i in l:
    k[i]=s[q]
    q+=1
for i in n:
    print(i," ",k[i])
