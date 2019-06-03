c =list(map(int,input().split(" ")))
li=list()
i=0
while i<c[1]:
    li.append(list(map(int,input().split(" "))))
    i=i+1
li=sorted(li,key=lambda x:x[1])[::-1]

i=0
prod=0
while i<c[1] and c[0]>=0:
    if(c[0]>=li[i][0]):
        c[0] = c[0]-li[i][0]
        
    else:
        li[i][0]=li[i][0]-(li[i][0]-c[0])
        c[0] = c[0]-li[i][0]
    prod = prod+li[i][0]*li[i][1]
    i=i+1    
print(prod)    
 
