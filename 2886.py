a , b = input().split()
a = int(a)
b = int(b)
h = 12 - a
m = 60 - b
s = 0
if (h < 0 or h >= 12) and (m < 0 or m >= 60) :
    h = 0
    m = 0
    print(f"{s}{h} : {s}{m}")
elif h < 0 or h >= 12 :
    h = 0 
    if m < 10 :
        print(f"{s}{h} : {s}{m}")
    else :
        print(f"{s}{h} : {m}")
elif m < 0 or m >= 60 :
    m = 0 
    if h < 10 :
        print(f"{s}{h} : {s}{m}")
    else :
        print(f"{h} : {s}{m}")
elif 0 <= h < 12 and 0 <= m < 60 :
    if h < 10 and m < 10 :
        print (f"{s}{h} : {s}{m}")
    elif h < 10 :
        print (f"{s}{h} : {m}")
    elif m < 10 :
        print (f"{h} : {s}{m}")
    else :
        print(f"{h} : {m}")