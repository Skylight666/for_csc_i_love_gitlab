import re

pattern = r"\>Rosalind\_(\d)"
text = []

with open('rosalind_cons.txt', 'r') as f:
    for l in f:
        text.append(l)

mtx = []
i = 0
while (i < len(text) and re.match(pattern, text[i])):
    ind = re.match(pattern, text[i]).group(0)
    i += 1
    row = ''
    while ( i < len(text) and text[i][0] != '>'):
        row += text[i].strip()
        i += 1
    mtx.append(row)

ll = len(mtx[0])
d = {'A':0, 'C':1, 'G':2, 'T':3}
inverse_d = ['A', 'C', 'G', 'T']
matind = [[0 for k in range(ll)] for k in range(4)] #ACGT
for line in mtx:
    for pos, letter in enumerate(line):
        matind[d[letter]][pos] += 1

ans = ''
for k in range(ll):
    k_max = max( [matind[j][k] for j in range(4)] )
    for i in range(4):
        if matind[i][k] == k_max:
            ans += inverse_d[i]
            break
print(ans)
for i in range(4):
    print('{}: '.format(inverse_d[i]), end='')
    for k in matind[i]:
        print(k, end=' ')
    print()
