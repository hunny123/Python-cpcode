n = int(input())
s = list(input())
i=0
count=0
while i<len(s)-1:
    if(s[i]==s[i+1]):
        count=count+1
        
        
    i=i+1
    
print(count)    
