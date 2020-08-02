from Chapter7.link import LinkedQueue, LinkedDeque

class Tree:
    """Abstract base class representing a tree structure."""

    # nested Position class
    class Position:
        """An abstraction representing the location of a single element."""
        
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)
        
    # abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p 

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of leavels seqarating Position p from the root."""
        if self.is_root(p):
            return 0 
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0 
        else:
            return 1 + max(self._height(c) for c in self.children(p))
    
    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        if p is None, return the height of the entire tree."""
        if p is None:
            p = self.root()
        return self._height(p)
    
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p 
    
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                     # visit p before its subtrees
        for c in self.children(p):  # for each child c 
            for other in self._subtree_preorder(c):     # do preorder of c's subtree
                yield other 
    
    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other 
        yield p         # visit p after its subtrees
    
    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()          # known positions not yet yielded
            fringe.enqueue(self.root())     # starting with the root 
            while not fringe.is_empty():
                p = fringe.dequeue()        # remove from front of the queue
                yield p 
                for c in self.children(p):
                    fringe.enqueue(c)       # add children to back of queue

    def breadthfirst_deque(self):
        """Deque version of breathfirst method."""
        if not self.is_empty():
            fringe = LinkedDeque()
            fringe.insert_first(self.root())
            while not fringe.is_empty():
                p = fringe.insert_last()
                yield p 
                fringe.insert_last(self.children(p))

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()      # return entire preorder iteration


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # additional abstract methods
    def left(self, p):
        """
        Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child."""
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods implemented in this class
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling.)"""
        parent = self.parent(p)
        if parent is None:
            return None 
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:    # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other 
        yield p         # visits p between its subtrees
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other 
    
    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()

    def num_children(self, p):
        """Return the number of children that Position p has."""
        num = 0
        if self.left(p) is not None:
            num += 1
        if self.right(p) is not None:
            num += 1
        return num 


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:
        # Lightweight, nonpublic class for storing a node.
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element 
            self._parent = parent 
            self._left = left
            self._right = right 
        
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container 
            self._node = node 
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element 
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node 
    
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node 
    
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None 
    
    # binary tree constructor 
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None 
        self._size = 0 
    
    # public accessors 
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size 
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Return the Position of p's left chold (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """Return the Position of p's right child (or Node if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        """Return the number of chilren of Position p."""
        node = self._validate(p)
        count = 0 
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count 
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty."""
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def add_left(self, p, e):
        """
        Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right 
        if child is not None:
            child._parent = node._parent 
        if node is self._root:
            self._root = child 
        else:
            parent = node._parent 
            if node is parent._left:
                parent._left = child 
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element 
    
    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):   # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node 
            node._left = t1._root 
            t1._root = None 
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node 
            node._right = t2._root 
            t2._root = None 
            t2._size = 0
    
    def _delete_subtree(self, p):
        """Remove the entire subtree rooted at p."""
        node = self._validate(p)
        if self.is_leaf(node):
            self._size -= 1
            self._delete(node)
        else:
            self._delete_subtree(self.children(node))
        

def preorder_label(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j+1) for j in path)    # displayed labels are one-indexed
    print(2*d*' ' + label, p.element())
    path.append(0)      # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path)     # child depth is d+1
        path[-1] += 1
    path.pop()

def parenthesize(T:Tree, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False 
            parenthesize(T, c)
        print(')', end='')

# assume a `space()` method of each tree element reports the local space used at that position
def disk_space(T:Tree, p):
    """Return total disk space for subtree of T rooted at p."""
    subtotal = p.element().space()      # space used at position p
    for c in T.children(p):
        subtotal += disk_space(T, c)    # add child's space to subtotal
    return subtotal 


class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree.
    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    """
    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree
    
    def tree(self):
        """Return refference to the tree being traversed."""
        return self._tree 
    
    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])     # start the recursion
    
    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position p.

        p       Position of current node being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)     # "pre visit" p
        results = []
        path.append(0)      # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))    # recur on child's subtree
            path[-1] += 1       # increment index
        path.pop()              # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results)  # "post visit" p
        return answer
    
    def _hook_previsit(self, p, d, path):   # can be overridden
        pass 

    def _hook_postvisit(self, p, d, path, results):
        pass 


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print(2*d*' ' + str(p.element()))

#tour = PreorderPrintIndentedTour(T)
#tour.execute()

class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:       # p follows a sibling
            print(', ', end='')         # so preface with comma
        print(p.element(), end='')
        if not self.tree().is_leaf(p):  # if p has children
            print(' (', end='')
    
    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')

class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        # simply add space associated with p to that of its subtrees
        return p.element().space() + sum(results)


class BinaryEulerTour(EulerTour):
    """
    Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour of the left subtree (if any),
    yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)      # "in visit" for p
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer 
    
    def _hook_invisit(self, p, d, path):
        pass 


# assume the element type for the original tree supports setX and setY methods
class BinaryLayout(BinaryEulerTour):
    """Class for computing (x, y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0
    
    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(self._count)
        self._count += 1 


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g., '42'),
        and the expression tree will havve that value at an isolated node.

        In a three-parameter version, token should be an operator, and left and right should be existing ExpressionTree instances 
        that become the operands for the binary operator.
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)
        if self is not None:
            if token not in '+-*/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)
        
    def __str__(self):
        """Return string representation of the expression."""
        pieces = []     # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)
    
    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))     # leaf value as a string
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())          # operator
            self._parenthesize_recur(self.right(p), result)
            result.append(')')
    
    def _evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())
    
    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element)
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+': return left_val + right_val 
            elif op == '-': return left_val - right_val 
            elif op == '*': return left_val * right_val
            else: return left_val / right_val


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression."""
    S = []
    for t in tokens:
        if t in '+-*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))     # push trivial tree storing value
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()