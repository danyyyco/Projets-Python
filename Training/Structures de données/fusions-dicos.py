dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = dict1 | dict2
print(result)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = {k: v for d in (dict1, dict2) for k, v in d.items()}
print(result)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = {**dict1, **dict2}
print(result)