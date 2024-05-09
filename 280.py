n = []
for i in range (3) :
    n.append(int(input()))

maxi = max (n)
n.remove(maxi)

if (n[0] ** 2) + (n[1] ** 2) == maxi ** 2 :
    print("YES")
else :
    print("NO")


    
    


    
