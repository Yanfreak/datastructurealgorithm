from collections import MutableMapping

class MapBase(MutableMapping):
    """Abstract base class that includes a nonpublic _Item class."""

    # nested _Item class 
    class _Item:
        __slots__ = '_key', '_value'
    
        def __init__(self, k, v):
            self._key = k
            self._value = v 

        def __eq__(self, other):
            return self._key == other._key
        
        def __ne__(self, other):
            return not (self == other)
        
        def __lt__(self, other):
            return self._key < other._key

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []        # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value 
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return 
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return 
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key
        