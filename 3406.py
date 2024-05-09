n = int(input())
m = int(input())
nreverse = int(str(n)[::-1])
mreverse = int(str(m)[::-1])
if nreverse == mreverse :
    print(f"{n} = {m}")
elif nreverse < mreverse :
    print(f"{n} < {m}")
elif mreverse < nreverse :
    print(f"{m} < {n}")




