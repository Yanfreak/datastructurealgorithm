class Full(Exception):
    pass

class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=None):
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



class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size 
    
    def is_empty(self):
        """Return `True` is the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e.m FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4: 
            self._resize(len(self._data) // 2)
        return answer 
    
    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self, cap):             # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                # keep track of existing list
        self._data = [None] * cap       # allocate list with new capacity
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]   # intentionally shift indices
            walk = (1+walk) % len(old)  # use old size as modulus
        self._front = 0                 # front has been realigned 


def check_contains(S:ArrayQueue, x):
    Q = ArrayQueue()
    found = False 

    for _ in range(2):
        while not S.is_empty():
            value = S.pop()
            if value == x:
                found = True 
            Q.enqueue(value)
        while not Q.is_empty():
            S.push(Q.dequeue())
    return found 



class LeakyStack(ArrayStack):

    def __init__(self, capacity = 20):
        self._data = [None]*capacity
        self._capacity = capacity
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

undo = LeakyStack()

for i in range(100):
    undo.push(i)

while not undo.is_empty():
    print(undo.pop)