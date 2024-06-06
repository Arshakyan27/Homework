# Write a function that prints all prime numbers up to a given limit
def primes_to_n(n):
    result = []
    x = 0
    while x <= n:
        prime = True
        for i in range(2,int(x/2)):
            if x % i == 0:
                prime = False
        
    if prime:
        result.append(x)
    x += 1
    
print(primes_to_n(15))
