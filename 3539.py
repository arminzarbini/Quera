def takraghami(i) :
    t = 0
    while i > 0 :
        b = i % 10 
        t = t + b
        i = i // 10
    return(t)

n = int(input())
while n >= 10 :
    n = takraghami(n)
print(n)










   


    
    
    

