class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence. """
        self._seq = sequence    # keep a reference to the underlying data
        self._k = -1            # will increment to 0 on first call to the next
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1                        # advance to next index
        if self._k < len(self._seq):        
            return(self._seq[self._k])      # return the data element.
        else:
            raise StopIteration()           # there are no more elements
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class ReversedSequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)
    
    def __next__(self):
        self._k -= 1
        if self._k > -1:
            return self._seq[self._k]
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

        