def cube(n):
    for i in range(1,n+1):
        if n == i**3:
            return(True)
    return(False)

def sum3cubes(n):
    for i in range(1,n-1):
        for j in range (1,n-i):
            k = n - (i+j)
            if cube(i) and cube(j) and cube(k):
                return(True)
    return(False)
