mat=[]
for i in range(4):
    n=input()
    rowv=[int(i) for i in n.split()]
    mat.append(rowv)
mat=mat[::-1]
print(mat)
k=[]
l=input("Enter the level mi or ma")
k=[i for i in l.split()]
alpha=0
beta =1000
it=0
v=max(mat)
print(k)
for i in range(0,12,3):
    if(k[it]=="max"):
        f=[]
        
        
        
        it+=1
    if(k[it]=="min"):
        f=[]
        
        
        it+=1
    it=0


if(l[len(l)-1]=="min"):
    print(v)
elif(l[len(l)-1]=="max"):


    print(max(mat))
for i in v:
    
    
    


