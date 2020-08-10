from Chapter7.link import LinkedQueue
import math

def merge(S1, S2, S):
    """Merge two sorted Python list S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[j]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return 
    # divide
    mid = n // 2
    S1 = S[0:mid]       # note that slice exclude 'mid]'
    S2 = S[mid:n]
    # conquer (with recursion)
    merge_sort(S1)
    merge_sort(S2)
    # merge results
    merge(S1, S2, S)


def merge_linked_list_ver(S1:LinkedQueue, S2:LinkedQueue, S:LinkedQueue):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())

def merge_sort_linked_list_ver(S:LinkedQueue):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return 
    # divide 
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    # conquer (with recursion)
    merge_sort_linked_list_ver(S1)
    merge_sort_linked_list_ver(S2)
    # merge results
    merge_linked_list_ver(S1, S2, S)


def merge_bottom_up(src, result, start, inc):
    """Merge `src[start:start+inc]` and `scr[start+inc+2*inc]` into result."""
    end1 = start + inc                  # boundary for run 1
    end2 = min(start+2*inc, len(src))   # boundary for run 2
    x, y, z = start, start+inc, start   # index into run 1, run 2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]; x += 1
        else:
            result[z] = src[y]; y += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]

def merge_sort_bottom_up(S:list):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n, 2))
    src, dest = S, [None] * n               # make temporary storage for dest
    for i in (2**k for k in range(logn)):   # pass i creates all runs of length 2i
        for j in range(0, n, 2*i):          # each pass merges two length i runs
            merge_bottom_up(src, dest, j, i)
        src, dest = dest, src   # reverse roles of lists
    if S is not src:
        S[0:n] = src[0:n]       # additional copy to get results to S


def quick_sort(S:LinkedQueue):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return
    # divide 
    p = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif S.first > p:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    # ocnquer (with recursion)
    quick_sort(L)
    quick_sort(G)
    # concatenate results 
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


def inplace_quick_sort(S:list, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return 
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)

import random

def quick_select(S:list, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]
    pivot = random.choice(S)
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if pivot < x]
    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot 
    else:
        j = k - len(L) - len(E)
        return quick_select(G, j)