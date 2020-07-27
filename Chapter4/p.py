# A recursive implementation of the Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# English ruler
def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length 
    if tick_label:
        line += ' ' + tick_label 
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(senter_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


# Binary search
def binary_search(data, target, low, high):
    """
    Return `True` if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False 
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True 
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


# File system 
"""
Algorithm `DiskUsage(path)`:
    Input: A string designating a path to a file-system entry
    Output: The cumulative disk space used by that entry and any nested entries
    total = size(path)
    if path represents a directory then
        for each child entry stored within directory path do
            total = total + DiskUsage(child)
    return total
"""
import os 

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)       # account for direct usage
    if os.path.isdir(path):             # if this is a directory
        for filename in os.listdir(path):   # find the children
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total 


# sum list
def linear_sum(S, n):
    """Return the sum of the first n numbers of a sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

# reversing a sequence with recursion 
def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


# recursive algorithms for computing powers
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n+1)

# computing the power function using repeated squaring 
def power_2version(x, n):
    if n == 0:
        return 1
    else:
        partial = power_2version(x, n//2)
        result = partial * partial 
        if n % 2 ==1:
            return *= x
        return result 


# sum using binary recursion
def binary_sum(S, start, stop):
    """Return the sum of the numbers in simplicit slice S[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

