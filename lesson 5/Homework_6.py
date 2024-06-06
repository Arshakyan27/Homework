#Turn every item of a list into its square
first = [1,2,3,4,5,6]
square = []
for x in first:
    if x not in square:
        square.append(x**2)
print(square)
