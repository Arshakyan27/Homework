# Write a Python program to square and cube every number in a given list of
# integers using Lambda.
given = [1,2,3,45,6,47,9,85,]
result = list(map(lambda x,y:(x**2,y **3), given,given))

print(result)