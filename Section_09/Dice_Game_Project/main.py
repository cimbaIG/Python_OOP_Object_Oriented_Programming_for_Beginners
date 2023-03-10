import random


class Die:
    
    # We do not want to have value as an argument of __init__ function
    # as it is better option not to give user a possibility to define
    # a value of a value attribute. This is the reason why is better
    # to only define value attribute default value inside the __init__
    # method.
    def __init__(self):
        self._value = None
    
    # We defined only a getter because we do not need a setter.
    # We only want to get a value (but only inside the class, which is
    # a reason why we defined value attribute as non-public) and we do
    # not want to change attribute value outside the class.     
    @property
    def value(self):
        return self._value
    
    # Assign random int value to a non-public value attribute.
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:
    
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    # Getter for die attribute
    @property
    def die(self):
        return self._die
    
    # Getter for is_computer attribute
    @property
    def is_computer(self):
        return self._is_computer
    
    # We provide only a getter (without a setter) as we do not want
    # to alter the counter value outside the class. We want to do 
    # that only inside the class and this is a reason why we set
    # counter attribute as non-public.
    @property
    def counter(self):
        return self._counter
    
    # Increment counter attribute by 1
    def increment_counter(self):
        self._counter += 1
        
    # Decrement counter attribute by 1
    def decrement_counter(self):
        self._counter -= 1
    
    # Aggregation in action
    # First get a die instance by calling self._die and after that
    # call the roll() method defined inside a Die() class.
    def roll_die(self):
        return self._die.roll()
