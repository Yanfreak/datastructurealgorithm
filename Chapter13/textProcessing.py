def find_brute(T:str, P:str):
    """Return the lowest index of T at which substring P begins (or elese -1)."""
    n, m = len(T), len(P)
    for i in range(n-m+1):  # try every potential starting index within T
        k = 0               # an index into pattern P
        while k < m and T[i+k] == P[k]: # kth character of P matches
            k += 1
        if k == m:          # reaches the end of pattern
            return i        # substring T[i:i+m] matches P
    return -1           # failed to find a match starting with any i

T = "abacaabaccabacabaabb"
P = "abacab"


def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P beigins (or else -1)."""
    n, m = len(T), len(P)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[P[k]] = k      # later ooccurrence overwrites
    # align end of pattern at index m-1 of text
    i = m - 1               # an index into T
    k = m - 1               # an index into P
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i 
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)    # case analysis for jump step
            k = m - 1               # restart at end of pattern
    return -1


def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    if m == 0: return 0
    fail = compute_kmp_fail(P)
    j = 0       # index into text
    k = 0       # index into pattern
    while j < n:
        if T[j] == P[k]:    # P[0:1+k] matched thus far
            if k == m - 1:  # match is complete
                return j - m + 1
            j += 1          # try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1]   # reuse suffix of P[0:k]
        else:
            j += 1
    return -1

def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m      # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:        # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:    # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:     # k follows a matching prefix
            k = fail[k-1]
        else:           # no match found starting at j 
            j += 1
    return fail 


# from Chapter5.example import 
def matrix_chain(d):
    """d is a list of n+1 numbers such that size of kth matrix is d[k]-by-d[K+1].
    Return an n-by-n table such taht N[i][j] represents the minimum number of multiplications needed to compute the product of Ai through Aj inclusive.
    """
    n = len(d) - 1          # number of matrices
    N = [[0] * n for i in range(n)]     # initialize n-by-n result to zero
    for b in range(1, n):   # number of products in subchain
        for i in range(n-b):    # start of subchain
            j = i + b
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N 


def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
    n, m = len(X), len(Y)
    L = [[0] * (m+1) for k in range(n+1)]   # (n+1) * (m+1) table
    for j in range(m):
        for k in range(m):
            if X[k] == Y[k]:
                L[j+1][k+1] = L[j][k] + 1
            else:       # choose to ignore one character
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L 


def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table L."""
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:          # common characters remain
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))