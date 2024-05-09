a,b,l = input().split()
khar = []
for item in a,b,l :
    item = int(item)
    khar.append(item)
n = 0
for i in range (1,khar[2] + 1) :
    if i % 2 != 0 :
        n = n + khar[0]
    elif i % 2 == 0 :
        n = n + khar[1]

print(n)
