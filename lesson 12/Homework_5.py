# Write a function that calculates the sum of squares of numbers from 1 to n.
def squares_to_n(n):
    x = 0
    sum = 0
    while x <= n:
        sum += x**2
        x+=1
   
    return sum
print(squares_to_n(3))