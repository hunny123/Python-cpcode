
li =list(input())
n =len(li)
k='a'
i=0
t=0
count =0
while i<n:
    t=abs(ord(k)-ord(li[i]))
    if t<13:
        
        count=count+t
        
    else:
        count=count+abs(t-26)
        
    k=li[i]    
    i=i+1
print(count)    
                        
                        
        
