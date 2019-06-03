def findwidth(n,h):
    sum1=0
    i=0
    while i<len(n):
        
        if(n[i]>h):
            sum1 = sum1+2
        else:
            sum1 = sum1+1
        i=i+1    
    return sum1
t = input()
t = list(map(int ,t.split(" ")))
li = input()
li = list(map(int,li.split(" ")))
print(findwidth(li,t[1]))
