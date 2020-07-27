class Full(Exception):
    pass

class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=20):
        """Create an wmpty stack."""
        self._data = [None] * maxlen
        self._capacity = maxlen
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element `e` to the top of the stack."""
        if self.__len__() >= self._capacity:
            raise Full('Stack is full')
        else:
            self._data.append(e)
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()



# A function that reverses the order of lines in a file.
def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename):
    for line in original:
        S.push(line.rstrip('\n'))   # we will re-insert newlines when writing 
    original.close()

    # now we overwrite with contents in LIFO order 
    output = open(filename, 'w')    # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')    # re-insert newline characters
    output.close()


# Function for matching delimiters in an arithmetic expression
def is_matched(expr):
    """Return `True` if all delimiters are properly match; `False` otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif x in righty:
            if S.is_empty():
                return False 
            if righty.index(c) != lefty.index(S.pop()):
                return False 


def is_matched_html(raw):
    """Return `True` if all HTML tags are properly match; `False` otherwise."""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False 
        tag = raw[j+1:k]
        if not tag.startswith('/'):      # this is opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False             # nothing to match with
            if tag[1:] != S.pop():
                return False            # mismatched delimeter
        j = raw.find('<', k + 1)
    return S.is_empty()


def transfer(S, T):
    """
    Transfer all elements from stack S onto stack T, 
    so that the element that starts at the top of S is the first to be inserted onto T,
    and the element at the bottom of S ends up at the top of T.
    """
    while not S.is_empty():
        T.push(S.pop())
    return T

S = ArrayStack()
T = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.push(6)
transfer(S, T)
T.top()


def rm_stack_elements(stack):
    """recursive method."""
    if not stack.is_empty():
        stack.pop()
        return rm_stack_elements(stack)
    else:
        return 'all removed'

rm_stack_elements(T)
T.is_empty()


def stack_reverse(L):
    M = ArrayStack()
    for i in range(len(L)):
        M.push(L[i])
    for j in range(len(L)):
        L[j] = M.pop()
    return L 

stack_reverse([1, 3, 5, 7, 9, 11])


def find_permutations_stack(n):
    nums = {x for x in range(1, n+1)}
    S = ArrayStack(10)

    for num in nums:
        S.push(([num], nums-set([num])))
    
    while not S.is_empty():
        l, remaining = S.pop()
        if len(remaining) == 0:
            print (l)
        else:
            for n in remaining:
                l2 = l.copy()
                l2.append(n)
                S.push((12, nums-set(l2)))

find_permutations_stack(5)


class LeakyStack(ArrayStack):

    def __init__(self, maxlen=20):
        super().__init__(maxlen)
        self._front = 0
        self._size = 0

    def push(self, value):
        self._data[(self._front + self._size) % len(self._data)] = value
        if self._size == self._capacity:
            self._front += 1
        else:
            self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        rslt = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._size -= 1
        return rslt

undo = LeakyStack(30)

for i in range(100):
    undo.push(i)

while not undo.is_empty():
    print(undo.pop)



class ArrayDoubleStack():
    DEFAULT_CAPACITY = 20
    GROW_RATE = 2
    
    def __init__(self):
        self._sizer = 0
        self._sizeb = 0
        self._data = [None]*self.DEFAULT_CAPACITY
        self._rfront = 0
        self._bfront = self.DEFAULT_CAPACITY //2
        
        
    def is_empty_blue(self):
        return self._sizeb == 0
        
    def is_empty_red(self):
        return self._sizer == 0    
    
    def is_full(self):
        return (self._sizer + self._sizeb) == len(self._data)
    
    
    def push_red(self, value):
        idx = (self._rfront + self._sizer)%len(self._data)
        if self.is_full() or idx == self._bfront : self._resize(len(self._data)*self.GROW_RATE)
        
        new_idx = (self._rfront + self._sizer)%len(self._data)
        self._data[new_idx] = value
        self._sizer += 1
    
    def push_blue(self, value):
        idx = (self._bfront + self._sizeb)%len(self._data)
        if self.is_full() or idx == self._rfront : self._resize(len(self._data)*self.GROW_RATE)
        
        new_idx = (self._bfront + self._sizeb)%len(self._data)
        self._data[new_idx] = value
        self._sizeb += 1
        
    
    def _pop(self, front, size):
        
        ans = self._data[(front + size-1)%len(self._data)]
        self._data[(front + size-1)%len(self._data)] = None
        return ans
    
    def pop_red(self):
        if self.is_empty_red(): raise Empty('Red is empty')
        ans = self._pop(self._rfront, self._sizer)
        self._sizer -= 1
        return ans
    
    def pop_blue(self):
        if self.is_empty_bue(): raise Empty('Blue is empty')
        ans = self._pop(value, self._bfront, self._sizeb)
        self._sizeb -= 1
        return ans
    

    
    def _resize (self, capacity):
        """
        Note, red walks, then blue takes half of the remaining space
        
        """
        
        new_array = [None]*capacity
       
        
        for i in range(self._sizer):
            new_array[i] = self._data[(self._rfront + i)%len(self._data)]    

        
        
        new_frontb = self._sizer + (capacity-self._sizer - self._sizeb)//2
        
        
        for i in range(self._sizeb):
            new_array[i + new_frontb] = self._data[(self._bfront+i)%len(self._data)]
          
        self._rfront = 0
        self._bfront = new_frontb
        self._data = new_array
        
        
        
dA = ArrayDoubleStack()
        
        
for i in range(11):
    dA.push_blue(i)
    dA.push_red(100+i)
    print(dA._data, dA._sizer, dA._sizeb, '\n')
    
    
while not dA.is_empty_red():
    print (dA.pop_red())