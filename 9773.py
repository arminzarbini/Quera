n = int(input())
c = n // 2
star = "*"
space = " "
for i in range (1 , n + 1 , 2) :
    if i == n :
        print (f"{i*star}{i*star}")
    else :        
        print (f"{c*space}{i*star}{c*space}{c*space}{i*star}{c*space}")
        c = c - 1

for j in range (n -2 , 0 , -2) :
    c = c + 1
    print (f"{c*space}{j*star}{c*space}{c*space}{j*star}{c*space}")