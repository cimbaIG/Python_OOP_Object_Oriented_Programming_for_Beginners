# In the first function, you can create a clone of the data list.
# In the second function, instead of using the .pop() method that mutates the 
# list, you can index the original list and use the value without modifying
# the list.

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c

def remove_elem(data, target):
    new_data = data[:]

    for item in data:
        if item == target:
            new_data.remove(target)

    return new_data

def get_product(data):
    total = 1

    for i in range(len(data)):

        total *= data[i]
    
    return total

remove_elem(c, 3)
print(get_product(b))
print(a)