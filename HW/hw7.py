# Name:Erick Andres
# Email:eandres1@berkeley.edu

# Q1.

class Amount(object):
    """An amount of nickels and pennies.

    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value
    22
    >>> a.nickels = 5
    >>> a.value
    32
    """
    def __init__(self, nickels, pennies):
        self.nickels = nickels
        self.pennies = pennies
    @property    
    def value(self):
        return 5*self.nickels + 1*self.pennies
            
class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than
    four pennies, by converting excess pennies to nickels.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels
    4
    >>> a.pennies
    2
    >>> a.value
    22
    """
    def __init__(self, nickels, pennies):
        Amount.__init__(self, nickels, pennies)
      
        if pennies > 4:
            conversion = pennies % 5
            add_nickels = pennies // 5
            self.nickels += add_nickels
            self.pennies = conversion

# Q2.

class Square(object):
    def __init__(self, side):
        self.side = side
    
class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
def apply(operator_name, shape):
    """Apply operator to shape.

    >>> apply('area', Square(10))
    100
    >>> apply('perimeter', Square(5))
    20
    >>> apply('area', Rect(5, 10))
    50
    >>> apply('perimeter', Rect(2, 4))
    12
    """
    def square_area(s):
        return s.side**2
    def square_perimeter(s):
        return 4*s.side
    def rectangle_area(r):
        return r.width * r.height
    def rectangle_perimeter(r):
        return 2*r.width + 2*r.height
    apply_operator = {
    ('area', Square): square_area,
    ('perimeter', Square): square_perimeter,
    ('area', Rect): rectangle_area,
    ('perimeter', Rect): rectangle_perimeter}
    
    tag = type(shape)
    key = (operator_name, tag)
    return apply_operator[key](shape)
    
# Q3.

def empty(s):
    return len(s) == 0

def set_contains2(s, v):
    """Return true if set s contains value v as an element.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> set_contains2(s, 2)
    True
    >>> set_contains2(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains2(s.rest, v)

def intersect_set2(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> t = Rlist(2, Rlist(3, Rlist(4)))
    >>> intersect_set2(s, t)
    Rlist(2, Rlist(3))
    """
    if empty(set1) or empty(set2):
        return Rlist.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Rlist(e1, intersect_set2(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set2(set1.rest, set2)
        elif e2 < e1:
            return intersect_set2(set1, set2.rest)

def adjoin_set2(s, v):
    """Return a set containing all elements of s and element v.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> adjoin_set2(s, 2.5)
    Rlist(1, Rlist(2, Rlist(2.5, Rlist(3))))
    >>> adjoin_set2(s, 0.5)
    Rlist(0.5, Rlist(1, Rlist(2, Rlist(3))))
    >>> adjoin_set2(s, 3)
    Rlist(1, Rlist(2, Rlist(3)))
    """
    "*** YOUR CODE HERE ***"
    if s is Rlist.empty:
        return Rlist(v)
    elif set_contains2(s, v):
        return s
    elif s.first > v: 
        return Rlist(v, s)
    else:
        return Rlist(s.first, adjoin_set2(s.rest, v))

def union_set2(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> t = Rlist(1, Rlist(3, Rlist(5)))
    >>> union_set2(s, t)
    Rlist(1, Rlist(2, Rlist(3, Rlist(5))))
    >>> union_set2(s.rest, t)
    Rlist(1, Rlist(2, Rlist(3, Rlist(5))))
    >>> union_set2(Rlist.empty, intersect_set2(s.rest, t))
    Rlist(3)
    """
    "*** YOUR CODE HERE ***"
    if set1 is Rlist.empty:
        return set2
    elif set2 is Rlist.empty:
        return set1
    elif set1.first == set2.first:
        return Rlist(set1.first, (union_set2(set1.rest, set2.rest)))
    elif set1.first < set2.first:
        return Rlist(set1.first, (union_set2(set1.rest, set2)))
    else:
        return Rlist(set2.first, (union_set2(set1, set2.rest)))

# Q4.

class Tree(object):
    """A tree with internal values."""

    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

def big_tree(left, right):
    """Return a tree set of unique elements between left and right.

    >>> big_tree(0, 12)
    Tree(6, Tree(2, Tree(0), Tree(4)), Tree(10, Tree(8), Tree(12)))
    """
    if left > right:
        return None
    split = left + (right - left)//2
    return Tree(split, big_tree(left, split-2), big_tree(split+2, right))

def set_contains3(s, v):
    """Return true if set s contains value v as an element.

    >>> t = Tree(2, Tree(1), Tree(3))
    >>> set_contains3(t, 3)
    True
    >>> set_contains3(t, 0)
    False
    >>> set_contains3(big_tree(20, 60), 34)
    True
    """
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains3(s.right, v)
    elif s.entry > v:
        return set_contains3(s.left, v)

def adjoin_set3(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = big_tree(0, 9)
    >>> b
    Tree(4, Tree(1), Tree(7, None, Tree(9)))
    >>> adjoin_set3(b, 5)
    Tree(4, Tree(1), Tree(7, Tree(5), Tree(9)))
    """
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry, s.left, adjoin_set3(s.right, v))
    elif s.entry > v:
        return Tree(s.entry, adjoin_set3(s.left, v), s.right)

def intersect_set3(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> s, t = big_tree(0, 12), big_tree(6, 18)
    >>> intersect_set3(s, t)
    Tree(8, Tree(6), Tree(10, None, Tree(12)))
    """
    s1, s2 = map(tree_to_ordered_sequence, (set1, set2))
    return ordered_sequence_to_tree(intersect_set2(s1, s2))

def union_set3(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> s, t = big_tree(6, 12), big_tree(10, 16)
    >>> union_set3(s, t)
    Tree(10, Tree(6, None, Tree(9)), Tree(13, Tree(11), Tree(15)))
    """
    s1, s2 = map(tree_to_ordered_sequence, (set1, set2))
    return ordered_sequence_to_tree(union_set2(s1, s2))

def tree_to_ordered_sequence(s):
    """Return an ordered sequence containing the elements of tree set s.

    >>> b = big_tree(0, 9)
    >>> tree_to_ordered_sequence(b)
    Rlist(1, Rlist(4, Rlist(7, Rlist(9))))
    """
    "*** YOUR CODE HERE ***" #Think about how to add the Rlist, 
    #using helper then produce Rlist of left side then right side
    if s is None:
        return Rlist.empty
    elif s.left is None and s.right is None:
        return Rlist(s.entry)
    else:
        left_side = tree_to_ordered_sequence(s.left)
        right_side = tree_to_ordered_sequence(s.right)
        return union_set2(adjoin_set2(left_side, s.entry), right_side)
def partial_tree(s, n):
    """Return a balanced tree of the first n elements of Rlist s, along with
    the rest of s. A tree is balanced if the length of the path to any two
    leaves are at most one apart.

    >>> s = Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
    >>> partial_tree(s, 3)
    (Tree(2, Tree(1), Tree(3)), Rlist(4, Rlist(5)))
    """
    if n == 0:
        return None, s
    #elif s == Rlist.empty:
        #return None, s
    left_size = (n-1)//2
    right_size = n - left_size - 1
    tuple_a = partial_tree(s, left_size)
    entry = tuple_a[1].first
    tuple_b = partial_tree(tuple_a[1].rest, right_size)
    return (Tree(entry, tuple_a[0], tuple_b[0]), tuple_b[1])
    

def ordered_sequence_to_tree(s):
    """Return a balanced tree containing the elements of ordered Rlist s.

    A tree is balanced if the lengths of the paths from the root to any two
    leaves are at most one apart.

    Note: this implementation is complete, but the definition of partial_tree
    above is not complete.

    >>> ordered_sequence_to_tree(Rlist(1, Rlist(2, Rlist(3))))
    Tree(2, Tree(1), Tree(3))
    >>> b = big_tree(0, 20)
    >>> elements = tree_to_ordered_sequence(b)
    >>> elements
    Rlist(1, Rlist(4, Rlist(7, Rlist(10, Rlist(13, Rlist(16, Rlist(19)))))))
    >>> ordered_sequence_to_tree(elements)
    Tree(10, Tree(4, Tree(1), Tree(7)), Tree(16, Tree(13), Tree(19)))
    """
    return partial_tree(s, len(s))[0]

# Q5.

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    def number_of_ways(level):
        if 'PP' in level:
            return 0
        elif level[0] == 'P':
            return 0
        elif level == ' ':
            return 1
        else:
            with_jump = 0
            if len(level) != 2:
                with_jump = number_of_ways(level[2:]) 
            without_jump = number_of_ways(level[1:])
            return with_jump + without_jump
    return number_of_ways(level)
        
# Q6.

def has_cycle(s):
    """Return whether Rlist s contains a cycle.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3)))
    >>> has_cycle(t)
    False
    """
    "*** YOUR CODE HERE ***"
    

def has_cycle_constant(s):
    """Return whether Rlist s contains a cycle.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

class Rlist:
    """A recursive list consisting of a first element and the rest.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest
    Rlist(2, Rlist(3))
    >>> len(s)
    3
    >>> s[1]
    2
    """

    class EmptyList:
        def __len__(self):
            return 0
        def __repr__(self):
            return "Rlist.empty"

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        assert type(rest) is Rlist or rest is Rlist.empty
        self.first = first
        self.rest = rest

    def __getitem__(self, index):
        if index == 0:
            return self.first
        else:
            return self.rest[index-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        return rlist_expression(self)

def rlist_expression(s):
        """Return a string that would evaluate to s."""
        if s.rest is Rlist.empty:
            rest = ''
        else:
            rest = ', ' + rlist_expression(s.rest)
        return 'Rlist({0}{1})'.format(s.first, rest)




