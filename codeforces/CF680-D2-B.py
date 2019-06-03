n = list(map(int,input().split(" ")))

li = list(map(int,input().split(" ")))
count=0
if li[n[1]-1]==1:
    count=count+1
i=1


while  n[1]-1+i<n[0]:
    if(n[1]-1-i>=0 and n[1]-1+i<n[0]):
        
        if(li[n[1]-1-i]==1 and li[n[1]-1+i]==1):
            
            count = count+2
    else:
        break
    i=i+1
   

if(n[1]-1-i>=0):
    
    while n[1]-1-i>=0:
        if(li[n[1]-1-i]==1):
       
            count =count+1
        i=i+1
else:    
    while n[1]-1+i<n[0]:
        
   
        if(li[n[1]-1+i]==1):
            
            count = count+1            
        i=i+1
 
print(count)        
