# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def get_the_factorial(num):
    x = 1
    factorial = 1
    while x <= num:
        factorial *= x
        x += 1
    return factorial
y = get_the_factorial(0)
print(0)
        