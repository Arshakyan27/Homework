# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

def get_cubes(N):
    empty = {}
    num = 1
    
    
    while num <= N:
        empty[num] = num ** 3
        num += 1
    return empty
    
print(get_cubes(7))
        