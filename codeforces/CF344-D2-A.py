n = int(input())
i=0
li = list()
while i<n:
    li.append(input())
    i=i+1
count =1
i=0
while i<n-1:
    if(li[i]!=li[i+1]):
        count=count+1
    i=i+1
print(count)    
    
