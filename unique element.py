##s=list(map(int,input().split()))
##for i in s:
##    if(s.count(i)==1):
##        print(i)

l=list(map(int,input().split()))
c=0
for i in l:
   c^=i
print(c)
        

