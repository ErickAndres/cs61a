# Name:Erick Andres
# Email:eandres1@berkeley.edu

# Q1.
def g(n):
    """Return the value of G(n), computed recursively.
	find 5 quotes and analyze them
    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return (g(n - 1)) + (2 * g(n - 2)) + (3 * g(n - 3)) 

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n
    k = 3
    previous, predecessor, current = 1, 2, 3
    while  n > k:
        previous, predecessor, current = predecessor, current, 3 * previous + 2 * predecessor + current
        k = k + 1
    return current
	
# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10) #or has_seven(k % 10)
# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(100)
    2
    """
    def helper(k, v, flag):
        if k == n:
            return v
        elif has_seven(k) or k % 7 == 0:
            if flag == True:
                return helper(k + 1, v - 1, not flag)
            return helper(k + 1, v + 1, not flag)
        else:
            if flag == True:
                return helper(k + 1,v + 1, flag)
            return helper(k + 1, v - 1, flag)
    return helper(1, 1, True)

# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    #return ways(n // 10, n % 10) + ten_pairs(n // 10)
	
    def ways(other, last_digit):
        if other == 0:
            return 0
        elif (other % 10 + last_digit % 10 == 10):
            return 1 + ways(other // 10, last_digit % 10)
        return ways(other // 10, last_digit % 10)  
    return ways(n // 10, n % 10) + ten_pairs(n // 10)
# Q5.
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def make_change(n, m):
        if n == 1 or n == 0:
            return 1
        elif m >= n:
            return 0
        else:
            without_m = make_change(n - m, m)
            with_m = make_change(n - m, m * 2)
            return with_m + without_m
    return make_change(amount, 1)