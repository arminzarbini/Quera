def perfect(a) :
    p = 0
    for i in range (1, n) :
        if n % i == 0 :
            p = p + i
    if p == n :
        return "YES"
    else :
        return("NO")
    
n = int(input())
print(perfect(n))


