# Write a Python program to check whether a given string is number or
# not using Lambda
given_string = "5"
result = lambda x: x.isdigit()

last_Result = bool(result(given_string))
print(last_Result)
