c1, c2, c3, theta = [float(i) for i in input('Input c1 c2 c3 theta ').split()]

c_with_line = (c1 + c2 + c3)/3

S = (((c_with_line-c1)**2 + (c_with_line-c2)**2 + (c_with_line-c3)**2)/2)**(1/2)

epsilon = 4.3 * S / (3)**(1/2)

S_theta = theta / (1.1 * (3)**(1/2))

S_x = S / (3)**(1/2)

theta_div_S_x = theta / S_x

S_sigma = (S_x**2 + S_theta**2)**(1/2)

K = (epsilon + theta)/(S_x + S_theta)

if (theta / S_x) < 0.8 :
    delta = epsilon
elif (theta / S_x) > 8 :
    delta = theta
elif (theta == S_x) :
    delta = 0.8*(theta + S_x)
else:
    delta = K * S_sigma

print('c_with_line', c_with_line)
print('S', S)
print('S_x', S_x)
print('ε', epsilon)
print('θ/S_x ', theta_div_S_x)
print('Sθ', S_theta)
print('K', K)
print('S_Σ', S_sigma)
print('Δ', delta)
input()
