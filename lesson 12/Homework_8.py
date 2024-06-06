# Write a function that takes a dictionary with information about students. Return info
# about the youngest student
def average_of_list(list_1):
    sum = 0
    for x in list_1:
        sum += x
    result = sum / len(list_1)
    return result
    

def highest_average_score(student_1,student_2,student_3):
    stu_1 = average_of_list(student_1["scores"])
    stu_2 = average_of_list(student_2["scores"])
    stu_3 = average_of_list(student_3["scores"])
    max = student_1["scores"]
    if stu_1 >= stu_2 and stu_1 >= stu_3:
        return student_1
    elif stu_2 >= stu_1 and stu_2 >= stu_3:
        return student_2
    else:
        return student_3
y = highest_average_score({"scores":[4,15,6],"Name":"Sahak"},{"scores":[1,2,3],"Name":"Armen"},{"scores":[4,7,8],"Name":"karen"})
print(y)