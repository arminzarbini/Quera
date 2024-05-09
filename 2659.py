n = int(input())
word = input()
studentword = input()
wrong = 0
for i in range (n) :
    if word[i] == studentword[i] :
        continue
    else :
        wrong += 1
print(wrong)
