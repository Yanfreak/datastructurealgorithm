class Empty(Exception):
    pass

class ArrayDeque():
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._front = 0 
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size 
    
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]
    
    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[(self._front + self._size - 1) % len(self._data)]
    
    def add_first(self, value):
        if self._size == len(self._data):
            self._resize(self._size * 2)
        self._data[(self._front - 1) % len(self._data)] = value 
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        fst = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return fst 
    
    def add_last(self, value):
        if self._size == len(self._data):
            self._resize(self._size * 2)
        self._data[(self._front + self._size) % len(self._data)] = value 
        self._size += 1

    def remove_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        lst = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size) % len(self._data)] = None
        self._size -= 1
        return lst
    
    def _resize(self, capacity):
        old = self._data 
        self._data = [None] * capacity
        for i in range(len(old)):
            self._data[i] = old[(self._front + i) % len(old)]
        self._front = 0

DEQ = ArrayDeque()


print('Adding last')
for i in range(10):
    DEQ.add_last(i)
    print (i, DEQ._data)
    
print ('Adding first')
for i in range(20, 10, -1):
    DEQ.add_first(i)
    print (i, DEQ._data)
    
print('Performing the removals')
while not DEQ.is_empty():
    print ('Remove first', DEQ.first(), DEQ.remove_first(), 'Remove last', DEQ.last(),  DEQ.remove_last())