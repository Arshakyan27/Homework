# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# character frequency to another text file (output.txt).
def character_counnt(inputed,outputed):
    with open(inputed, 'r') as file:
        text = file.read()

    result = {"New_lines": 1 }
    new = "\n"
    
    for x in text: 
        if x in result:
            result[x] += 1
        elif x == new:
             result["New_lines"] += 1  
       
        else:
            result[x] = 1
    with open(outputed,"w") as file:
        for k,v in result.items():
            file.write(f"{k}:{v}\n")
inputed = "input.txt"
outputed = "output.txt"   
character_counnt(inputed,outputed)
        