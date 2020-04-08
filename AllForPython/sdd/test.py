import random
import math
import scipy.special
l = [9.47, 9.71, 9.65, 9.37, 9.16, 10.01, 9.60, 9.23, 10.22, 10.19, 10.18, 8.58, 9.07, 9.32, 9.64, 8.82, 9.33, 9.08, 9.16, 9.15, 9.21, 9.32, 9.42, 9.12, 8.75, 8.77, 9.23, 9.29, 9.35, 9.21, 9.31, 9.12, 9.20, 8.76, 9.65, 8.93, 9.28, 8.83, 8.89, 10.06, 9.31, 9.67, 8.55, 9.17]

# with open('fiz.txt', 'r') as f:
#     for line in f:
#         l.append(float(line))



avarage = sum(l)/len(l)

lsq = [(i - avarage)**2 for i in l]
lnsq = [(i - avarage) for i in l]

sigma = (sum(lsq)/len(l))**0.5
sigma_t = (sum(lsq)/len(l)/(len(l)-1))**0.5

def gauss(t):
    return str(round(( math.exp( -1 * ((t - avarage) ** 2)/(2 * (sigma ** 2)) ) )/(sigma*(2*math.pi)**0.5), 3))

def int_gauss(t):
    return (-0.5)*scipy.special.erf((avarage-t)/(2**0.5 * sigma))

for n, i in enumerate(l):
    print('{} & {} & {} & {} \\\\ [5pt] \\hline'.format(n+1, i, round(i - avarage, 3), round((i - avarage)**2, 3)))
print('Avarage {}'.format(avarage))
print('Min {}'.format(min(l)))
print('Max {}'.format(max(l)))
print('Sigma {}'.format(sigma))
print('Sigmat {}'.format(sigma_t))
print('Strange sum {}'.format(sum(lnsq)))

x = 0.24
mm = min(l)
ranges = [(round(i*x+mm, 2), round((i+1)*x+mm, 2)) for i in range(7)]
for i in ranges:
    counter = 0
    for j in l:
        if (j <= i[1]) and (j >= i[0]):
            counter += 1
    print('{} & {} & {} & {}\\\\ [5pt] \\hline'.format(str(i[0]) + ';' + str(i[1]), counter, round(counter/(len(l)*x), 3), gauss(i[0]) + ';' + gauss(i[1]) ))

sranges = [(round(avarage-(i+1)*sigma, 2), round(avarage+(i+1)*sigma, 2)) for i in range(3)]
for i in sranges:
    counter = 0
    for j in l:
        if (j <= i[1]) and (j >= i[0]):
            counter += 1
    print('{} & {} & {} & {}\\\\ [5pt] \\hline'.format(str(i[0]) + ';' + str(i[1]), counter, round(counter/(len(l)), 3), round(int_gauss(i[1]) - int_gauss(i[0]),3) ))
