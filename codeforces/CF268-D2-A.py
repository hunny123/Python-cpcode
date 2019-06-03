n = int(input())
li=list()
i=0
while i<n:
    li.append(list(map(int,input().split(" "))))
    i=i+1
count=0
i=0
while i<n:
    j=0
    
    while j<n :
        if(li[i][0]==li[j][1] and i!=j):
            
            count=count+1
        j=j+1
    i=i+1
print(count)    
              
    
