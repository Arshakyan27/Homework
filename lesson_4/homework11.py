#Given a real number, round it to the nearest whole.
 
num = (str(input("please enter a float number - ")))
if 0 < float(num) < 10:
    if int(num[2]) >= 5:
        print("your number was rounded to - ",int(num[0]) + 1)
    else: print(int(num[0]))
if 9 < float(num) < 100:
    if int(num[3]) >= 5:
        print(int(num[0:2]) + 1)
    else:    
        print(int(num[:1]))   
if 99 < float(num) <1000:
    if int(num[4]) >= 5:
        print(int(num[0:3]) + 1)
    else: print(int(num[:3]))
#else: 
