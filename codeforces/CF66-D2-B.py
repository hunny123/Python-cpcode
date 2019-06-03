def forward(i,li):
    count =1
    k=i
    n = len(li)
    while k<n-1 and k>=0:
        
        if(li[k]>=li[k+1]):
            count=count+1
        else:
            break
        k=k+1
    return count     
def backward(i,li):
    count =1
    k=i
    n = len(li)
    while k<n and k>0:
        
        if(li[k]>=li[k-1]):
            count=count+1
        else:
            break
        k=k-1
    return count     
n = int(input())
li = list(map(int,input().split(" ")))
count = list()
s=0
i=0
while i<n:
    if(i==0):
        s=forward(i,li)
    elif(i==n-1):
        s = backward(i,li)
    else:
        s = forward(i,li)+backward(i,li)-1
    count.append(s)

    i=i+1
print(max(count))    
