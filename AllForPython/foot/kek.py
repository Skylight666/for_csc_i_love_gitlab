ar = []

with open('dataset_313198_2_4.txt', 'r') as f:
    for l in f:
        ar += [int(j) for j in l.split()]

sr = set(ar)
dr = {k:0 for k in ar}

for k in ar:
    dr[k] += 1

print(max(dr.values()))
