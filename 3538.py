hafte = {"shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"}
pouyanfriends = []
p1 = int(input())
pouyanfriends.extend(input().split(" "))
p2 = int(input())
pouyanfriends.extend(input().split(" "))
p3 = int(input())
pouyanfriends.extend(input().split(" "))

pouyan = set(pouyanfriends)
mehdi = hafte.difference(pouyan)
print(len(mehdi))

