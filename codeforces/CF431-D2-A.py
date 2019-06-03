n = list(map(int,input().split(" ")))
k= list(map(int,input()))
i=0
s=0
for x in k:
    
    s=s+n[x-1]
print(s)    
