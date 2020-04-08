arr = []

with open("base.txt") as base:
    for line in base:
        if line.strip():
            l = list(line.replace(' ', '').replace('\xa0', '!').replace(chr(1087), '').replace(chr(1027), '')[:-2]) #.replace('x1', 'a').replace('x2', 'b').replace('x3', 'c').replace('x4', 'd')
            print(ord(l[13]))
            # for n, ch in enumerate(l):
            #     if ch not in ['1', '2', '3', '4', 'x', '+']:
            #         l[n] = '!'
            arr.append(''.join(l) + '\n')


with open('ans.txt', 'w') as f:
    f.writelines(arr)
