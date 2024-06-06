# 6. Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# # the student with the highest score

def highest_score(Students):
    highest = Students[0][1]
    high_stu = Students[0][0]
    
    for k,v in Students:
        if v > highest:
            highest = v
            high_stu = k
    return high_stu,highest
print(highest_score((('vahe',12),('sahak',20),('partev',77))))        
        