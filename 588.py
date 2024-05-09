n = int(input())
a = input().split()
while len(a) > n :
    a.pop(n)
    if len(a) == n :
        break
maxi = 0
for i in a :
    i = int(i)
    if i > maxi :
        maxi = i
print(maxi)
    
    


