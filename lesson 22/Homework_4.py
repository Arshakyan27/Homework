# 4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)
def get_common_elements(l_1,l_2):
    s_1 = set(l_1)
    s_2 = set(l_2)
    return list(s_2 & s_1)

print(get_common_elements([1,2,3,4],[1,2,3]))