# R-4.6
def harmonic_number(n):
    im = 1.0 / n
    if n == 1:
        return im
    elif n > 1:
        return im + harmonic_number(n-1)

harmonic_number(1)
harmonic_number(2)
harmonic_number(3)

# R-4.7
def str_2_int(string, index=0):
    length = len(string)
    if index = length - 1:
        return int(string[index])
    else:
        return int(string[index])*10**(length-index-1) + str_2_int(string, index+1)

# C-4.12
def product(m, n):
    if n == 1:
        return m 
    else:
        return product(m, n-1) + m 

product(4, 3)
product(9,9)

# C-4.14
def move_disk(from_peg, to_peg):
    to_peg.append(from_peg.pop())
    print("==========[Status]==========")
    print("[a]:", a)
    print("[b]:", b)
    print("[c]:", c)

def hanoi(n, from_peg, help_peg, to_peg):
    if n == 1:
        move_disk(from_peg, to_peg)
    else:
        hanoi(n-1, from_peg, to_peg, help_peg)
        move_disk(from_peg, to_peg)
        hanoi(n-1, help_peg, from_peg, to_peg)

n = 9
a = list(reversed(range(1,int(n)+1)))
b = []
c = []

print("[a]: ", a)
print("[b]: ", b)
print("[c]: ", c)
hanoi(9, a, b, c)


# C-4.15
UNK = chr(1000)
def subset(current, remaining):
    if len(s) == 0:
        print('{', str([x for x in current if x != UNK])[1: -1], '}')
    else:
        val = remaining.pop()
        current.append(UNK)
        subset(current, remaining)
        current.pop()

        current.append(val)
        subset(current, remaining)
        current.pop()
        remaining.append(val)

def print_subset(current):
    subset([], list[current])

print_subset({1, 2, 3, 4, 5, 6, 7})


# C-4.16
def reverse(s, i=0):
    if i == len(s) - 1:
        return [s[i]]
    else:
        a = reverse(s, i+1)
        a.append(s[i])
        if i == 0:
            a = ''.join(a)
        return a

s = 'pots&pans'
reverse(s)

# C-4.17
def palindrome(s, first=0):
    if first == len(s)-1-first:
        return True 
    elif first == len(s)-first-2:
        if s[first] == s[len(s)-first-1]: 
            return True
        else:
            return False
    else:
        if s[first] == s[len(s)-1-first]:
            return palindrome(s, first+1)
        else:
            return False

s = 'gohangasalamiimalasagnahog'
v = 'racecar'
x = 'shfkkjbiy'
print(palindrome(s))
print(palindrome(v))
print(palindrome(x))


# C-4.18
VOWELS = {'a', 'e', 'i', 'o', 'u'}
def vowel_consonant_compare(s, v=0, i=0):
    if s[i] in VOWELS:
        v += 1
    if i < len(s)-1:
        return vowel_consonant_compare(s, v, i+1)
    else:
        if v > len(s) - v:
            return True
        else:
            return False


s = 'aaaaaaaaaajjj'
vowel_consonant_compare(s)

# C-4.19
def even_before_odd(nums):
    if not nums:
        return []
    if nums[0] % 2 == 0:
        return [nums[0]] + even_before_odd(nums[1:])
    else:
        return even_before_odd(nums[1:]) + [nums[0]]


# C-4.20
def less_before_greater(S, k):
    if not S:
        return []
    if S[0] <= k:
        return [S[0]] + less_before_greater(S[1:], k)
    else:
        return less_before_greater(S[1:], k) + [S[0]]


# C-4.21
S = [1, 2, 3, 4, 5, 6, 7]
def sum_to_k(nums: List[int], k: int, start: int, end: int) -> List[int]:
    assert len(nums) > 2
    if start == end:
        return []
    if nums[start] + nums[end] == k:
        return [nums[start], nums[end]]
    elif nums[start] + nums[end] < k:
        return sum_to_k(nums, k, start + 1, end)
    else:
        return sum_to_k(nums, k, start, end - 1)

# P-4.23
import os 
def find(path, filename):
    if os.path.isdir(path):
        for obj in os.listdir(path):
            if os.path.isdir(os.path.join(path, obj)):
                find(os.path.join(path, obj), filename)
            elif obj == filename:
                print(os.path.join(path, obj))

# P-4.24