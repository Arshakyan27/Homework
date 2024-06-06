# Write a Python program to find if a given string starts with a given
# character using Lambda.
given = "n"
bar = "narek"
result = bool(filter(lambda x : x[0] == given,bar))
print(result)
