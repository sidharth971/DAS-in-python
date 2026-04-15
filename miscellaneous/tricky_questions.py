class A:
    items = []

    def add(self, value):
        self.items.append(value)

a1 = A()
a2 = A()

a1.add(1)
a2.add(2)

print(a1.items)
print(a2.items)

# -----------------------------------------------------------------------------
class A:
    def __eq__(self, other):
        return True

a = A()
print(hash(a))
# -------------------------------------
def func():
    try:
        return 1
    finally:
        return 2

print(func())
# -------------------------------------------------------------
def gen():
    yield 1
    return 2

g = gen()
print(next(g))
print(next(g))
# ---------------------------------------------------------------------
try:
    1 / 0
except Exception as e:
    print(e)

print(e)
# ---------------------------------------------------------------------
t = ([1, 2], 3)

try:
    t[0] += [4]
except Exception as e:
    print("Error:", e)

print(t)
# --------------------------------------------------------------------------
a = 1000
b = 1000

print(a is b)
# --------------------------------------------------------------------
class A:
    def __init__(self, items=[]):
        self.items = items

a = A()
b = A()

a.items.append(1)

print(b.items)
# ---------------------------------------------------------------------
d = {"a": 1, "b": 2}

for k in d:
    d[k + "x"] = d.pop(k)

print(d)
# ----------------------------------------------------------------------
str1 = 'SidharthSahoo'
Output = 'Sidharth Sahoo'
# ----------------------------------------------------------------------------
from collections import ChainMap

a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}

data = ChainMap(a, b)
print(data)
print(data['b'])
print(data['c'])
print(data.maps)
for k, v in data.items():
    print(k, v)

print(data.parents)
# -----------------------------------------------------------------------------------
dict1 = {'a': 1, 'b': {'x': 10, 'y': 20},'c': {'x': 4}}
dict2 = {'b': {'y': 30, 'z': 40}, 'c': {'x': 20, 'y': 10}}

# Output: {'a': 1, 'b': {'x': 10, 'y': 50, 'z': 40}, 'c': {'x': 24, 'y': 10}}

def sum_dict(dict1, dict2):
    res = {}
    for k, v in dict1.items():
        if k in dict2:
            sub_sum = {}
            for i, j in v.items():
                if i in dict2[k]:
                    sub_sum[i] = dict2[k][i] + j
                else:
                    sub_sum[i] = j

            for x, y in dict2[k].items():
                if x not in sub_sum:
                    sub_sum[x] = y

            res[k] = sub_sum

        else:
            res[k] = v

    return res


print(sum_dict(dict1, dict2))
# ---------------------------------------------------------------------------------------
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# [['Harry', 37.21], ['Berry', 37.21]]
def sec_low(arr):
    low = sc_low = max(students, key=lambda x: x[-1])[-1]

    for name, val in arr:
        if val < low:
            sc_low = low
            low = val
        elif low < val < sc_low:
            sc_low = val

    return list(filter(lambda x: x[-1] == sc_low, students))


print(sec_low(students))
# -------------------------------------------------------------------------------------------------