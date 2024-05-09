n = int(input())
t = 0
c = 1
while t <= n :
    t = 2 ** c
    c = c + 1
    if t > n :
        break
print(t)
