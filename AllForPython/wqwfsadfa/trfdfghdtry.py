arr = []
for i in range(1):
    arr.append([int(k) for k in input().split(' ')])

def foo(l):
    ans = ''
    for i in range(16):
        if i in l:
            ans += '1'
        else:
            ans += '0'
    return ans

with open('sgvredpihjub.txt', 'w') as f:
    for w in arr:
        f.write(foo(w)+'\n')
