from collections import defaultdict

dict_data = defaultdict(list)
data = [(0, 1), (1, 2), (2, 3)]

for a, b in data:
    dict_data[a].append(b)

print(dict_data)


