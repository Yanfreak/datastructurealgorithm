class Progression:
    """
    Iterator producing a generic progression.

    Defualt iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialise current to the first value of the progression."""
        self._current = start 

    def _advance(self):
        """
        Update `self._current` to a new value.

        This should be overridden by a subclass to customise progression.
        
        By convention, if current is set to `None`, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current value to return 
            self._advance()             # advance to prepare for next time
            return answer
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
    
    def print_progression(self, n):
        """Print next `n` values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.

        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):     # overide inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        base        the fixed constant multiplied to each term (default 2)
        start       the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base 

    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalised Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """
        Create a new fibonacci progression.

        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """
        super().__init__(first)         # start progression at first
        self._prev = second - first     # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


class AbsDifferenceProgression(Progression):
    """
    Iterator producing a progression in which each value is the absolute value of the difference between the previous two values.
    Accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.
    """

    def __init__(self, first=2, second=200):
        self._current = first 
        self._prev = first + second 

    def __next__(self):
        answer = self._current 
        self.current, self_prev = abs(self._current - self._prev), self._current
        return answer


class SqureRootProgression(Progression):
    """Each value of the progression is the square root of the previous value."""

    def __init__(self, start=65536.0):
        super().__init__(start)

    def _advance(self):
        from math import sqrt
        self._current = sqrt(self._current)

