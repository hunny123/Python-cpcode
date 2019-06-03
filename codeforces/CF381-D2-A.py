n = int(input())
li = list(map(int,input().split(" ")))
count=0
s=0
d=0
i=0
while i<n:
    k = max(li[0],li[len(li)-1])
    del(li[li.index(k)])
    if(i%2==0):
        s=s+k
    else:
        d=d+k
    i=i+1
print(str(s)+" "+str(d))    
