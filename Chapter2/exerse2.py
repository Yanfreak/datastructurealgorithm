# R-2.4
"""
Write a Python calls, `Flower`, that has three instance variables of type `str`, `int`, and `float`, 
that respectively represent the name of the flower, its number of petals, and its price. 
Youe class must include a constructor method that initialises each variable to an appropriate value, 
and your class should include methods for setting the value of each type, and retrieving the value of each type.
"""
class Flower():

    def __init__(self, name, petal_num, price):
        self._name = name 
        self._petals = petal_num
        self._price = price 
    
    def get_name(self):
        return self._name 
    
    def get_petals(self):
        return self._petals
    
    def get_price(self):
        return self._price 
    
    def set_name(self, name):
        self._name = name 

    def set_petals(self, petals):
        self._petals = petals 
    
    def set_price(self, price):
        self._price = price 

# R-2.18
fib = FibonacciProgression(2, 2)
fib.print_progression(8)

# R-2.19
steps = 2 ** (63 - 7)

# R-2.20
"""
If behaviour changes in A without D knowing (ex. different teams or people working on it),
it can be very difficult to troubleshoot the problems.
You also have a larger change of namespace conflicts that you aren't aware of 
"""


# P-2.34
class DocumentReader():

    def __init__(self, filepath):
        self._filepath = filepath
        self._total_characters = 0
        self._charcount = self._initialize_array()

        self._read_document()
    
    def _read_document(self):
        f = open(self._filepath)
        all_text = f.read().lower()
        for char in all_text:
            if self._check_if_character(char):
                self._charcount[ord(char)-ord('a')] += 1
        self._total_characters = sum(self._charcount)

    def _initialize_array(self):
        return [0] * (ord('z') - ord('a') + 1)
    
    def _check_if_character(self, char):
        number = ord(char)
        if number >= ord('a') and number <= ord('z'):
            return True
        else:
            return False 
    
    def output_graph(self):
        max_value = max(self._charcount)
        for i in range(len(self._charcount)):
            print(chr(i + ord('a')), 'X' * int(self._charcount[i] / max_value * 100))
        print('Each `x` represents:', max_value*100, 'instances of that character (rounded down)')

aaa = DocumentReader(r'')
aaa.output_graph()


# P-2.35
"""Write a set of Python classes that an simulate an Internet application in which one party, Alice, is periodically creating set of packets that she wants to send to Bob.
An Internet process is continually checking if Alice has any packets to send, and if so, it delivers them tp Bob's computer, and Bob is periodically checking if his computer has a packet from Alice, and if so, he reads and deletes it."""

import random

#Unknowns: What happens if you create a new packet without deleting the old one?
#Auume it overwrites it


class AliceBot():
    CHANCE_OF_ACTING = 0.3
    def __init__(self):
        self._current_packet = None
    
    def act(self):
        if random.random() <= self.CHANCE_OF_ACTING:
            self._current_packet = self._create_packet()
            return True
        else: 
            return False
    
    def _create_packet(self):
        length = random.randint(5,20)
        packet = [' ']*length
        for i in range(length):
            packet[i] = chr(random.randint(ord('A'), ord('z')))
        return ''.join(packet)
    
    def get_packet(self):
        return self._current_packet
    
    def delete_packet(self):
        self._current_packet = None


class InternetBot():
    def __init__(self):
        self._new_packet = False
        self._Alice = None
    
    def check_for_packet(self):
        if self._Alice.get_packet() is not None:
            return True
        else:
            return False
        
    def read_packet(self):
        if self._new_packet:
            return self._Alice.get_packet()
        else:
            return None
        
    def delete_packet(self):
        self._Alice.delete_packet()
        
    def assign_Alice(self, alice):
        self._Alice = alice
        
        
            

class BobBot():
    def check_for_packet(self, other):
        if other.check_for_packet():
            return True
        else:
            return False
        
    def delete_packet(self, other):
        other.delete_packet()


#Simulator for this process
Alice = AliceBot()
Inter = InternetBot()
Inter.assign_Alice(Alice)
Bob = BobBot()

for i in range(50):
    print(f'Time is {i}')
    if Alice.act(): print('Created the packet', Alice.get_packet())    
    if Bob.check_for_packet(Inter): 
        print('Bob detected the packet')
        Bob.delete_packet(Inter)


# P-2.38
"""
Write a Python program that simulates a system that supports the functions of an e-book reader.
You should include methods for users of your system to "buy" new books, view their list of purchased books, and read their puchased books.
Your system should use actual books, which have expired copyrights and are available on the Internet, 
to populate you set of available books for users of your system to "purchase" and read.
"""
import random
from pathlib import Path
from IPython.display import clear_output

"""
Areas for improvement:
- Page select
- Improve the flow between the book class and the main program


"""


