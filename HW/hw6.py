# Name:Erick Andres
# Email:eandres1@berkeley.edu

# Q1.

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, value):
        self.balance = 0
        self.stock = 0
        self.product = product
        self.value = value
    def vend(self):
        if self.stock == 0: 
            return 'Machine is out of stock.'
        elif self.value > self.balance:
            return 'You must deposit $' + str(self.value - self.balance) + ' more.'
        elif self.value < self.balance:
            change = self.balance - self.value
            self.stock -= 1
            self.balance = 0
            return 'Here is your ' + str(self.product) + ' and $' + str(change) + ' change.'
        else:
            self.stock -= 1
            self.balance = 0
            return 'Here is your ' + str(self.product) + '.'
    def restock(self, amount):
        self.stock += amount
        return 'Current ' + str(self.product) + ' stock: ' + str(self.stock)
    def deposit(self, money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(money) + '.'
        else:
            self.balance += money
            return 'Current balance: $' + str(self.balance)

# Q2.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    def __init__(self, obj):
        self.inside_object = obj
        self.methods = dir(obj)
        
    def ask(self, *args):
        if 'please' not in args[0]:
            return 'You must learn to say please first.'
        else:
            rest_of = args[0].replace('please ', '')
            if rest_of in self.methods: #rest_of is a string, self.methods is a list
                if len(args) == 1:
                    return getattr(self.inside_object, rest_of)()
                method_call = 'self.inside_object.' + rest_of + '('
                for index in range(1, len(args)): 
                    if len(args) - 1 == index:
                        method_call = method_call + str(args[index]) + ')'
                    else:
                        method_call = method_call + str(args[index]) + ','     
                return eval(method_call)
            else:
                return 'Thanks for asking, but I know not how to ' + rest_of
           







