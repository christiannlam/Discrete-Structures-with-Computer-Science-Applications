def binaryAdd(a, b):
    """returns the sum of two binary numbers a and b
    INPUT: a,b - string representation of the binary numbers
    OUPUT: string representation of their sum
    """
    a = a.replace(" ", "") #removing all whitespaces in string a
    b = b.replace(" ", "") #FIXME: REMOVE ALL WHITESPACES IN STRING b
    
    m = len(a) #number of digits in string a
    n = len(b) #number of digits in string b
    
    if m < n: #if string a is shorter than string b
        num_missing_zeros = n - m
        a = num_missing_zeros*"0" + a #appending 0's to the beginning of string a, to make it the same length as b
    
    if n < m:
        num_missing_zeros = m - n
        b = num_missing_zeros*"0" + b
    
    result = "";
    carry = 0;
    i = 0;
    for i in range(m-1,-1,-1):
        if carry == 0:
            if a[i] == "0" and b[i] == "0":
                result = "0" + result
            elif a[i] == "0" and b[i] == "1":
                result = "1" + result
                
            elif a[i] == "1" and b[i] == "0":
                result = "1" + result
                
            elif a[i] == "1" and b[i] == "1":
                carry = 1
                result = "0" + result
        else:
            if a[i] == "0" and b[i] == "0":
                carry = 0
                result = "1" + result
            elif a[i] == "0" and b[i] == "1":
                result = "0" + result
            elif a[i] == "1" and b[i] == "0":
                result = "0" + result
            elif a[i] == "1" and b[i] == "1":
                result = "1" + result
        
    if carry == 1:
        result = "1"+ result
            
    return result;
            
    print("a =", a)
    print("b =", b)
    print("result =", result)

