# Q3.
ssh star.cs.berkeley.edu -l cs61a-xb
encapsolation-data abstraction and creating classes and permission restrictions, inheritance, polymorphisism(common interfaces for different objects to communicate with each other)
def make_instance(some_class):
    """Return a new object instance of some_class."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = some_class['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    """Return value or a bound method if value is callable."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

def make_class(attributes, base_classes=()):
    """Return a new class with attributes.

    attributes -- class attributes
    base_classes -- a sequence of classes
    """
    "*** YOUR CODE HERE ***"

def init_instance(some_class, *args):
    """Return a new instance of some_class, initialized with args."""
    instance = make_instance(some_class)
    init = some_class['get']('__init__')
    if init:
        init(instance, *args)
    return instance

# AsSeenOnTVAccount example from lecture.

def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""

    interest = 0.02

    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')

    return make_class(locals())

Account = make_account_class()

def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee.

    >>> checking = CheckingAccount['new']('Jack')
    >>> checking['get']('interest')
    0.01
    >>> checking['get']('deposit')(20)
    20
    >>> checking['get']('withdraw')(5)
    14
    """
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)

    return make_class(locals(), [Account])

CheckingAccount = make_checking_account_class()

def make_savings_account_class():
    """Return the SavingsAccount class, which imposes a $2 deposit fee.

    >>> savings = SavingsAccount['new']('Jack')
    >>> savings['get']('interest')
    0.02
    >>> savings['get']('deposit')(20)
    18
    >>> savings['get']('withdraw')(5)
    13
    """
    deposit_fee = 2

    def deposit(self, amount):
        fee = self['get']('deposit_fee')
        return Account['get']('deposit')(self, amount - fee)

    return make_class(locals(), [Account])

SavingsAccount = make_savings_account_class()

def make_as_seen_on_tv_account_class():
    """Return an account with lots of fees and a free dollar.

    >>> such_a_deal = AsSeenOnTVAccount['new']('Jack')
    >>> such_a_deal['get']('balance')
    1
    >>> such_a_deal['get']('interest')
    0.01
    >>> such_a_deal['get']('deposit')(20)
    19
    >>> such_a_deal['get']('withdraw')(5)
    13
    """
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 1)

    return make_class(locals(), [CheckingAccount, SavingsAccount])

AsSeenOnTVAccount = make_as_seen_on_tv_account_class()