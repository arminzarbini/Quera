n = input().split()
n2 = []
for i in n :
    i = int(i)
    n2.append(i)

if n2[0] == 0 or n2[1] == 0 or n2[2] == 0 :
    print("No")
elif n2[0] + n2[1] + n2[2] == 180 :
    print("Yes")
else :
    print("No")