# Write a Python program to add two given lists using map and
# lambda

first = lambda x,y: x + y
res = list(map(first,[1,3,4],[4,5,6]))
print(res)