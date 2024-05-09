import random
haftsin = ["sib","samano","serkeh","sekeh","somagh","sabzeh","senjed","sepand","sir"]
m = int(input())
if m > 7 :
    m = 7
pasha = []
sinchoice = 0
while sinchoice < m :
    sin = random.choice(haftsin)
    if sin in pasha :
        continue
    else :
        pasha.append(sin)
        sinchoice += 1
    
for item in pasha :
    print(item)
