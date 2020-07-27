# R-5.7
import random 
n = 16
A = [i for i in range(1, n)]
random.shuffle(A)
A.insert(random.randint(0, n-1), random.randint(1, n-1))

def find_dup(nums):
    n = len(nums)
    return sum(nums) - n * (n - 1) // 2

# R-5.11
dataset = [ [0] * c for j in range(r)]
sum(dataset[i][j] for i in range(c) and j in range(r))

# R-5.14
from random import randrange

def my_shuffle(d):
    a = []
    for k in range(len(d)):
        i = randrange(len(d))
        a.append(d.pop(i))
    return a


# R-5.27
import math
import random

def find_missing(S):
    max_num = 2**(math.ceil(math.log(len(S), 2))+1)
    num_count = [0]*(max_num+1)
    for element in S:
        num_count[element] += 1
        
    missing_nums = []
    for i in range(len(num_count)):
        if num_count[i] == 0:
            missing_nums.append(i)
            
    return missing_nums
    

n = 20
S = [random.randint(0, 2**(math.ceil(math.log(len(S), 2))+1)-1) for _ in range(n)]
print(S)
print(find_missing(S))

# R-5.29
def natural_join(A, B):
    Y_map = {}
    for x, y in A:
        if y in Y_map: Y_map[y].add(x)
        else: Y_map[y] = set({x})
    
    joined = []
    for y, z in B:
        if y in Y_map:
            joined.extend([(x, y, z) for x in Y_map[y]])
    
    return joined 

A = [(1,1), (1,3), (3,4), (3,5), (5,6), (4,5)]
B = [(1,4), (1, 5), (4, 2), (5, 1)]

print('Typical example', natural_join(A, B))
"""
Analysis:

The first part iterates O(n) times with each iteration taking O(1) time -> O(n)

The second part iterates O(m) times, with each join taking O(n) in the worst case.

For example, if all items in B start with 1 and all items in A end with 1, there will be m*n combos

Therefore the overall performance is O(n) + O(m*n), which is O(m*n)


"""

A = [(x, 1) for x in range(10)]
B = [(1, x) for x in range(10)]

print('\n\nWorst Case Example', natural_join(A, B))



# C-5.30
import random 

def binary_search(array, low, high, target):
    if low >= high:
        return low 
    
    mid = (low + high) // 2
    if array[mid] == target:
        return mid 
    elif array[mid] > target:
        return binary_search(array, low, mid-1, target)
    else:
        return binary_search(array, mid+1, high, target)

def packet_receiver(S):
    final_array = []
    for i in range(len(S)):
        packet = S[i]       # simulates her recieving that packet
        index = binary_search(final_array, 0, len(final_array), packet)
        index = min(index, len(final_array - 1))
        if final_array and final_array[index] < packet:
            index += 1
        final_array.insert(index,  packet)
        print(f'New Packet: {packet} ->'m '\t', final_array)

S = list(range(17))
random.shuffle(S)
packet_receiver(S)


# C-5.31
def list_r(S):
    total = 0
    if not isinstance(S, list):
        return S
    else:
        for element in S: 
            total += list_r(element)
    return total 


# P-5.32
"""
Write a Python function that takes two three-dimensional numeric data sets 
and adds them componentwise.
"""
import operator
class Matrix():
    #For subclassing...
    @classmethod
    def _get_cls(cls):
        return cls
    
    
    def __init__(self, data, num_dims = 3):
        self._data = data
        self._dimensions = []
        self._ndims = num_dims
        temp = data
        for i in range(num_dims):
            self._dimensions.append(len(temp))
            temp = temp[0]   
            
            
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return (self._dimensions[0])
        
        
    def __repr__(self):
        return (f'{self._ndims}D Matrix with dimensions {self._dimensions}:' + '\n' + f'{self._data}')
    
    def _create_empty_3D_dataset(self, dimensions):
        a = None
        for d in reversed(dimensions):
            a = [None for _ in range(d)] if a is None else [a.copy() for _ in range(d)]
        return self._get_cls()(a, len(dimensions))
    
    
    def _op_lists_r(self, a, b, c, operation):
        """
        a + b = c
        """
        assert len(a) == len(b) == len(c), 'Length mismatch'
        for i in range(len(a)):
            if isinstance(a[i], list): self._op_lists_r(a[i], b[i], c[i], operation)
            else: c[i] = operation(a[i],b[i])
        return c
            
    
    def __add__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.add))
        
m1 = Matrix([[[i for i in range(10)] for i in range(7)] for i in range(4)])
m2 = Matrix([[[i for i in range(10)] for i in range(7)] for i in range(4)])
print(m1)

print(m1 + m2)