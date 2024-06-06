# Write a Python function to calculate count of each letter in string



def letter_count(string):
    counts  =  {}

    for x in string:
        if x.isalpha():
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
    return counts
y = letter_count("kaparan")
print(y)
            
    