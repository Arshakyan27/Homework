# Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.
y = 'bar  bar hah'
di = {x: y.count(x) for x in y}

print(di)