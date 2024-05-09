n = int(input())
for i in range (1,n+1) :
    if i == 1 or i == n :
        print(n * "*")
    else :
        print("*\t*".expandtabs(n-1))