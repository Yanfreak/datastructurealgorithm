class Empty(Exception):
    pass

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

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
        self._head = None 
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size 
    
    def is_empty(self):
        """Return `True` if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element `e` to the top of the stack."""
        self._head = self._Node(e, self._head)  # create and link a new node 
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise `Empty` exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise `Empty` exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next 
        self._size -= 1
        return answer



class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element 
            self._next = next
    
    def __init__(self):
        """Create an empty queue."""
        self._head = None 
        self._tail = None 
        self._size = None 
    
    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None 
        return answer
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest 
        self._size += 1

    def rotate(self):
        if self._size > 0:
            old_head = self._head 
            self._head = old_head._next
            self._tail._next = old_head 
            old_head._next = None 
    
    def concatenate(self, Q2: LinkedQueue):
        """Takes all elements of LinkedQueue Q2 and appends them to the end of the original queue. 
        The operation should run in O(1) time and should result in Q2 being an empty queue."""
        self._tail._next = Q2._head
        self._tail = Q2._tail
        Q2._head = None 



class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element 
            self._next = next 
    
    def __init__(self):
        """Create an empty queue."""
        self._tail = None 
        self._size = 0

    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next 
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next 
        if self._size == 1:
            self._tail = None 
        else:
            self._tail._next = oldhead._next 
        self._size -= 1 
        return oldhead._element 
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
        self._tail = newest 
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next    


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'    # streamline memory

        def __init__(self, element, prev, next):    # initialize node's fields
            self._element = element
            self._prev = prev
            self._next = next 
    
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header 
        self._size = 0
    
    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element `e` between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev 
        successor = node._next 
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element     # wait, i think this is a shallow copy??
        node._prev = node._next = node._element = None
        return element 
    
    def reverse(self):
        """Reverse the order of the list, yet without creating or destroying any nodes."""

        self._header, self._trailer = self._trailer, self._header
        self._header._prev, self._header._next = self._header._next, self._header._prev
        self._trailer._prev, self._trailer._next = self._trailer._prev, self._trailer._next 
        if not self.is_empty():
            cursor = self._header._next 
            for _ in range(self._size):
                cursor._next, cursor._prev = cursor._prev, cursor._next
                cursor = cursor._next




class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty('Deuque is empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)


class PositionalList(_DoublyLinkedBase):
    """A sequential container of ellements allowing positional access."""

    # nested Position class 
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node 
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return `True` if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node 

        def __ne__(self, other):
            """Return `True` if other does not represent the same location."""
            return not (self == other)
    
    # utility method 
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:       # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node 
    
    def _make_position(self, node):
        """Return Position instance for given node (or `None` if sentinel)."""
        if node is self._header or node is self._trailer:
            return None 
        else:
            return self.Position(self, node)
    
    # accessors 
    def first(self):
        """Return the first Position in the list (or `None` if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or `None` if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    # mutators 
    # overide inherited version to return Position, rather than Node 
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element `e` at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element `e` at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element `e` into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p."""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def max(self):
        """Return the maximum element from the instance."""
        currentmax = self.first().element
        node_iter = self.__iter__()
        for n in node_iter:
            if n.element > currentmax:
                currentmax = n.element 
        return currentmax 
    
    def find(self, e):
        """returns the position of the (first occurrence of) element e in the list (or None if not found)."""
        p = self._header._next
        if p is None:
            return None
        elif p._element == e:
            return self._make_position(p)
        else:
            return self.find(e)

    #def swap(self, p: _Node, q: _Node):



# sorting a positional list 
def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot 
            else:
                walk = marker 
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


class FavouritesList:
    """List of elements ordered from most frequently accessed to least."""

    # nested _Item class
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    
    # nonpublic utilities 
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk 
    
    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count 
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                        walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # public methods 
    def __init__(self):
        """Create an empty list of favourites."""
        self._data = PositionalList()
    
    def __len__(self):
        """Return number of entries on favourites list."""
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)      # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))  # if new, place at end
        p.element()._count += 1     # always increment count
        self._move_up(p)            # consider moving forward
    
    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
    
    def top(self, k):
        """Generate sequence of top k elements in term of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for _ in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

    def clear(self):
        """Returns the list to empty."""
        walk = self._data.first()
        while walk is not None:
            walk = self._data.after(walk)
            self._data.delete(self._data.before(walk)) 
    
    def reset_counts(self):
        """Rresets all elements’ access counts to zero (while leaving the order of the list unchanged)."""
        p = self._data.first()
        while p is not None:
            p.element()._count = 0
            p = self._data.after(p)





class FavouritesListMTF(FavouritesList):
    """List of elements ordered with move-to-front heuristic."""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position `p` to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))
    
    # we override top because list is nno longer sorted
    def top(self, k):
        """Generate sequence of top `k` elements in terms of access count."""
        if not 1<= k <= len(self):
            raise ValueError('Illegal value for k')

        # begin by making a copy of the original list 
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)
        
        # repeatedly find, report, and remove element with largest count
        for _ in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk 
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element().old_value
            temp.delete(highPos)