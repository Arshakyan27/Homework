# Arrange string characters such that lowercase letters should come first
word = "BjIshK"
poqr = ""
mec = ""

for x in word:
    
    if x.islower():
        poqr += x
    if x.isupper():
        mec += x
res = poqr + mec
print(res)