
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student


    # if student_1["age"] <= student_2["age"] and student_1["age"] <= student_3["age"]:
    #     return student_1
    # elif student_2["age"] <= student_1["age"] and student_2["age"] <= student_3["age"]:
    #     return student_2
    # else:
    #     return student_3

def find_the_youngest(students):

    max = students["student_1"]["age"]
    for  k,v in students.items():
        if v["age"] > max:
            max = v["age"]
    return max
students = {"student_1" : {"age": 12,"name":"sahak"
                     },
       "student_2" : {"age": 24,"name":"armen"
                         },
       "student_3" :{"age": 62,"name":"gurgen"}}
print(find_the_youngest(students))


