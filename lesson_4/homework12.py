#12.Line Segment Intersection
#You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
#line segments on a line. Find the length of their intersection. Note that the
#order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
#and [2;1] are considered the same.


a_1 = input("please enter the first point of first line - ")
a_2 = input("please enter the second point of first line - ")
b_1 = input("please enter the first point of second line - ")
b_2 = input("please enter the second point of second line - ")
#c_1 = float(a_2)- float(a_1)
#len_1 = abs(c_1)
#c_2 = float(b_2) - float(b_1)
#len_2 = abs(c_2)
if float(a_2) > float(a_1):
    print
result_1 = abs(float(b_1) - float(a_2))
print("The intersection equals - ",result_1)