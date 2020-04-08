import string
from prettytable import PrettyTable
alp = string.ascii_lowercase

def merge(arr, ans, final):
    while {} in arr:
        arr.remove({})

    check = set()

    if len(arr) == 1:
        for k1, v1 in arr[0].items():
            if k1 in final:
                final[v1] += k1
            else:
                final[v1] = k1

    for n in range(len(arr) - 1):
        a = arr[n]
        b = arr[n+1]
        # if a == {} and b == {}:
        #     continue
        for k1, v1 in a.items():
            flag = False
            for k2, v2 in b.items():
                #print(k1, v1, k2, v2)
                counter = 0
                pos = 0
                for p in range(4):
                    if v1[p] == v2[p]:
                        counter += 1
                    else:
                        pos = p
                if counter == 3:
                    l = list(v1)
                    l[pos] = '-'
                    ans[n][k1+k2] = ''.join(l)
                    check.add(k1)
                    check.add(k2)
                else:
                    flag = True
            if flag:
                if k1 not in check:
                    if k1 in final:
                        final[v1] += k1
                    else:
                        final[v1] = k1
                    # print(k1+'*')
                    # if len(k1) <=2:
                    #     raise Exception
        if n == len(arr) - 2:
            for k2 in b.keys():
                if k2 not in check:
                    if k2 in final:
                        final[v2] += k2
                    else:
                        final[v2] = k2
                    # print(k2+'@')
                    # if len(k2) <=2:
                    #     raise Exception
                    check.add(k2)

    return ans

def print_d(d):
    for a in d:
        if a:
            for k, v in a.items():
                print(k, v)
    print()

def mt(line):
    final = {}
    minterms = []
    # arr = line.split('+')
    # for eq in arr:
    #     mint = ''
    #     eq = list(eq)
    #     for sym in eq:
    #         if eq[0] == '!':
    #             mint += '0'
    #             eq = eq[3:]
    #         else:
    #             mint += '1'
    #             eq = eq[2:]
    #         if eq == []:
    #             break
    #     minterms.append(mint)

    for n, i in enumerate(line):
        if i == '1':
            print(n, end=' ')
            mint = bin(n)[2:]
            if len(mint) != 4:
                mint = (4 - len(mint))*'0' + mint
            minterms.append(mint)

    print()

    minterms = sorted(minterms, key = lambda term: term.count('1'))

    groups1 = [{}, {}, {}, {}, {}]
    noth2 = [{}, {}, {}, {}]
    noth3 = [{}, {}, {}]
    noth4 = [{}, {}]
    noth5 = [{}]

    x = PrettyTable()
    x.field_names = ["Имя", "Ярус", "x1", "x2", "x3", "x4"]

    for n, a in enumerate(minterms):
        groups1[a.count('1')][alp[n]] = a
        x.add_row([alp[n], a.count('1'), *list(a)])

    print(x)
    print()
    print_d(groups1)
    groups2 = merge(groups1, noth2, final)
    print('Сравнение 1')
    print_d(groups2)
    groups3 = merge(groups2, noth3, final)
    print('Сравнение 2')
    print_d(groups3)
    groups4 = merge(groups3, noth4, final)
    # print('Сравнение 3')
    # print_d(groups4)
    groups5 = merge(groups4, noth5, final)
    # print('Сравнение 4')
    # print_d(groups5)

    y = PrettyTable()
    y.field_names = ["Имя"] + list(alp[:len(minterms)])

    for k, v in final.items():
        kkk = lambda o: int((o in set(v)))
        test = [k] + [kkk(o) for o in list(alp[:len(minterms)])]
        y.add_row(test)
    print('Таблица покрытий')
    print(y)
    print()

with open('fek.txt') as f:
    for n, l in enumerate(f, 1):
        print(n)
        print()
        l = list(l)
        while ' ' in l:
            l.remove(' ')
        mt(''.join(l))
        print('-'*50)

# l = '1101000111010001'
# mt(l.strip())
