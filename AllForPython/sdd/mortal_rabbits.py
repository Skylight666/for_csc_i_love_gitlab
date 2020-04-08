n = 82
m = 19

population = [1]
age = [1] + [0 for i in range(m - 1)]
for cur_mounth in range(n-1):
    new_age = [0 for i in range(m)]
    for i in range(1, m):
        new_age[0] += age[i]
    for i in range(1, m):
        new_age[i] = age[i-1]
    age = new_age
    #print(cur_mounth, age)
print(sum(age))
