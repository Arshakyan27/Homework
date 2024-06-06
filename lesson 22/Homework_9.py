# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.

def max_of_dict(dict):
    max_value = float('-inf')
    max_key = ''
    for k,v in dict.items():
        if v > max_value:
            max_value = v
            max_key = k
    return max_key
y = {'tiv':12,'myus':44,'ok':99,'hike':888}
print(max_of_dict(y))