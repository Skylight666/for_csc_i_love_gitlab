q = int(input())
for i in range(q):
    a = int(input())
    ll = sorted([int(k) for k in input().split() if int(k) <= 2048], reverse=True)
    ans = 0
    for k in ll:
        if ans + k <= 2048:
            ans += k
        else:
            continue
    print('YES' if ans == 2048 else 'NO')
