# 12. List Exercise:
# Write a function that returns the nth largest element from a list
def get_nth_highest(lis,n):
    if n > len(lis) or n <= 0:
        return False
    
    for i in range(n):
        max_num = max(lis)
        lis.remove(max_num)
    return max_num
        
print(get_nth_highest([1,23,4,5,6],3))