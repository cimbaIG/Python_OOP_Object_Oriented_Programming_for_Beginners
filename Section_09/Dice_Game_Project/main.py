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
    
    
# Testing the class Die()
die = Die()    
print(die.value)

die.roll()
print(die.value)