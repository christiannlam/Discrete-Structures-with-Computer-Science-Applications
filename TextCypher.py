def modinv(a,m):
        i = 1
    while(i <= a and i <= m):
        if(a % i == 0 and m % i == 0):
            gcd = i
        i = i + 1
        
    if(gcd == 1):
        mod = m
        s = 1
        t = 0
        sBar = 0
        tBar = 1
        while( m != 0):
            quotient = a // m
            aTemp = a
            sTemp = s
            tTemp = t
            a = m
            s = sBar
            t = tBar
            m = aTemp - ( quotient * m )
            sBar = sTemp - ( quotient * sBar)
            tBar = tTemp - ( quotient * tBar)
        if(s < 0):
            return s + mod
        else:
            return s
    else:
        raise ValueError('The given values are not relatively prime')
        
def affineEncrypt(text, a, b):
   cipherIndex = 0
    words = ""
    i = 1
    letters = letters2digits(text)
    while(i <= a and i <= 26):
        if(a % i == 0 and 26 % i == 0):
            gcd = i
        i = i + 1
    if( gcd == 1 ):
       for i in range (0,len(letters),2):
            cipher = str(( a * int(letters[i:cipherIndex+ 2]) + b ) % 26)
            if(len(str(cipher)) == 1):
                cipher = "0" + str(cipher)
            words = words + digits2letters(cipher)
            cipherIndex += 2 
       return words 
    else:
        raise ValueError('The given key is invalid. The gcd(a,26) must be 1.')
        
def affineDecrypt(ciphertext, a, b):
        words = ""
    cipherIndex = 0
    i = 1
    while(i <= a and i <= 26):
        if(a % i == 0 and 26 % i == 0):
            gcd = i
        i = i + 1
    if( gcd == 1):
        invA = modinv(a,26)
        letters = letters2digits(ciphertext)
        for i in range (0,len(letters),2):
            cipher = (invA * (int(letters[i:cipherIndex + 2]) - b ) ) % 26
            cipherIndex += 2
            if(len(str(cipher)) == 1):
                cipher = "0" + str(cipher)
            words = words + digits2letters(str(cipher))
        return words
    else:
        raise ValueError('The given key is invalid. The gcd(a,26) must be 1.')
        
def encryptRSA(m, p, q, e):
    code = ""
    n = p * q
    l = 0
    i = 1
    a = (p-1)*(q-1)
    while(i <= a and i <= e):
        if(a % i == 0 and e % i == 0):
            gcd = i
        i = i + 1
    if(gcd == 1):
        letters = letters2digits(m)
        l = blocksize(n)
        if( len(letters) % l != 0):
            letters = letters + "23"
        for i in range(0,len(letters),l):
            cipher = str((int(letters[i:i+l])**e) % n)
            if(len(cipher) < l):
                code = code + "0" + str(cipher)
            else:
                code = code + str(cipher)
        return code
    else:
        raise ValueError('The given key is invalid. The gcd((p-1)*(q-1),e) must be 1.')
        
def decryptRSA(c, p, q, e):
    code = ""
    words = ""
    cipherIndex = 0
    n = p * q
    a = (p-1)*(q-1)
    i = 1
    c = c.replace(" ","")
    print(c)
    while(i <= a and i <= e):
        if(a % i == 0 and e % i == 0):
            gcd = i
        i = i + 1
    if( gcd == 1):
        invE = modinv(e,a)
        print(invE)
        l = blocksize(n)
        print(len(c))
        print(l)
        for i in range(0,len(c),l):
            cipher = str((int(c[i:i+l])**invE) % n)
            if(len(cipher) < l):
                code = code + "0" + str(cipher)
                print(code)
            else:
                code = code + str(cipher)
                print(code)
        for i in range (0,len(code),2):
            cipher = digits2letters(code[i:cipherIndex + 2])
            words = words + cipher
            cipherIndex += 2
        return words
    

encrypted1 = encryptRSA("STOP", 43, 59, 13)
encrypted2 = encryptRSA("HELP", 43, 59, 13)
encrypted3 = encryptRSA("STOPS", 43, 59, 13)
print("Encrypted Message:", encrypted1)
print("Expected: 2081 2182")
print("Encrypted Message:", encrypted2)
print("Expected: 0981 0461")
print("Encrypted Message:", encrypted3)
print("Expected: 2081 2182 1346")

decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")
