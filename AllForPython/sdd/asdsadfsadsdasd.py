l = []
for x in range(-400, 400):
    for y in range(-400, 400):
        if (x+y<5) and (x>3):
            l.append((x-y, x, y))
for el in l:
    if el[0] == 4:
        print(el[1], el[2])
