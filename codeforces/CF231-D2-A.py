n = int(input())
li=list()
i=0
count=0
while i<n:
    li = list(map(int,input().split(" ")))
    if(sum(li)>=2):
        count = count+1
    i=i+1

print(count)
    
