# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.

fib = [0,1]
n = 10
y = 2
while y < n:
    next_num = int(fib[-1] + fib[-2])
    fib.append(next_num)
    
    y += 1
print(fib)
    
