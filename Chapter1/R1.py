
# R-1.1
def is_multiple(n, m):
    """
    Takes two integer values and returns True if `n` is a multiple of `m`, that is, `n = mi` for some integer `i`, and `False` otherwise.
    """
    if isinstance(n, int) and isinstance(m, int):
        if n % m == 0:
            return True 
        else:
            return False
    else:
        raise ValueError('At least one of the input values are not integer.')

is_multiple(100, 10)
is_multiple(12, 5)
is_multiple(3.1, 9.2)
is_multiple(2, 0) # Raise ZeroDivisionError

# R-1.2
def is_even(k):
    """
    Takes an integer value and returns `True` if `k` is even, and `False` otherwise.
    However this function cannot use the multiplication, modulo, or division operator.
    """
    if isinstance(k, int):
        return not k & 1
    else:
        raise ValueError('At least one of the input values are not integer.')

is_even(24)
is_even(3)
is_even(-2)
is_even(0) # question: is zero even?

# R-1.3
def minmax(data):
    """
    Takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two.
    Using the built-in functions `min` or `max` is not allowed in implementing your solution.
    """
    minnum = maxnum = data[0]
    for i in range(len(data)-1): # `for a in data[1:]:` would make it easier.
        minnum = data[i+1] if data[i+1] < minnum else minnum
        maxnum = data[i+1] if data[i+1] > maxnum else maxnum
    return (minnum, maxnum)

minmax([6, 2, 9, -1.3, 7.8])

# R-1.4

def smallersumsquare(n):
    """
    Takes a positive integer `n` and returns the sum of the squares of
    all the positive integers smaller than `n`.
    """
    if isinstance(n, int) and n > 0:
        return sum(a*a for a in range(1, n))
    else:
        raise ValueError

# R-1.5
def short_smallersumsquare(n):
    return sum(a*a for a in range(1, n))


# R-1.6
def oddsumsquare(n):
    """
    Takes a positive integer `n` and returns the sum of the squares of all the odd positive integers smaller than `n`.
    """
    if isinstance(n, int) and n > 0:
        odd = n-2 if n & 1 else n - 1
        s = 0
        while odd > 0:
            s += odd * odd 
            odd -= 2
        return s
    else:
        raise ValueError 

oddsumsquare(5)
oddsumsquare(6)
oddsumsquare(0)
oddsumsquare(-3)

# R-1.6
def shortr1dot5(n):
    return sum(a*a for a in range(1, n, 2))

shortr1dot5(5)
shortr1dot5(6)

# R-1.8
>>> s[n-k-1:n-1]

# R-1.9
>>> range(50, 81, 10)

# R-1.10
>>> range(8, -9, -2)

# R-1.11
>>> list(2**a for a in range(9))

# R-1.12
from random import randrange
randrange(0, 10)

# C-1.13
# list[i] = list[n-1-i] list[n-1-i] = list[i] for i in range(n//2) 

# C-1.15
def is_unique(data: List[Num]):
    return len(data) == len(set(data))

# C-1.16
# desinate

# C-1.18
>>> print([n*(n+1) for n in range(0, 10)])

# C-1.19
>>> print([chr(ord('a')+i) for i in range(0, 26)])

# C-1.20
from random import randint 
#def shuffle(data: List[Any]) -> None:
def shuffle(data):
    for i in range(len(data)-1, 0, -1):
        j = randint(0, i-1)
        data[i], data[j] = data[j], data[i]
        return data 

l1 = [1, 2, 3, 4]
l2 = (1, 2, 3, 4, 5)
shuffle(l1)
shuffle(l2)

# C-1.21
def print_reverse() -> None:
    lines = []
    while True:
        try:
            line = input("input something: ")
        except EOFError:
            break 
        lines.append(line)
    print('\n')
    for line in reversed(lines):
        print(line)

# C-1.22 
def array_dot_product(a, b):
    return [i*j for i, j in zip(a, b)]
    # return [a[i] * b[i] for i in range(len(a))]
    # no warning for the condition where len(a) != len(b)

# C-1.23
def check_overflow():
    data = [1, 2, 4]
    try:
        data[3] = 0
    except IndexError:
        print("Don't try buffer overflow attacks in Python.")

