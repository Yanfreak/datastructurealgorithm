class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name 
        self._score = score 

    def get_name(self):
        return self._name 

    def get_score(self):
        return self._score 
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialise scoreboard with given maximum capacity.
        All entries are initially None."""

        self._board = [None] * capacity 
        self._n = 0
    
    def __getitem__(self, k):
        """Return entry at index k. """
        return self._board
    
    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1 
            
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry 


def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
            A[j] = cur


class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26           # temp array for encryption
        decoder = [None] * 26           # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)                




class MatrixwMult(Matrix):
    def __mul__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.mul))
    
    def dot_product(self, other):
        assert len(self._dimensions) == 2, 'Dot product not implemented for rank>2'
        
        
        ar, ac = self._dimensions
        br, bc = other._dimensions
        
        c = self._create_empty_3D_dataset([ar, bc])

        a = self._data
        b = other._data
        
        print(c._dimensions)
        
        for i in range(ar):
            for j in range(bc):
                total = 0
                for k in range(ac):
                    total += a[i][k]*b[k][j]
                    #print (total, a[i][k], b[k][j], 'Index', i, j, k)
                c._data[i][j] = total
                             
        return c
            
        
        
        
        
        
    
mm1 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
mm2 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    
print(mm1*mm2)


mmm1 = MatrixwMult([[1,2,3],[4,5,6]], 2)
mmm2 = MatrixwMult([[1,2,3],[1,2,3],[1,2,3]], 2)


mmm1.dot_product(mmm2)