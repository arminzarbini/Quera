def bloodcheck(d,m,c) :
    blood = True
    for i in "A","B" :
        if i not in d and i not in m and i in c :
            blood = False
            break
    for j in "O" , "-" :
        if j in d and j in m and j not in c :
            blood = False
            break
        
    if blood == True :
        return("valid")
    elif blood == False :
        return("invalid")
        
t = int(input())
bloodresult = []
for i in range (t) :
    d,m,c = input().split()
    bloodresult.append(bloodcheck(d,m,c))

for item in bloodresult :
    print(item)