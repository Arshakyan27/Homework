# 13. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements)

def if_are_disjoint(s_1,s_2):
    if len(set(s_1) & set(s_2)) == 0:
        return False
    return True
print(if_are_disjoint((1,2,3,4),(4,5,6,7,8)))