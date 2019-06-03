n = int(input())
li = input()
li = list(li)
t = 0
r=0
i=0
while i<n:

    if(li[i]=='A'):
        t=t+1
    else:
        r=r+1
    i=i+1    
if(t>r):
    print('Anton')
elif(t<r):
    print('Danik')
else:
    print('Friendship')
    
    
    
