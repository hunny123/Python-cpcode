n = int(input())
li=list()
l2 = list()
i=0
while i<n:
    li.append(i)
    l2.append('0')
    i=i+1
i=0
l = list(input())

while i<n:
    mid = len(li)//2
    if(len(li)%2==0):
        mid = mid-1
    
    
    l2[li.pop(mid)]=l[i]
    
    mid =0
    i=i+1
print("".join(l2))    