class EbookReader():
    class Book():
        MIN_PRICE = 2
        MAX_PRICE = 20
        LINES_PER_PAGE = 15
        def __init__(self, filepath):
            self._name = str(filepath.name).replace('.txt', '')
            self._filepath = filepath
            self._price = random.random()*(self.MAX_PRICE-self.MIN_PRICE) + self.MIN_PRICE
            self._purchased = False
            self._current_position = 0
            self._iostream = open(self._filepath, encoding = 'latin-1')
            self._length = self.determine_length()
            
        def __repr__(self):
            return(f'Book: {self._name}, Price: {self._price}, Purchased: {self._purchased}')
        
        def purchase_book(self):
            self._purchased = True
            
        def open_book(self):
            if self._purchased:
                return open(self._filepath)
            else:
                print('Please purchase this book first!')
                return None
            
        def seek_path(self, page=0):
            self._iostream.seek(0)
            num_lines = page*self.LINES_PER_PAGE
            for _ in range(num_lines):
                self._iostream.readline()
            
        def read_book(self, page = None):
            if not self._purchased:
                print('Please purchase this book first!')
                return False
            else:
                start = self._current_position if page is None else page
                print(start)
                fp = self._iostream
                self.seek_path(start)
                for _ in range(self.LINES_PER_PAGE):
                    print(fp.readline())
                
                self._current_position = start + 1
                return True
            
        def __len__(self):
            return self._length
        
        
        def __getitem__(self, value):
            #Choose this order to shortcircuit in the event that it is not an int
            if isinstance(value, int) and value < len(self) and value>0:
                self.read_book(value)
            else:
                print('Invalid input')
                
        def determine_length(self):
            self._iostream.seek(0)
            lines = self._iostream.readlines()
            return len(lines)
        
            
            
    def __init__(self, book_dir = 'SampleFiles/Chapter 2 Books'):
        self._book_dir = Path(book_dir)
        self._library = self._build_book_dictionary()
        self._balance = 0
        self._currentbook = None
        self._statusmessage = 'Nothing to report...'
        
        
    def load_money(self, value):
        try:
            self._balance += float(value)
            return True
        except Exception as e:
            self.out(f'Invalid input: {e}')
            return False
        
        
    def out(self, message):
        self._statusmessage = message
        
    def purchase_book(self, bookname):
        if bookname in self._library:
            book = self._library[bookname]
            if book._purchased:
                self.out('You have already purchased this book')
                return False
            elif self._balance >= book._price: 
                book.purchase_book()
                self._balance -= book._price
                return True
            else:
                self.out('You have insufficient funds for that purchase')
                return False
            
        else:
            self.out('Book not in library')
            return False
        
    def read_book(self, bookname, page = None):
        #Need to add more error handling here...
        if bookname in self._library:
            self._library[bookname].read_book(page = page)
            self._currentbook = self._library[bookname]
            return True
        else:
            self.out('Book not found')
            return False
        
        
    def _read_page(self, book, page = None):
        book.read_book(page = page)
        return True

    
        
    def _build_book_dictionary(self):
        #create a list of all the books
        booklist = {str(x.name).replace('.txt', ''):self.Book(x) for x in self._book_dir.iterdir() if str(x).endswith('.txt')}
        return booklist
        
    def _print_catalog(self):
        print("The following books are available for purchase:")
        for book in self._library.values():
            if not book._purchased: print(book)
                
    def _print_owned(self):
        print('You have purchased the following books:')
        for book in self._library.values():
            if book._purchased: print(book)
               
    def _print_balance(self):
        print('\nYour current balance is: ', self._balance)
    
    def __repr__(self):
        #clear_output()
        print('Current message is:', self._statusmessage, '\n')
        self._print_owned()
        print('')
        self._print_catalog()
        self._print_balance()
        
        print('Your current book is:', self._currentbook)
        return('')  #Note: a call to print expects a returned string
    
    def console(self):
        clear_output()
        self._read_page(self._currentbook)
        
        print(self)
        print('Commands are: Purchase, Open, Next (for the next page)')
        input_results = self.get_input()
        return input_results
        
    
    
    def get_input(self):
        input_string = input()
        
        if input_string == 'exit':
            return False
        
        elif input_string.lower() == 'purchase':
            input_purchase = input('Which book would you like to purchase')
            self.purchase_book(input_purchase)
            return True #purchase a new book if you can
            
        
        elif input_string == 'next':
            #self.current_book
            return True #read the next page of the book
        
        
        elif input_string == 'open':
            input_book = input('Which book would you like to open')
            
            self._currentbook = input_book
            #open a new book (position of the old one is still saved)
            return True
            
        else:
            self.out('Invalid input')
            return True
    
            
            
eb1 = EbookReader()       
eb1.load_money(1000)
eb1.purchase_book('Alice in Wonderland')
eb1.purchase_book('Frankenstein')
print(eb1)

eb1.read_book('Alice in Wonderland')
for _ in range(10):
    eb1.read_book('Alice in Wonderland')
    
eb1.read_book ('Alice in Wonderland', 500)
eb1._library['Alice in Wonderland'][20]
eb1._library['Alice in Wonderland']['ollo']












# the last one
"""
Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area() and perimeter(). 
Implement classes Triangle, Quadrilateral, Pentagon, Hexagon,and Octagon that extend this base class, with the obvious meanings for the area() and perimeter() methods. 
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle,and Square, that have the appropriate inheritance relationships. 
Finally, write a simple program that allows users to create polygons of the various types and input their geometric dimensions, and the program then outputs their area and perimeter. 
For extra effort, allow users to input polygons by specifying their vertex coordinates and be able to test if two such polygons are similar.
"""
from abc import abstractmethod, ABCMeta
import math

class Polygon(metaclass = ABCMeta):
    def __init__(self, side_lengths = [1,1,1], num_sides = 3):
        self._side_lengths = side_lengths
        self._num_sizes = 3
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def __repr__(self):
        return (str(self._side_lengths))
    
    
    
class Triangle(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 3)
        self._perimeter = self.perimeter()
        self._area = self.area()
        
    
    def perimeter(self):
        return(sum(self._side_lengths))
        
    def area(self):
        s = self._perimeter/2
        product = s
        for i in self._side_lengths:
            product*=(s-i)
        return product**0.5
    
    
class EquilateralTriangle(Triangle):
    def __init__(self, length):
        super().__init__([length]*3)
        
        
t1 = Triangle([1,2,2])
print(t1.perimeter(), t1.area())


t2 = EquilateralTriangle(3)
print(t2.perimeter(), t2.area())
print(t2)