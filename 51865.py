X = int(input())
N = int(input())
if N == 0 :
    X = 20
    print (X)
elif N == 7 :
    print (X)
else :
    X = X - N
    if X < 0 :
        X = 0
        print (X)
    elif X >= 0 :
        print (X)
        