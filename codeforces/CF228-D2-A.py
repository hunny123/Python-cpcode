li = list(map(int,input().split(" ")))
i=0
count=0
while i<len(li):
    if(li.count(li[i])>1):
        
        count=count+1
        li[i]=0
    i=i+1
print(count)    
