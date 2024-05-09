def reverse(n) :
    reversenum = 0
    while n > 0 :
        r = n % 10
        reversenum = (reversenum * 10) + r
        n = n // 10
    return reversenum

n = int(input())
if n == reverse(n) :
    print("YES")
else :
    print("NO")
