#GCD
'''def gcd(a,b):#9,12
    if a>b:
        a,b=b,a
    c=a
    while True:
        if a%c==0 and b%c==0:
            return c
        c-=1
a,b=map(int,input().split())
print(gcd(a,b))
'''
#eucledian algorithm
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a,b=map(int,input().split())
print(gcd(a,b))
#9,12
#9,3--swap

