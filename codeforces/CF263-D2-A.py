i=0
j=0
ic =3
jc =3
j1=0
i1=0
a =list()
while i<5:
    a.append(list(map(int,input().split(" "))))
    
    i=i+1
i=0

for i in range(0,len(a)):
    for j in range(0,len(a[i])):
       
        if(a[i][j]==1):
            
            j1=j+1
            i1=i+1
            
            print(abs(ic-i1)+abs(jc-j1))
            
       
  


