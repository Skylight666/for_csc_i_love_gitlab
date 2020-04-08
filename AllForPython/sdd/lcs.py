import re

pattern = r"\>Rosalind\_(\d)"
text = []

with open('rosalind_lcsm.txt', 'r') as f:
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

N = 100
L = [[0 for i in range(N)]
        for j in range(N)]

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
    return lcs_set

#print(mtx)
buf = []
ans = list(lcs(mtx[0], mtx[1]))
for i in range(2, len(mtx)):
    for subst in ans:
        buf += list(lcs(subst, mtx[i]))
    ans = buf
print(max(ans))
