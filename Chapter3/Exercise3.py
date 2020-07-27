# R-3.1
import matplotlib.pyplot as plt 
import numpy as np
import math 

x = [10**i for i in range(10)]

funcs = [lambda x: 8 * x,
        lambda x: 4 * x * math.log(x),
        lambda x: 2 * x**2,
        lambda x: x**3,]

ys = []
for func in funcs:
    ys.append(list(map(func, x)))

for y in ys:
    plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')


# C-3.36
def last10(array):
    if len(array) >= 10:
        return sorted(array)[-10: ]
    else:
        return array 


# C-3.45
def find_misssing(S):
    total_list = list(range(len(S)+1))
    total = 1
    for x in total_list:
        total *= x + 1
    for x in S:
        total /= x + 1
    return int(total-1)

find_misssing([0, 1, 2, 3, 4, 6, 7, 8, 9])

# c-3.50
def polynomial(x, coefficients):
    x_tot = 1
    total = 0
    for a in coefficients:
        total += a * x_tot
        x_tot *= x 
    return total 


# C-3.54
import random 

def find_most_frequent(n):
    S = []
    for _ in range(n):
        S.append(random.randint(0, 4*n + 1))
        print(S)
    
    counts = [0] * (4 * n)
    max_int = 0
    for num in S:
        counts[num] += 1
        if counts[num] >= counts[max_int]:
            max_int = num
    
    print(max_int, counts[max_int])
    if counts[max_int] == 1:
        return False 
    else:
        return max_int 

find_most_frequent(1000)

# P-3.57
import time 
import matplotlib.pyplot as plt
import random 

def test_sorted(n_e_max, num_tests=10000):
    xs = [list(range(2**x)) for x in range(1, n_e_max)]
    output_times = []
    times = []
    nlogns = []
    for x in xs:
        random.shuffle(x)
        before = time.time()
        for _ in range(num_tests):
            sorted(x)
        after = time.time()
        times.append(after-before)
        nlogns.append(x**((after-before)/len(x)))
    return (times, nlogns)

n_x_max =15
times, y = test_sorted(n_e_max)
x = [2**x for x in range(1, n_x_max)]

plt.plot(x, y)
plt.show()