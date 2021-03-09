# Find out greatest common divisor(gcd) of given two numbers.
def gcd(m,n):
    if m < n:
        (m,n)=(n,m)
    while (m%n)!= 0:
        (m,n)=(n,m%n)
        print(m,n)
    return(n)
