def binary(n):
    r=0
    i=0
    while n:
        rem=n%10
        r+=((2**rem)*i)
        n//=10
        i+=1
    return r
n=int(input())
print(binary(n))
