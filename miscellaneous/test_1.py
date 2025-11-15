from functools import reduce

students = [
    {"name": "A", "mark": 80},
    {"name": "B", "mark": 90},
    {"name": "C", "mark": 70},
]

print(min(students, key=lambda x: x["mark"]))
print(max(students, key=lambda x: x["mark"]))

print(reduce(lambda x, y: x + y['mark'], students, 0))

print(sorted(students, key=lambda x: x['mark'], reverse=True))