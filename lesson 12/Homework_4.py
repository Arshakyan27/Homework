# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.
index = 0
def find_index_of_item_in_listt(list_1,item):
        for x in range(len(list_1)):
            if list_1[x] == item:
                return x
        return -1
print(find_index_of_item_in_listt([1,2,3,45,6,87,8],2))
        
            
