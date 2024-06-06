# Write a python function, which add a new value
# with given key in dict.


def add_value(string):
    orinak = {'given': 'value_1', }
    if 'given' in orinak:
        orinak['given'] = string
    return orinak
print(add_value("kapadovkia"))