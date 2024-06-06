# 14. Strings Exercise:
# Write a function that capitalizes the first letter of each word in a sentence.

def capitalize(sent):
    cap_sent = ''
    for word in sent.split():
        cap_word = word.capitalize()
        cap_sent += ' '
        cap_sent += cap_word
    return cap_sent
print(capitalize('ba akam asc sn o'))