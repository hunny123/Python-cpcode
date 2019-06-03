def spell(n):
    return sum(list(map(int,n)))



n = (input())
count=0
while len((n))!=1:
    count =count+1
    n=str(spell(n))
print(count)
