# Write a function that calculates the average of a list of numbers.

def average_of_list(list_1):
    sum = 0
    for x in list_1:
        sum += x
    result = sum / len(list_1)
    return result
    
print(average_of_list([1,2,3,4,5]))