# 3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def get_seven_multiples(l_1):
    sum = 0
    for i in l_1:
        if i % 7 == 0 :
            sum += i
    return sum
print(get_seven_multiples([7,14,21,33]))