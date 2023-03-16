# Explain the relationship between rich comparison methods and operator 
# overloading.
# Operator overloading occurs when an operator has different implementations 
# depending on the data type of the operands.
# This means that the same operator can have different functionality based on 
# the data type of the operands.
# Rich comparison methods are special methods that allow us to customize the 
# “behavior” of the comparison operators ( < <= > >= == !=) when these 
# operators act on instances of the class.
# This customization of the behavior is a form of operator overloading because 
# we are providing a different functionality for the same operator depending on 
# the data type of the operands.

class Bubble:
    
    def __init__(self, size):
        if size > 0 and size < 11:
            self._size = size
        else:
            print("The size of a bubble has to be integer in range 1-10!")
        
    @property
    def size(self):
        return self._size
    
    def __str__(self):
        return f"A bubble of size {self._size}."
    
    def __lt__(self, other):
        return self._size < other._size

    def __le__(self, other):
        return self._size <= other._size

    def __gt__(self, other):
        return self._size > other._size

    def __ge__(self, other):
        return self._size >= other._size

    def __eq__(self, other):
        return self._size == other._size

    def __ne__(self, other):
        return self._size != other._size


bubble1 = Bubble(size=2)
bubble2 = Bubble(size=4)
print(bubble1)
print(bubble2)

print(bubble1 == bubble2)
print(bubble1 != bubble2)
print(bubble1 >= bubble2)
print(bubble1 <= bubble2)
print(bubble1 > bubble2)
print(bubble1 < bubble2)