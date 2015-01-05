# Name:Erick Andres
# Email:eandres1@berkeley.edu

    Attempts = []
    failed_attempts = 0
    def withdraw(amount, pwd):
        nonlocal failed_attempts
        if failed_attempts >= 3:
            return "Your account is locked. Attempts: " + str(Attempts)
        if pwd != new_password:
            Attempts.append(pwd)
            failed_attempts = failed_attempts + 1
            return 'Incorrect password'
        balance = balance - amount
        return balance
    return withdraw
    
    incorrect_password = []
    failed_attempts = 0
    correct_password = [] 
    
    def withdraw(amount, pwd):
        nonlocal failed_attempts
        if failed_attempts >= 3:
            return "Your account is locked. Attempts: " + str(incorrect_password)
        elif pwd == old_password:
            correct_password.append(pwd)
            return withdraw(amount, correct_password)
        elif pwd == new_password:
            correct_password.append(pwd)
            return withdraw(amount, correct_password)
        elif pwd != old_password or new_password:
            incorrect_password.append(pwd)
            failed_attempts = failed_attempts + 1
            return 'Incorrect password'
        balance = balance - amount
        return balance
    return withdraw

    def other_withdraw(amount, pwd):
        if pwd == original
    
def str_interval(x):
    """Return a string representation of interval x.
    
    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q1.
def interval(a, b):
    """Construct an interval from a to b."""
    return (a, b) 

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

# Q2.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert not(lower_bound(y) <= 0 <= upper_bound(y))
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q4.
 
def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    """
    a = lower_bound(x)
    b = upper_bound(x)
    c = lower_bound(y)
    d = upper_bound(y)
    if a > 0 and c > 0:
        return (a * c, b * d)
    elif a > 0 and d < 0:
        return (b * c, a * d)
    elif b < 0 and c > 0:
        return (a * d, b * c)
    elif b < 0 and d < 0:
        return (b * d, a * c)
    elif a < 0 < b and c > 0:
        return (a * d, b * d)
    elif a < 0 < b and d < 0:
        return (b * c, a * c)
    elif a > 0 and c < 0 < d:
        return (b * c, b * d)
    elif b < 0 and c < 0 < d:
        return (a * d, a * c)
    elif a < 0 < b and c < 0 < d:
        return (min(a * d, b * c), max(a * c, b * d))
    
# Q5.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    return (c - (c * p / 100), c + (c * p / 100))

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """ 
    return (100 * ((upper_bound(x) - lower_bound(x)) / 2) / ((upper_bound(x) + lower_bound(x)) / 2))
    
 
# Q6. 

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
# print par1(r1, r2)
# print par2(r1, r2)

# Q7.

def multiple_references_explanation():
  return """Because par2 has implemented the div_interval it keeps the error number lower than the par1 equation, which only divides once not keeping the rounding to the minimum."""

# Q8.

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def f(t):
        return a * t**2 + b * t + c
    tcrit_x = -b / (2 * a)
    tcrit_y = f(tcrit_x)
    if a < 0: 
        return interval(min(f(lower_bound(x)), f(upper_bound(x))), f(tcrit_x))    
    elif a > 0:
        return interval(f(tcrit_x), max(f(lower_bound(x)), f(upper_bound(x))))
    
# Q9.

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    s = zero
    for el in seq:
        if non_zero(el) == True:
            s = add_interval(s, square_interval(el))    
    return s
    

def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(sum(filter(map(reduce(square_interval)))))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(seq for el in range(nonzero, x) if seq != 0)

# Q10.

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3)))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"