class Vector:
    """
    Represent a vector in a multidimensional space.
    """

    def __init__(self, d):
        """Create d-dimensional vector of zeros if d is an integer.
        Transform the given data to a vector if d is a list."""
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = d 
    
    def __len__(self):
        """Return the dimensional of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return `jth` coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set `jth` coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):     # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))      # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Return the difference of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return the negated vector"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result 
    
    def __mul__(self, n):
        """Multiply"""
        if isinstance(n, Vector):
            if len(self) != len(n):
                raise ValueError("the vectors' dimensions must agree")
            result = 0 
            for j in range(len(self)):
                result += self[j] * n[j]
            return result 
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * n 
            return result 

    def __rmul(self, n):
        return self.__mul__(n)
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other. """
        return self._coords == other._coords
    
    def __ne__(self, other):
        """Return `True` if vector has same coordinates as other. """
        return not self == other        # relies on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
        