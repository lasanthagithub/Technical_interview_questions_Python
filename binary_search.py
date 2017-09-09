"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    found = -1
    length = len(input_array)
    centre = int(length / 2)
    found = int(input_array[centre])
    
    if value <= max(input_array) or value >= min(input_array):
        while found != value:
        
            if value < found:
                centre = int(centre / 2)
                
            elif value > found:
                centre = int((length - centre) / 2)
                print(centre)    
            elif value == found:
                found = int(input_array[centre])
    else:
        found = -1
            
    
    return found

test_list = [1,3,9,11,15,19,29]
test_val1 = 125
test_val2 = 115
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))