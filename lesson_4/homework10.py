#Given the salaries of three employees working at a department, find the
#amount of money by which the salary of the highest-paid employee differs
#from the salary of the lowest-paid employee. The input consists of three
#positive integers - the salaries of the employees. Output a single number,
#the difference between the top and the bottom salaries


a = int(input("Enter salary of first employee - "))
b = int(input("Enter salary of second employee - "))
c = int(input("Enter salary of third employee - "))
g = c - a
h = b - a
j = b - c
k = a - c
l = c -b
m = a - b
if a < b < c:
    print(g)
if a < c < b: 
    print(h)  
if c < a < b:
    print(j)
if c < b < a:
    print(k)
if b < a < c:
    print(l)
if b < c < a:
    print(m)
    
