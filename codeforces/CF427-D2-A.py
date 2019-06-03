n = int(input())
li = list(map(int,input().split(" ")))
i=0
c =0
t =list()
while i<n:
    if(li[i]>0):
        c=c+li[i]
        
    else:
        if(c==0):
            t.append(li[i])
        else:
            c=c+li[i]
  
    i=i+1 
print(len(t))    
