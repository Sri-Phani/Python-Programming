n=int(input())
a=0
b=1
#for i in range(0,n):
while (True):
    sum=a+b
    if n<=sum:
        a=b-a
        b=sum-b
        print(a+b)
        break
    a=b
    b=sum
