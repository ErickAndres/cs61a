#def count_change(amount):
 #   """Return the number of ways to make change for amount.

#    >>> count_change(7)
#    6
#    >>> count_change(10)
#    14
#    >>> count_change(20)
#    60
#    >>> count_change(100)
#    9828
#   """
#    def make_change(n, m):
#        if n == 1 or n == 0:
#            return 0
#        elif m >= n:
#            return 0
#        else:
#            with_m = make_change(n - m, m)
#            without_m = make_change(n - m, m * 2)
#           return with_m + without_m
#    return make_change(amount, 1)


#CS70 questions
#>>> n = pos(-1)
 #   >>> forall([-1, 1], n)
  #  False
   # >>> forall([4, 1, -2], n)
    #False
  #  >>> forall([6, 90, 8], n)
  #  True

#helper for this problem
def pos(x):
    return x > 0
def forall(lst, pred):
    """forall should return True if all elements in the list satisfy the predicate and False otherwise.
    >>> forall([-1, 1], pos)
    False
    >>> forall([4, 1, -2], pos)
    False
    >>> forall([6, 90, 8], pos)
    True
    """
    for el in lst: 
         if not pred(el): 
             return False
    return True



            #while el < lst - 1:

def exist(lst, pred):
    """exist return True if there exists an element in the list that satisfies the predicate and False otherwise

    >>> exist([-1, 1], pos)
    True
    >>> exist([4, 1, -2], pos)
    True
    >>> exist([-6, -90, -8], pos)
    False
    """
    for el in lst:
        if pred(el):
            return True
    return False

def forall2(lst, pred):
    """forall should return True if all elements in the list satisfy the predicate and False otherwise.
    >>> forall2([-1, 1], pos)
    False
    >>> forall2([4, 1, -2], pos)
    False
    >>> forall2([6, 90, 8], pos)
    True
    """
    return not exist(lst, -pred)    

def exist2(lst, pred):
    """exist return True if there exists an element in the list that satisfies the predicate and False otherwise

    >>> exist2([-1, 1], pos)
    True
    >>> exist2([4, 1, -2], pos)
    True
    >>> exist2([-6, -90, -8], pos)
    False
    """
    return not forall(lst, -pred)  










