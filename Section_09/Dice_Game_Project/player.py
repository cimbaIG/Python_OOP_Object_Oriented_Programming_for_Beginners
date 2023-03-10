class Player:
    
    def __init__(self, dice, is_computer=False):
        self._dice = dice
        self._is_computer = is_computer
        self._counter = 10

    # Getter for dice attribute
    @property
    def dice(self):
        return self._dice
    
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
    # First get a dice instance by calling self._dice and after that
    # call the roll() method defined inside a dice() class.
    def roll_dice(self):
        return self._dice.roll()
