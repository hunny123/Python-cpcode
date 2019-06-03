n =input()
li = list(map(int,n.split(" ")))
i=1
while i<=max(li[0],li[1]):
    if(li[0]*3**i>li[1]*2**i):
        print(i)
        break
    i=i+1 
