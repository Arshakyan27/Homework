# List Element Removal
# Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range.
def remove_from_list(l_1,elem):
    if elem <= len(l_1):
        del l_1[elem]
        return l_1
    else:
        raise Exception("There is no index equal to this number: ")
print(remove_from_list([1,2,3,4,5],6)) 
