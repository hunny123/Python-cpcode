s = input()
u=0
l=0
for x in s:
    if x.isupper():
        u=u+1
    else:
        l = l+1
if(u>l):
    print(s.upper())
else:
    print(s.lower())
