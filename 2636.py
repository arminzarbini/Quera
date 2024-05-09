chess = {"king" : 1, "queen" : 1, "rook" : 2, "bishop" : 2, "knight" : 2, "pawn" : 8} 
shatranj = []
n = input().split()
for i in n :
    shatranj.append(int(i))
    
c = 0
pouyan = []
for item in chess.values() :
    pouyan.append(item - shatranj[c])
    c = c + 1

for i in pouyan :
    print (i,end=" ")
