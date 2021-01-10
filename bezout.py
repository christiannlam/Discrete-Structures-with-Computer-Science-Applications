def modExp(b, n, m):
    x = 1
    p = b % m
    i = n
    while( i > 0 ):
        if ( i % 2 == 1 ):
            x = ( x * p ) % m
        p = ( p * p ) % m
        i = i // 2
        
    return x

def bezoutCoeffs(a,b):
    s = 1
    t = 0
    sBar = 0
    tBar = 1
    while( b != 0):
        # finds the quotient bewtween a & b
        quotient = a // b
        # temp variables to hold values of a s t
        aTemp = a
        sTemp = s
        tTemp = t
        a = b
        s = sBar
        t = tBar
        b = aTemp - ( quotient * b )
        sBar = sTemp - ( quotient * sBar)
        tBar = tTemp - ( quotient * tBar)
    return (s,t)

def gcd(a,b):
    d = 0
    # if b equals 0 then gcd is a
    if( b == 0):
        d = a
    else:
        # Takes the largest of a and b and gets gcd until remainder does not equal 0
        d = gcd(b, a % b)
    return d

print("Testing modExp(23, 1002, 41) = ", modExp(23, 1002, 41))
print("Testing bezoutCoeffs(26, 7) = ", bezoutCoeffs(26,7))
print("Testing gcd(101, 4620) = ", gcd(101, 4620))
print("Testing gcd(2349, 36) = ", gcd(2349, 36)) 

