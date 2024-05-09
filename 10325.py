r , c = input().split()
r = int(r)
c = int(c)
r2 = (10 - r) + 1
if 1 <= c <= 10 :
    print(f"right {r2} {c}")
else :
    c2 = (20 - c) + 1 
    print (f"left {r2} {c2}")