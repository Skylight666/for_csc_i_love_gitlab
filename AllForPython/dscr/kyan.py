import numpy as np


def to_xyzw(s, p):
    ans = ''
    d1 = {0 : 'x', 1 : 'y', 2 : 'z', 3 : 'w'}
    d2 = {0 : 'x1', 1 : 'x2', 2 : 'x3', 3 : 'x4'}
    if p:
        d = d1
    else:
        d = d2
    for n, i in enumerate(s):
        if i == '-':
            continue
        if int(i):
            ans += d[n]
        else:
            ans += '!' + d[n]
    return ans

def diff(r, c):
    for a in range(4):
        if r[a] != '-':
            if r[a] != c[a]:
                return '    '
    return ' +  '

#print(to_xyzw('-100'))
#vec = input()
vec = '1110011000010101'
#vec = '1000100000111111'
#vec = '1110001000000011'
l = []
for n, i in enumerate(vec):
    if int(i):
        l.append(format(n, '04b'))
print(l)
print('_'*80)
def am_nam(l):
    #cnt_sym = len(l[0])
    sh_l = set()
    adding = set(l)
    for a1 in l:
        for a2 in l:
            cntr = 0
            buf = ''
            for i in range(4):
                if a1[i] == a2[i]:
                    buf += a1[i]
                    cntr += 1
                else:
                    buf += '-'
            if cntr == 3:
                sh_l.add(buf)
                adding.discard(a1)
                adding.discard(a2)
    if sh_l.union(adding) == set(l):
        return sh_l.union(adding)
    else:
        return am_nam(sh_l.union(adding))

ans = am_nam(l)

print([to_xyzw(i, 0) for i in ans])
print('_'*80)

print([to_xyzw(i, 1) for i in ans])
print('_'*80)

print(ans)
print('_'*80)

a = [[0 for i in range(len(l) + 1)] for k in range(len(ans)+1)]
a[0] = ['____'] + l

for k in range(len(ans)):
    a[k+1][0] = list(ans)[k]

for i in range(1, len(l)+1):
    for k in range(1, len(ans)+1):
        a[k][i] = diff(a[k][0], a[0][i])

with open('table.txt', 'w') as f:
    for s in a:
        f.write(str(s))
        f.write('\n')
