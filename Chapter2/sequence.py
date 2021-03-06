from abc import ABCMeta, abstractmethod

def Sequence(metaclass=ABCMeta):
    """OUr own version of `collections.Sequence` abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
    
    @abstractmethod 
    def __getitem__(self, j):
        """Return the element at index `j` of the sequence."""

    def __contains__(self, val):
        """Return `True` if `val` found in the sequence; `False` otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False 
    
    def index(self, val):
        """Return leftmost index at which `val` is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:      # leftmost match
                return j 
        raise ValueError('value not in sequence')   # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k 
    
    def __eq__(self, another):
        """Return `True` pricisely when the two sequences are elemnt by element equivalent."""
        if len(self) != len(another):
            return False
        else:
            for i in range(len(self)):
                if self[i] != another[i]:
                    return False 
            return True 
    
    def __lt__(self, another):
        """lexicographic comparison `seq1 < `seq2`"""
        for i in range(len(self)):
            if self[i] < another[i]:
                return True 
            return False 
            