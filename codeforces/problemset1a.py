n = list(map(int,input().split(" ")))
l= n[0]
h=n[1]
a = n[2]
t=0
k=0
if(l%a==0):
    t=l//a
else:
    t=l//a+1
if(h%a==0):
    k=h//a
else:
    k=h//a+1
print(k*t)    
