# # Write a Python program to find intersection of two given arrays using
# # Lambda.

list_1 = [1,2,3,4,5,6,7,8]
list_2 = [1,2,3,4,5]
res = lambda x,y: x in y
result = list(filter(lambda l_1,l_2: list(filter(lambda x,y: in l_1,l_2)),[list_1,list_2])[0])
print(res)