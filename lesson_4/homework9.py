#You are given four real numbers - the coordinates of two points on a
#plane. The first two numbers are the x and y coordinates of the first point,
#and the last two numbers are the x and y coordinates of the second point.
#O"utput the length of the line segment bounded by the two points.

a_1 = float(input("please enter first x - "))
b_1 = float(input("please enter first y - "))
a_2 = float(input("please enter second x - "))
b_2 = float(input("please enter second y - "))
x = (float(b_1) - float(b_2))**2
y = (float(a_1 - float(a_2)))**2
c = (x + y)**0.5
print(c)