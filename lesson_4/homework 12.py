#12.Line Segment Intersection
#You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
#line segments on a line. Find the length of their intersection. Note that the
#order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
#and [2;1] are considered the same.





a_1 = float(input("please enter your number - "))
a_2 = float(input("please enter your number - "))
b_1 = float(input("please enter your number - "))
b_2 = float(input("please enter your number - "))
 
first = float(max(a_1,a_2))
second = float(min(b_1,b_2))
if first > second:
    print("The interception equals - ",first - second)
elif second > first:
    print("0")
