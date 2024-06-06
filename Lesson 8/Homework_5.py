# You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all
# three.
# The set of elements that are unique to each list (present in only one list).
first = ["barev", "andzrev","arev"]
second = ["barev","sexan","ator"]
third = ["barev","dexin","karmir","andzrev"]
fir = set(first)
sec = set(second)
th = set(third)

# first 
res1 = fir & sec & th
if res1:
     print("first",res1)
else:print("There are not common words in lists")



# third
res7 = fir - sec - th 
res8 = sec - fir - th
res9 =  th - fir - sec
print("third", res7,res8,res9)
