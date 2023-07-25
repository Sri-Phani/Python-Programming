'''def dec(n):
    while(n>1):
        r=n%2
        n//=2
        print(r,end=' ')
    print(n)

n=int(input())
dec(n)
'''
def dec(n):
    s=''
    while(n>1):
        r=n%2
        n//=2
        s+=str(r)
    s+=str(n)
    return s[: :-1]
n=int(input())
dec(n)
