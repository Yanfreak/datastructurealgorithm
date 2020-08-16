# R-12.7
"""Suppose we are given two n-element sorted sequences A and B each with distinct elements,
but potentially some elements that are in both sequnces.
Describe an O(n)-time method for computing a sequnce representing the union A U B (with no deplicates) as a sorted sequnce."""
# both A and B are sorted 
def unionAB(A:list, B:list):
    C = []
    i = j = 0
    n = len(A)
    while i < n and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
        else:
            C.append(B[j])
            j += 1
    if i < n:
        C.extend(A[i:n])
    if j < n:
        C.extend(B[j:n])
    return C

A = [2, 4, 6, 8, 10, 11, 12, 13]
B = [1, 2, 5, 7, 9, 11, 14, 19]
unionAB(A, B)

# R-12.18
# radix-sort