# C-1.24
'''
    def hsfush(data):
        return len([i for i in data.lower() if i in ['a', 'e', 'i', 'o', 'u']])
'''

# C-1.25
def remove_punctuation(sentence: str):
    removed = [char for char in sentence if (ord('A') <= ord(char) <= ord('z')) or ord(char) == ord(' ') or (ord('0') <= ord(char) <= ord('9'))]
    return ''.join(removed)

remove_punctuation("Look at Izuku's messy hair, Shouto!")


# P-1.29
"""Write a Python program that outputs all possible strings formed by using the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once."""
from itertools import permutations
s = 'catdog'
for x in permutations(s):
    print(''.join(x))

# alternative 
def add_char(char, string_list):
    return [char + string for string in string_list]

def flatten_list(lists):
    result = []
    for l1 in lists:
        result += l1
    return result 

def permutation(chars):
    if len(chars) == 1:
        return [chars]
    return flatten_list([add_char(chars[i], permutation(chars[:i] + chars[i+1: ])) for i in range(len(chars))])

permutation('catdog')

# P-1.30
""" Write a Python program that can take a positive interger greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2."""
from math import floor, log2
n = int(input("Enter an integer:"))
assert n > 2
print(f"Need {(int(floor(log2(n))))} times to divide")

# P-1.34
"""
A common punishment for school children is to write out the sentence multiple times.
Write a Python stand-alone program that will write out the following sentence on hundred times:
    "I will never spam my friends again."
Your program should number each of the sentences and it should make eight different random-looking typos.
"""
import random 

def create_typo(message, char_range):
    error_spot = random.randrange(0, len(message))
    error_character = random.choice(char_range)
    incorrect_message = list(message)
    incorrect_message[error_spot] = chr(error_character)
    return (''.join(incorrect_message))

def spammm(message, num_errors=8, num_lines=100):
    # find all the character values for Aa-Zz
    char_range = list(range(ord('A'), ord('Z')+1)) + list(range(ord('a'), ord['z']+1))
    line_count = 0
    error_lines = set()
    while line_count < num_errors:
        new_error_line = random.randrange(num_lines)
        if new_error_line not in error_lines:
            error_lines.add(new_error_line)
            line_count += 1
    
    for i in range(num_lines):
        if i not in error_lines:
            print(message)
        else:
            print(create_typo(message, char_range), 'TYPOOOO')

spammm('I will never spam my friends again')





#P-1.35
"""
The birthday paradox says that the probability that two people in a room will have the same birthday is more than half, provided `n`, the number of people in the room, is more than 23.
This property is not really a paradox, but many people find it surprising. 
Design a Python program that can test this paradox by a series of experiements on radomly generated birthdays, which test this paradox for n = 5, 10, 15, 20, ..., 100.
"""
import random 

def test_birthday_paradox(num_people):
    birthdays = [random.randrange(0, 365) for p in range(num_people)]
    birthday_set = set()
    for bday in birthdays:
        if bday in birthday_set:
            return True 
        else:
            birthday_set.add(bday)
    return False

def paradox_stats(num_people=23, num_trials=100):
    num_successes = 0
    for tri in range(num_trials):
        if test_birthday_paradox(num_people):
            num_successes += 1
    return num_successes/num_trials 

for x in range(5, 101, 5):
    print(f'For {x} people, the probability is approximately: {paradox_stats(x)}')


# P-1.36
"""
Write a Python program that inputs a list of words, seperated by whitespace, and outputs how many times each word appears in the list.
"""
import random 

def clean_up_text(text):
    text = text.lower()

    unwanted_chars = {'\n', '.', '!', "'", '?', ','}
    for char in unwanted_chars:
        text = text.replace(char, ' ')
    return text 

def open_txt_file(filepath):
    f = open(filepath)
    text = f.read()
    return(text)

def word_count(text):
    text = clean_up_text(text)
    word_array = text.split(' ')
    word_counts = {}
    for w in word_array:
        if w in word_array:
            word_counts[w] += 1
        else:
            word_counts[w] = 1
    
    if '' in word_counts: 
        del word_counts['']
    
    return word_counts 