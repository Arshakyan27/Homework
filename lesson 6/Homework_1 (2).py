#count how many odd number are in list

fir = [12,3,4,5,7,9]
sec = []
for odd in fir:
    if odd % 2 != 0:
        sec.append(odd)
print(len(sec))
