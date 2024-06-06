# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt).
def replace_word(inputed, w_1, w_2, outputed):
    with open(inputed, "r") as file:
        text = file.read()
    modified_text = text.replace(w_1, w_2)
    with open(outputed, "w") as file:
        file.write(modified_text)

inputed = "input.txt"
outputed = "output.txt"
replace_word(inputed, "Python", "C++", outputed)