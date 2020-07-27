from link import Empty, LinkedStack, LinkedQueue, LinkedDeque, CircularQueue, _DoublyLinkedBase, PositionalList

# R-7.1
def get_nd2last(L: LinkedStack):
    node = L._head
    while node._next._next is not None:
        node = node._next
    return node._element
    # _Node class.

# R-7.8
def get_middle(DL: _DoublyLinkedBase):
    start = DL._header
    ending = DL._trailer 
    while not (start is ending or start._next is ending):
        start = start._next 
        ending = ending._prev 
        return start 
    # running time -- O(n/2)

# R-7.9
def concatenating_dll(l1: _DoublyLinkedBase,
                      l2: _DoublyLinkedBase) -> _DoublyLinkedBase:
    l1._tailer._prev._next = l2._header._next
    l2._header._next._prev = l1._tailer._prev
    return l1


# C-7.24
class StackADTWithHeader:
    """Stack ADT using a singly linked list that includes a header sentinel."""
        # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element 
            self._next = next 

    # stack methods 
    def __init__(self):
        """Create an empty stack."""
        self._header = self._Node(None, None)
        self._header._next = None 
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size 
    
    def is_empty(self):
        """Return `True` if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element `e` to the top of the stack."""
        new = self._Node(e, self._header._next)
        self._header._next = new
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise `Empty` exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._header._next._element
    
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise `Empty` exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._header._next._element
        poped_node = self._header._next
        self._header._next = poped_node._next 
        self._size -= 1
        return answer


# C-7.25
class QueueADTWithHeader:
    """Queue ADT using a singly linked list that includes a header sentinel."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element 
            self._next = next
    
    def __init__(self):
        """Create an empty queue."""
        self._header = self._Node(None, None)
        self._header._next = None
        self._tail = None 
        self._size = None 
    
    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._header._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        the_node = self._header._next
        self._header._next = the_node
        answer = the_node._element 
        the_node = None 
        self._size -= 1
        if self.is_empty():
            self._tail = None 
        return answer
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._header._next = newest
        else:
            self._tail._next = newest
        self._tail = newest 
        self._size += 1
