# .Write a python function which create dict from 2
# lists with the same length

def dict_from_two_lists(l_1:list,l_2:list):
    empty = {}
   
    n = 1
    for i in range(len(l_1)):
        keys = keys[i]
        value = value[i]
        
        if len(l_1) == len(l_2):
            empty[keys] = value
            
    return empty
l_1 = ["Italia","Ispania","Germania"]
l_2 = ["Hrom", "Madrid","Berlin"]
print(dict_from_two_lists(l_1,l_2))
        