def is_sen_a_pangram(sentence:str):
    result = set()
    for x in sentence:
        if x.isalpha():
            result.add(x)
    return len(result) == 26
print(is_sen_a_pangram("qwertyuiopasdfghjklzxcvbnm"))