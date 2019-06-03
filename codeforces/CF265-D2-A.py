li = list(input())
li2 = list(input())
count =0
i=0
while i<len(li2):
    if(li[count]==li2[i]):
        count=count+1
    i=i+1
print(count+1)    
