#ok
tab = 5
res = 0
for i in range (1, 11, 1):
    res = tab * i
    print(tab, 'x', i, '=', res)

#possibilidade 1: print(tab, " x ", i, " = ", res)
#possibilidade 2: print(f"{tab} x {i} = {res}")