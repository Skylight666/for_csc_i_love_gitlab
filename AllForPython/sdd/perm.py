from itertools import permutations

n = 7
perm = permutations(range(1,n+1))

k = list(perm)
print(len(k))
for i in k:
    for j in i:
        print(j, end=' ')
    print()
