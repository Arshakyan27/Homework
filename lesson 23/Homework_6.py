# Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.


dict_1 = {'bar':5,'sar': 4, '_tun':2}
dict_2 = {'shun':1,'guyn':77,'_jur':1111}
dict_3 = {x: v for d in (dict_1,dict_2) for x,v in d.items() if x[0] != '_'}
print(dict_3)



# for x in (dict_1,dict_2):
#     lis.append(x)
# print(lis)