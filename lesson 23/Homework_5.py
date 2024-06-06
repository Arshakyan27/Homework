# Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3

start = ['barev','tun','pahak','sev']
dict_1 = {x:len(x) for x in start if len(x) > 3 }
print(dict_1)