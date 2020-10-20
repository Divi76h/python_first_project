ti = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 2, 21, 3, 3, 13, 1, 3, 23, 1, 3231231)
e = ()
o = ()

for i in range(len(ti)):
    if ti[i] % 2 == 0:
        e = e + (ti[i],)
    else:
        o = o + (ti[i],)

print(e)
print(o)