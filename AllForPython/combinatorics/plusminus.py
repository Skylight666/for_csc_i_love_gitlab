import itertools
numbers = [7330, 5700, 294, 420]
need = [3670, 2800, 210, 720]
buffer = []
mask = ''
control_sum = 2344
mc = len(numbers)
for i in itertools.product('10', repeat=mc): # 1 = - ; 0 = + ;
    for z, n in enumerate(numbers):
        sign = 1 if int(i[z]) else -1
        buffer += [n * sign]
    if sum(buffer) == control_sum:
        mask = i
    # for l in buffer:
    #     print(l, end = '')
    # print()
    buffer = []
print(mask)
for z, n in enumerate(need):
    sign = 1 if int(mask[z]) else -1
    buffer += [n * sign]
print(sum(buffer))
