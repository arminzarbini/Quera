x = []
y = []
x1, x2, x3, x4, x5 = input().split()
y1, y2, y3, y4, y5 = input().split()
for xm in x1,x2,x3,x4,x5 :
    xm = int(xm)
    x.append(xm)
for ym in y1,y2,y3,y4,y5 :
    ym = int(ym)
    y.append(ym)

escaperoom = False
for i in range (5) :
    x.insert(0 , x[4])
    x.pop(5)
    for j in range (5) :
        y.insert(0, y[4])
        y.pop(5)
        n1 = x[1] + y[1]
        n2 = x[2] + y[2]
        n3 = x[3] + y[3]
        if n1 >= 10 :
            n1 = n1 - 10 
        if n2 >= 10 :
            n2 = n2 - 10
        if n3 >= 10 :
            n3 = n3 - 10
        n1 = n1 * 100
        n2 = n2 * 10
        n = n1 + n2 + n3
        if n % 6 == 0 :
            escaperoom = True
            break
    
if escaperoom == True :
    print("Boro joloo :)")
else :
    print("Gir oftadi :(")