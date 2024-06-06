# 15. Multiple Exceptions:
# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not
def error_handling(lst,index):
    try:
        return lst[index]
    except:
        raise IndexError('Incorrect Index')
    finally:
        print("Task Completed")
        
print(error_handling([1,2,3,4],1))