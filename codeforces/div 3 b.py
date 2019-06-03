n = int(input())
i=0
str1 = input()
li = list(map(str,input().strip().split(" ")))
li.insert(0,0)
ti =list()
ti.append(int(str1))
i=0
while i<n:
    str2 = str1.replace(str1[i],li[int(str1[i])],1)
    
    
    if(str2>str1):
        str1=str2
    i=i+1
    
print(str(max(ti)))
