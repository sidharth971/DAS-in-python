class A:
    @staticmethod
    def m1():
        print('This is static class')
class B(A):
    @staticmethod
    def m1():
        print('ssss')
        super(B,B).m1()
# a=B()
# a.m1()

class A:
    def connect(self):
        print('Hello')
class B(A):
    def connect(self):
        print('Hiiiiiiiiiii')
        super().connect()
# a=B()
# a.connect()

class Connect:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def class_method(cls,name):
        cls.name = name
    @staticmethod
    def static_method():
        age=20

class Disconnect(Connect):
    def __init__(self, name, title):
        super().__init__()
        self.title=title
        super().class_method(name)
        super().static_method()
        print(super().a)
    def display(self):
        print('The name is: ', Disconnect.name)
        print('The title is: ', self.title)

# a=Disconnect('sanjay','sahoo')
# a.display()

charac='python_laptop'
spl_chr=charac.split('_')
# print(spl_chr)
emp_lis=[]
for x in spl_chr:
    emp_lis.append(x[::-1])
    output=' '.join(emp_lis)
# print(output)

# def fibo():
#     x,y=0,1
#     while True:
#         yield x
#         x,y = y, x+y
# for x in fibo():
#     if x <100:
#         # print(x)
#         pass

# my_list=[10,20,30,40,50]
# iter_obj = iter(my_list)
# while True:
#     try:
#         print(next(iter_obj))
#     except StopIteration:
#         break

def show(a,b):
    while a<=b:
        yield a
        a+=1
# s=show(1,5)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

list1=[10,20,30,40,50,60,70]
index_num = list1.index(30)
# print(index_num)

spl_chr='s2d3f5g2'
emp_str = ''
for x in spl_chr:
    if x.isalpha():
        chr = x
    else:
        num = int(x)
        output = chr*num
        emp_str +=output
# print(emp_str)

char_str='python_laptop'
spl_chr = char_str.split('_')
# print(spl_chr)
length_chr = len(spl_chr)
# print(length_chr-1)
emp_lis = []
for i in range(len(spl_chr)-1,-1,-1):
    emp_lis.append(spl_chr[i])
# print(emp_lis)

s='sanjaykumar'
spl_chr = s.split()
emp_chr = ''
for x in range(len(s)-1,-1,-1):
    emp_chr = emp_chr+s[x]
# print(emp_chr)

str1 = 'san kum sah kus ctc ods'
str_spl = str1.split()
i=0
emp_lis = []
for i in range(len(str_spl)-1):
    if i%2==0:
        emp_lis.append(str_spl[i])
    
# print(emp_lis)

duplicate_chr='aaaaaasssssffffgggg'
emp_lis = []
for x in duplicate_chr:
    if x not in emp_lis:
        emp_lis.append(x)
# print(''.join(emp_lis))

dic={'a':100,'b':200,'c':400,'d':900}
dic['e'] = 700
# print(dic)
# print(dic.get('k',1000))
# print(dic)

dic['a'] = dic.get('a',3999)+30
# print(dic)
for k,v in dic.items():
    # print(k,v)
    pass

a=[10,20,30,40,50]
b=[10,20,30,40,50]
# print(a is b)
c=a
# print(c is b)
# print(a==c)

a=10
b=20
c=30

max_num = a if a>b and a>c else b if b>c else c
# print(max_num)

list1=[10,20,30,40,50,60,70,80]
list2=[29,39,94,59,69,79,89,34]

lambda_list = list(map(lambda x: x*2,list1))
# print(lambda_list)

add_from_both = list(map(lambda x,y:x+y, list1,list2))
# print(add_from_both)

from functools import reduce
lambda_reduce = reduce(lambda x,y:x*y, list2)
# print(lambda_reduce)

lambda_filter = filter(lambda x: x>30 , list1)
# print(list(lambda_filter))

def reverse_str(str1):
    list_char= ''
    for x in str1:
        list_char = x + list_char
    return list_char
str1='sanjaykumar'
# print(reverse_str(str1))

str_input='one two three four five six'
num_spl = str_input.split()
emp_lis = []
for x in range(len(num_spl)):
    if x %2!=0:
        emp_lis.append(num_spl[x][::-1])
# print(emp_lis)

str1='sanjaoiaaiiy'
vowels=['a','e','i','o','u']
emp_lis = []
for ch in vowels:
    if ch in str1:
        emp_lis.append(ch)
# print(emp_lis)

dict_man = {x:x*2 for x in range(10)}
# print(dict_man)

def factorial(n):
    if n==0:
        return 1
    else:
        result = n*factorial(n-1)
    return result
# print(factorial(5))

list1=[10,20,30,40,50,60]
list_insert = list1.insert(len(list1)//2, 201)
# print(list1)

a={'m':2,'q':5,'w':8,'d':3}
sorted_dict_item = dict(sorted(a.items(),reverse=False))
# print(sorted_dict_item)

sorted_key = {k:v for k, v in sorted(a.items(), reverse=False) }
# print(sorted_key)

square_num = [x**2 for x in range(1,10)]
# print(square_num)

even_num = [x for x in range(10) if x%2==0]
# print(even_num)

# Shallow Copy And Deep Copy
import copy
lst1 = [1, 2, [3, 4]]
# lst2=lst1
# print(lst1,lst2)
# lst2[1]=12
# print(lst2,lst1)

lst2=lst1.copy()
# lst2[1]=100
# print(lst2,lst1)
lst2[2][1]=100
# print(lst1, lst2)

# print(lst1, lst2)
lst2 = copy.deepcopy(lst1)
lst2[2][1]=100
# lst1.append([2,2,3,4])
# print(lst1, lst2)

# Pickling And Unpickling
import pickle
data = {"name": "John", "age": 30, "skills": ["python", "django"]}
with open('data.pkl','wb') as file :
    pickle.dump(data, file)

# Unpickling
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
# print(loaded_data)

# MRO : When we have a complicated Inheritance structure MRO is a rule that says which method 
# will execute after which one.
#if you want to see MRO of a class , classname.mro()

class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        print('B')
        super().show()
class C(A):
    def show(self):
        print('C')
        super().show()
class D(B,C):
    pass

obj = D()
# obj.show()

# print(D.mro())

a=3 #has some memory location
a=4 # it delete previous a=3 memory location
# This above mechanism is called reference counting garbage collector

a={}
b={}
a['ref']= b
b['ref'] = a
# so for delete this type of garbage collector we use generational garbage collector
import gc
gc.collect() # use for delete manual garbage(This is bascially used files, sockect and db connection.)
# these file , socket are not automatically removed . We have to use manually

# first-class function
# when a funtion assign to variable 
# When it call as a parameter
# Example:
def square(num):
    return num*num
def display(func, value):
    return func(value)
# print(display(square,5))

# next is return a funtion from another function 
# example
def outer():
    def inner():
        return "Inside inner function"
    return inner

obj = outer() # returns inner function
print(obj())  # calling returned function

# Encapsulation
# Encapsulation is the process of wrapping data (variables)and methods 
# into a single unit (class) and protecting them from direct access.
#Example:
class Example:
    def __init__(self):
        self._age=20
# obj = Example()
# print(obj._age)

class Example:
    def __init__(self):
        self.__age=20
obj = Example()
# print(obj._Example__age)

class Bank:
    def __init__(self):
        self.__balance=1000

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount > 0 :
            self.__balance = amount
        else:
            print('Invalid entry')
B=Bank()
# print(B.get_balance())
B.set_balance(8000)
print(B.get_balance())

# Store one record at a time
num = [a for a in range(1000000)] # it store the record one at time
# print(num)

# Generator Improve performance
def read_file():
    with open('file.txt') as f:
        for line in f:
            yield line

# Values are produced only when needed(Lazy Evaluation)
gen = (x*x for x in range(10))
# print(next(gen))
# print(next(gen))

def infinite_num():
    n=1
    while True:
        yield a
        n+=1
# print(next(infinite_num()))

def square():
    for i in range(10):
        return i*i
obj= square()
# print(obj)

num=[2,3,1]
# num.sort() #it modified original list
# print(num)

sorted_list = sorted(num)
# print(sorted_list) # it not modified original list
# print(num)

dict_ex = {"a":1, "b":2, "c":3}
dict_ex['a']=10
dict_ex['d']=30
# print(dict_ex)
dict_ex['dance']=dict_ex.pop('d')
# print(dict_ex)

# from django.utils.deprecation import MiddlewareMixin
# class custom_middlewear(MiddlewareMixin):
#     def first_middlewear_request(self, request):
#         print('Middlewear First')
    
#     def second_middlewear_response(self, request, response):
#         print('Middlewear second')
#         return response
    
#another way
class SimpleMiddleWear:
    def __init__(self, get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        print('Before view')
        response = self.get_response(request)
        return response
    
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return 0

class Rectangular(Shape):
    def __init__(self):
        self.height=7
        self.width = 8
    def calculate_area(self):
        return self.height*self.width

R=Rectangular()
# print(R.calculate_area())
# r=Shape()


# Example of @property decorator and Setter method
class Display:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"
    

    def explain(self):
        return f"the employee is {self.fname} {self.lname}"
    
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self, string):
        print('setting now.....')
        name = string.split('@')[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]

obj=Display('Sanjay','sahoo')
print(obj.email)

obj.fname='suju'
print(obj.email)
obj.email='sahoo.sanj@gmail.com'
print(obj.fname)

# Property:
# A Python feature that lets methods behave like attributes.
# Helps implement encapsulation.
# Avoids changing code using dot notation.

# Getter:
# A method used to retrieve the value of a private variable.
# Allows read-only or controlled access.

# Setter:
# A method used to modify a private variable with validation.
# Ensures data integrity.

def extra_num(num):
    def outer(func):
        def inner(a,b):
            result = func(a,b)
            return num+result
        return inner
    return outer

@extra_num(10)
def add_num(a,b):
    return a+b
# print(add_num(10,20))

list_compre = [x*2 for x in range(12)]
# print(list_compre)

gen_compre = (x*2 for x in range(10))
print(gen_compre)
for x in gen_compre:
    # print(x)
    pass

import sys
lst = [i for i in range(1000000)]
gen = (i for i in range(1000000))

# print(sys.getsizeof(lst))  # big memory
# print(sys.getsizeof(gen))  # very small memory

def fibo():
    a,b=0,1
    for _ in range(10):
        yield a*a
        a,b = b, a+b
for i in fibo():
    # print(i)
    pass

def add_num(*nums):
    result = sum(nums)
    return result
# print(add_num(2,3,4,5))


# select MAX(salary) as second_highest_salary
# from emp where salary < (select MAX(salary) from emp);

# select salary, name
# from emp 
# order by salary DESC
# LIMIT 1 OFFSET 1

str1 = "my name is avinash and i m from kerala"
# output :1
# my name is
# name is avinash
# is avinash and
# avinash and i
# and i m
# i m from
# m from kerala
spl_str = str1.split()
# print(spl_str)
step =3
for ex in range(len(spl_str)-2):
    # print(spl_str[ex:ex+3])
    pass

list_val = [0, 45, 45, 32, 21, 29]

for x in range(len(list_val)-1):
    for y in range(x, len(list_val)-1):
        if list_val[x] > list_val[y+1]:
            list_val[x],list_val[y+1]=list_val[y+1],list_val[x]
# print(list_val)
        

list_val = [0, 45, 45, 32, 21, 29]
for ex in range(len(list_val)-1):
    for every in range(len(list_val)-1):
        if list_val[every] < list_val[every + 1]:
            list_val[every], list_val[every+1]=list_val[every+1], list_val[every]
# print(list_val)

# check anagram
def check_anagram(chr, chr2):
    if sorted(chr)==sorted(chr2):
        return "its a anagram"
    else:
        return False
# print(check_anagram('sanjay','sanju'))

from collections import Counter, defaultdict
def check_anagram_counter(word1, word2):
    word1 = word1.replace(' ','').lower()
    word2 = word2.replace(' ','').lower()

    if Counter(word1)==Counter(word2):
        return "Its a Anagram"
    else:
        return False

# print(check_anagram_counter('snaay','ynaas'))



Output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

from collections import defaultdict

def group_anagrams(words):
    my_dict = defaultdict(list)
    for word in words:
        word_tuple = tuple(sorted(word))
        my_dict[word_tuple].append(word)
    return list(my_dict.values())

# Test
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(input_list))


def group_anagrams_out_defaultdict(words):
    groups = {}
    for word in words:
        my_tuple = tuple(sorted(word))
        if my_tuple not in groups:
            groups[my_tuple]=[]
        
        groups[my_tuple].append(word)
    return list(groups.values())
# print(group_anagrams_out_defaultdict(input_list))

data_list = [(1, 2), (3, 4), (5, 6)]
output = [1, 3, 5]

# print([x[0] for x in data_list])

students = [("ram", 21), ("shyam", 22), ("hari", 20)]
# print([x[1] for x in students])

data = [(1, 'a'), (2, 'b'), (3, 'c')]
output = [1, 2, 3], ['a', 'b', 'c']

list1 = []
list2 = []
for x in data:
    list1.append(x[0])
    list2.append(x[1])
# print(list1, list2)

items = [("apple", 5), ("banana", 12), ("mango", 8), ("grapes", 15)]
[("banana", 12), ("grapes", 15)]

list_data = [x[1] for x in items if x[1] > 10]
# print(list_data)

emp_lis = []
for x in items:
    if x[1]>10:
        emp_lis.append(x)
# print(emp_lis)

list1 = []
pairs = [(1, 2), (3, 4), (5, 6)]
for x in pairs:
    list1.append(x[0])
    list1.append(x[1])
# print(list1)

students = [("ram", 55), ("shyam", 89), ("hari", 40)]
["hari", "ram", "shyam"]


emp_dict = {}
for x in students:
    emp_dict[x[0]]=x[1]
# print(sorted(emp_dict))

employees = [(1, "Amit", 20000), (2, "Rita", 50000), (3, "Kabir", 30000)]
(2, "Rita", 50000)

sorted_salary = sorted(employees, key=lambda x:x[2])
# print(sorted_salary[2])

data = [(1, 2), (2, 3), (1, 2), (4, 5)]

list_chr = []
for x in data:
    if x not in list_chr:
        list_chr.append(x)
# print(list_chr)

points = [(10, 20), (30, 40), (50, 60)]

list1 = []
list2 = []
for x in points:
    list1.append(x[0])
    list2.append(x[1])
# print('x = ',list1)
# print('y = ', list2)

Input: 5
# Output: 1 2 3 4 5

def count_num(n):
    if n==0:
        return False
    count_num(n-1)
    print(n)

# print(count_num(5))

Input: 5
Output: 120

def find_facto(n):
    if n==0:
        return 1
    else:
        result = n*find_facto(n-1)
    return result
# print(find_facto(5))

Input: 1234
Output: 10
def find_sum(n):
    if n==0:
        return 0
    return (n%10) + find_sum(n//10)
# print(find_sum(1234))
# print(1234// 10)
num_count = 1234
   
# Input: "hello"
# Output: "olleh"

def reverse_chr(input):
    result = reverse_chr(input[::-1])
    return result
# print(reverse_chr("hello"))

input1 = [1, [2, 3], [4, [5, 6]]]
# output = count(input1) = 6

my_str = str(input1).replace('[','').replace(']','')
# print(my_str)

# print(len(my_str.split(',')))

def check_count(data):
    count = 0
    letters = list(data)
    while letters:
        list_val = letters.pop()
        if isinstance(list_val, list):
            letters.extend(list_val)
        else:
            count+=1
    return count
# print(check_count(input1))

raw_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []
for list_data in raw_list:
    flat_list.append(list_data[0])
    flat_list.append(list_data[1])
# print(flat_list)

access_element = [[10, 20], [30, 40], [50, 60]]

list_data = []
for list1 in access_element:
    list_data.append(list1[1])
# print(list_data)

my_list = [1, [2, [3, 4], 5], 6]
output =[1, 2, 3, 4, 5, 6]
result = []
def flat_list(data):
    stack=list(data)
    while stack:
        item = stack.pop()
        print(item)
        if isinstance(item, list):
            stack.extend(item)
        else:
            result.append(item)
    return sum(result)
# print(flat_list(my_list))

list1 = [1, [2, "x"], ["y", 3], 4]
output = [1, 2, 3, 4]

def findout_num(data):
    stack=list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            if isinstance(item, int):
                result.append(item)
    return sorted(result)
# print(findout_num(list1))

input1 = [1, [2, [3, [4]]]]

def findout_num(data):
    count = 1
    stack=list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
            count+=1
        else:
            pass
    return count
# print(findout_num(input1))

list1 = ["a", ["b", "c"], [["d"]]]
output = "abcd"

def findout_num(data):
    result = ''
    stack=list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            result = item+result
    return result
# print(findout_num(list1))

input1 = [1, 2, [3, 4], [5, [6, 7, 8]]]
output = [2, 4, 6, 8]

def findout_even(data):
    result = []
    stack = list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            if item%2==0:
                result.append(item)
    return sorted(result)
# print(findout_even(input1))

input = [2, [3, [4]]]
output = 24

def data_product(data):
    result = []
    mul=1
    stack = list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            mul= mul*item
            # result.append(result_mul*mul)
    return mul
# print(data_product(input))

my_list = [1, [2, [3, 4]]]
output = [1, [4, [9, 16]]]

def data_square(data):
    result=[]
    for x in data:
        if isinstance(x, list):
            result.append(data_square(x))
        else:
            result.append(x*x)
    return result
# print(data_square(my_list))

list_data = [ ["a", 1], ["b", [2, 3]], ["c", 4] ]
{
  "a": 1,
  "b": [2, 3],
  "c": 4
}

my_dict = {}
for item_val in list_data:
    my_dict[item_val[0]] = item_val[1]
# print(my_dict)

input_list = [1, "a", [2, "b"], ["c", [3, "d"]]]
output = ["a", "b", "c", "d"]

def extract_str(data):
    result = []
    stack = list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            if isinstance(item, str):
                result.append(item)
    return sorted(result)
print(extract_str(input_list))

list2 = [1, [2, 3], [4, [5, 6]]]
count_want = 3

def count_list(data):
    result = []
    count = 0
    stack = list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
            count+=1

    return count
# print(count_list(list2))

list_input = [1, [2, [3]]]
output = [(1,1), (2,2), (3,3)]

def make_tuple(data):
    result_data = []
    for item in data:
        if isinstance(item, list):
            result_data.extend(make_tuple(item))
        else:
            result_data.append((item,item))
    return result_data
print("tuple is ", make_tuple(list_input))

# select emp_name, dept_name
# from Employees e INNER JOIN Departments d
# ON e.dept_id=d.dept_id;

# Q2. Display all employees and their department name
# select e.emp_name, d.dept_name
# from Employees e LEFT JOIN Departments d
# ON e.dept_id = d.dept_id;

# Q3. Display all departments and employees working in them.
# select e.emp_name, d.dept_name
# from departments d RIGHT JOIN Employess e
# ON d.dept_id=e.dept_id

# Q4. List employees who do not belong to any department.
# select e.emp_name
# from Departments d RIGHT JOIN Employess e
# ON d.dept_id=e.dept_id
# where e.emp_name= NULL


input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

from collections import defaultdict
def find_anagram_word(data):
    group = {}
    for item in data:
        dict_item = tuple(sorted(item))
        # print(dict_item)
        if dict_item not in group:
            group[dict_item]=[]
        group[dict_item].append(item)
    return group.values()

print(find_anagram_word(input_data))

# my_dict = {'name': 'satya', 'age': 28, 'friends':{'joy'}}
# for x in my_dict:
#     if my_dict.values()=={'joy'}:
#         print(x)


lst =[1,2,3,[4,5,6,[7,8]],9]
# op = lst = [1,2,3,4,5,6,[7,8],9]

stack = []
count =0
for item in lst:
    if isinstance(item, list):
        stack.extend(item)
        print("what is the stack", stack)
    else:
        stack.append(item)
print(stack)

class InvalidAgeError(Exception):
    def __init__(self, message='Age is not valid'):
        self.message = message
        super().__init__(self.message)

try:
    raise InvalidAgeError('Age should be integer')
except InvalidAgeError as error:
    print(error)

# Execution time calculator
# Write a decorator to measure how long a function takes to run.

import time

def outer(func):
    def inner(a,b):
        start_time = time.time()
        # time.sleep(5)
        result = func(a,b)
        end_time = time.time()
        time_consumed = end_time - start_time
        return result, time_consumed
    return inner
@outer
def add(a,b):
    return a+b
# print(add(5,6)) 


# Count how many times a function is called
# Create a decorator that counts the number of times a function is executed.
def counter(func):
    count = 0 
    def inner(*args, **kwargs):
        nonlocal count
        count+1
        print(f"Function '{func.__name__}' called {count} times")
        return func(*args, **kwargs)
    return inner

@counter
def greet():
    print('hello')

# print(greet())

a = [1,'a','b',3,4,True]
output = [1,3,4]

list_val = [x for x in a if type(x) is int]
# print(list_val)

arr = [10, 5, 8, 20, 3]

largest = float("-inf")
second = float("-inf")
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest>num>second:
        second = num
# print(second)

empt_list = []
for r in range(len(arr)-1, -1, -1):
    empt_list.append(arr[r])
# print(empt_list)
from datetime import datetime
def outer(func):
    def inner(*args, **kwargs):
        work_time = datetime.datetime.now().hour
        if 9<=work_time<=18:
            return func(*args, **kwargs)
        else:
            print("Function cannot run outside working hours (9AM–6PM).")
    return inner

@outer
def display():
    print('Hello')

arr = [10, 4, 20, 15, 8]
def find_kth_largest(arr, k):
    n = len(arr)
    for x in range(k):
        for i in range(0, n - x - 1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr[n-k]
# print(find_kth_largest(arr,2))

# select max(salary) from emp 
# where salary < (select max(salry) from emp);

# select DISTINCT salary 
# from emp 
# order by salary DESC
# LIMIT1 OFFSET 1

# select e.emp_name as Employee, m.emp_name as Manager
# from employee e
# SELF JOIN employee m
# ON e.manager_id = m.empt_id


numbers = [1,2,3,4]
target = 3

result = []

for x in range(len(numbers)):
    for y in range(x+1, len(numbers)):
        if numbers[x]+numbers[y]==target:
            result.append((numbers[x], numbers[y]))
# print(result)

# Q.Write a query to fetch employees with salary > average salary.
# SELECT EMP_NAME, SALARY
# FROM EMPLOYEE
# WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE);

# What is SELF JOIN? Give an example.
# SELECT e.emp_id,e.emp_name, m.emp_name as manager
# from emp e LEFT JOIN emp m
# ON e.emp_id=m.manager_ID;

#Sub Query Example
# SELECT Emp_name FROM Emp
# Where dept_id IN (SELECT dept_id from department where location ='PUNE')

# Find complete duplicate rows
# SELECT *, count(*) FROM emp
# Group By emp_id, salary, email
# HAVING Count(*)>1;

# SELECT emp_name, count(*)
# from emp
# Group By emp_name
# HAVING count(*) >1;

#Delete All duplicate rows from a Table
# DELETE FROM Emp
# Where Emp_id IN(
#     SELCT Emp_id FROM (
#         SELECT Empd_id, ROW_NUM() OVER(
#             PARTITION BY emp_id, dept_id, salary
#             ORDER BY emp_id
#         )as rn
#         FROM Emp
#     ) x
#     WHERE rn > 1
# );

# Write a query to find employees who joined in the last 30 days.
# SELECT emp_id, emp_name, join_date
# FROM emp
# WHERE join_date >= CURDATE() - INTERVAL 30 DAY;

# Find highest-paid employee in each department
# SELECT emp_name, emp_id, salary,dept_id,  ROW_NUMBER() OVER(
#     PARTITION BY dept_id ORDER BY salary DESC) as rn
# FROM Emp;

# Example: Running sales total per month
# SELECT month, sales, SUM(sales) OVER (
#     ORDER BY month
# ) as total
# FROM Sales;

# Top 2 employees in each department:
# SELECT * FROM (
#     SELECT emp_id, dept_id, emp_name, salary, ROW_NUMBER() OVER(
#         PARTITION BY dept_id ORDER BY salary DESC) As rn
#     ) FROM Employee
# ) x 
# WHERE rn<=2:

# Total salary per department
# SELECT Dept_id, SUM(Salary) as total_salary
# From EMP
# GROUP BY Dept_ID;    

# Count employees in each department
# SELECT Dept_id , COUNT(*) as emp_count
# from Employee
# GROUP BY Dept_id;

# Average salary per department
# SELECT Dept_id, AVG(Salary)
# from emp
# GROUP BY Dept_id;

# Minimum & maximum salary per department
# SELECT Dept_id, MAX(Salary) as max_salary,
# MIN(Salary) as min_salary
# from emp 
# GROUP BY Dept_id;

# Count employees by department + by salary
# SELECT Dept_id, salary, COUNT(*)
# FROM Emp
# GROUP BY Dept_id, salary;

ar=[10,23,45,63,12,1]
def selection_sort(ar):
    n=len(ar)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if ar[j] > ar[min_index]:
                min_index=j
        ar[i], ar[min_index] = ar[min_index], ar[i]
    return ar
# print(selection_sort(ar))

s = 'ch,od@i!'

def reverse_alpha(str1):
    letters = []
    for ch in str1:
        if ch.isalpha():
            letters.append(ch)

    letters.reverse()
    letter_index = 0   # this will pick letters from the reversed list

    result = ''
    for x in str1:
        if x.isalpha():
            result += letters[letter_index] # take next reversed letter
            letter_index+=1
        else:
            result+=x # keep special characters as they are
    return result

s = 'san,ja@!y'
# print(reverse_alpha(s))

from functools import reduce
numbers = [2,3,4,5,6]
mul_num = reduce(lambda x,y: x*y, numbers)
# print(mul_num)


def trailing_zero_number(n):
    fact = n

    while n>1:
        fact *= n-1
        n-=1

    result = 0
    for i in str(fact)[::-1]:
        if i =='0':
            result+=1
        else:
            break
    return result
# print("trailing zero count ",trailing_zero_number(5))

def add_unlimit_number(*args, default=10):
    total_num = 0
    for x in args:
        total_num+=x
    result = total_num+default
    return result
# print(add_unlimit_number(1,2,3,4,5))

l1 = [1,2,3,4,5]
output_list= []
output = ["odd", "even", "odd" ,"even", "odd"]

find_evn_odd = ["even" if x %2==0 else "odd" for x in l1]
# print(find_evn_odd)

lst = [1,2,3]
append_num = [lst.append(x) for x in range(3)]
# print(lst)

lis = [1, 3, 4, 10, 4]

import itertools, functools
from itertools import accumulate
from functools import reduce
print(list(accumulate(lis,lambda x, y: x+y)))

# print(functools.reduce(lambda x, y: x+y, lis))

def convert_upper(func):
    def inner(*args):
        result = func(*args).upper()
        return result
    return inner

@convert_upper
def upper_func(name):
    return name
# print(upper_func('sanjay'))

x=10
f = lambda x,y=5:x+y
# print(f(x)(y))

num = [1,2,3,4]
square_num = list(map(lambda x: x*x, num))
# print(square_num)

find_even = list(filter(lambda x:x%2==0,num))
# print(find_even)

# sort_tuple = sorted(num, key=lambda x:x[1])
# print(sort_tuple)

add_num = reduce(lambda x,y:x+y, num)
# print(add_num)

x=10
y=20
outer = lambda x: (lambda y:x+y)
# print(outer(x)(y))

my_dict = {'a':1,'c':5,'b':3}
sorted_val = sorted(my_dict.items() , key=lambda x:x[1])
# print(sorted_val)

strs = ["flower", "flow", "flight"]

def find_prefix(strs):
    prefix = strs[0]
    while not prefix.startswith(strs[1:]):
        prefix = prefix[:-1]

    return prefix
# print(find_prefix(strs))

dict_prac = {"a":10, "b":20, "c":30}
# print(dict_prac.get('b'))
# if dict_prac.get('d') is not None:
#     print('Key Exist')
# else:
#     print('No key')

# if 'd' in dict_prac.keys():
#     print('Key Exist')
# else:
#     print('Not Exist')

dict_prac['d']=40
# print(dict_prac)
dict_prac.update({'b':50})
# print(dict_prac)
# item = dict_prac.pop('c')
# print(item)
# item = dict_prac.popitem()
# print(item)

# del dict_prac
# print(dict_prac)
# for x in dict_prac.values():
#     print(x)
# for x, y in dict_prac.items():
#     print(x, ':',y)
dict_prac = {"a":10, "b":20, "c":30}
new_dict = {'Name':123, 'Value':456, 'Sales':789}
# print({**new_dict,**dict_prac})
merge_dict = new_dict.copy()
merge_dict.update(dict_prac)
# print(merge_dict)

merge_item = dict_prac | new_dict
# print(merge_item)

dict_comp = {x:x*2 for x in range(10)}
# print(dict_comp)
find_value = {k:v for k,v in dict_prac.items() if v>20}
# print(find_value)

sort_dict = list(sorted(new_dict.items(), key=lambda x:x[0]))
# print(sort_dict)
value_default = dict_prac.setdefault('b')
# print(value_default)

words = ["apple", "ant", "banana", "ball"]
group_dict = {}

for x in words:
    group_dict.setdefault(x[0], []).append(x)
# print(group_dict)

company = {
    "employee": {
        "details": {
            "name": "Ravi",
            "age": 28
        }
    }
}

deep_values = company['employee']['details']['age']
# print(deep_values)
values_dict = company.get('employee', {}).get('details').get('age')
# print(values_dict)

def reverse_int(input):
    input = abs(input)
    str_num = ''
    for x in str(input):
        str_num=x+str_num
    return str_num
# print(reverse_int(1234))

def find_longest_palindrome(words):
    longest = ''
    for word in words:
        if word == word[::-1]:
            if len(word)>len(longest):
                longest=word
    return longest if longest else None
# Example
words_list = ["madam", "racecar", "apple", "noon", "level", "rotor"]

result = find_longest_palindrome(words_list)
# print("Longest palindrome:", result)

def find_common_prefix(words):
    prefix = words[0]
    for word in words:
        while not word.startswith(prefix):
            prefix=prefix[:-1]
            if prefix=='':
                return ''
    return prefix
# print(find_common_prefix(["flower", "flow", "flight"]))

num_list = [10,29,23,70,50]
find_square = list(map(lambda x : x*x, num_list))
# print(find_square)

for i in range(len(num_list)):
    min_index = i
    for j  in range(i+1, len(num_list)):
        if num_list[j]<num_list[min_index]:
            min_index = j
    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
# print(num_list)


def find_first_index_of_vowel(word):
    vowels = 'aeiou'
    for index, char in enumerate(word):
        if char in vowels:
            return index
    return -1


s = {10, 20, 30}
# s=[10,20,30]
# s={'a':10, 'b':20, 'c':30}
x = s.pop()
# print('remove element', x)     # 10 or 20 or 30 (random)
# print(s) 

# select salary
# FROM (
#     Select salary, DENSE_RANK() OVER(ORDER BY Salary DESC) as rnk
#     FROM Employees
# ) as temporary_result
# where rnk =2;

# select e.ename, e.salary, e.dept_id
# from employee e
# where e.salary > (select AVG(salary) from employee where dept_id=e.dept_id);

# select emp_id, ename, dept_id, salary
# from (select *, avg(salary) over(order by dept_id) as dept_avg_salary from employee) t
# where salary > dept_avg_salary;

# findout the how many times vowel presents in given string
random_string = 'sanjaoiaaiiy'
vowels=['a','e','i','o','u']
emp_dic = {}
for vowel in random_string:
    if vowel in vowels:
        emp_dic[vowel] = emp_dic.get(vowel,0)+1
# print(emp_dic.items())

for k,v in emp_dic.items():
    # print(f'{k} occurs {v} times')
    pass

def fac_num(n):
    if n==1:
        return 1
    else:
        result = n*fac_num(n-1)
    return result
# print(fac_num(5))

# def fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b = b, a+b
# for x in fibo():
#     pass
    # if x <100:
        # print(x)
        

def find_fibo(n):
    emp_list = []
    first_num, second_num = 0, 1

    for _ in range(n):
        emp_list.append(first_num)
        new_term = first_num + second_num
        first_num = second_num
        second_num = new_term
    print(emp_list)

    return emp_list

# print("find fibo", find_fibo(10))

def find_missing_number(arr):
    len_arr = len(arr)+1
    find_nth_sum = len_arr*(len_arr+1)//2
    total_sum = sum(arr)
    return find_nth_sum-total_sum
# print(find_missing_number([1, 2, 4, 6, 3, 7, 8]))

test_dict = {'gfg' : [5, 6, 7, 8],
              'is' : [10, 11, 7, 5],
              'best' : [6, 12, 10, 8],
              'for' : [1, 2, 5]}

emp_list = []
for val in test_dict.values():
    for actual_val in val:
        emp_list.append(actual_val)
# print(sorted(emp_list))

name_str = 'sanjay kumar sahoo'
spl_name = name_str.split()
print(spl_name)
emp_str = ''

for word in spl_name:
    rev_word = ''
    for ch in word:
        rev_word = ch+rev_word
    emp_str =' '+rev_word+emp_str
    
# print(emp_str.strip())

length_char = len(arr)
def fifo(arr):
    stack_list = []
    for num_length in range(length_char-1):
        stack_list.append(arr[len(arr)//2:])
    print("stack list", stack_list)

f=fifo('{ [ < >] }')


# what is difference between multithreading and multiprocessing
# Memory management in python
# Types of inheritance
# What is MRO
# What is difference between HAVING And WHERE Clause In SQL
# What is the Protected and private variable
# Types of Code used in API(EX:500, 401, 404)
# What is Polymorphism
# What is 
# Find Third Highest Salary Using Window Function
# What are the window function you have used ?
# What is encapsulation?
# What is Authentication and Authorization In django

# SELECT emp_id, salary, SUM(salary) OVER(Partition By emp_id) as Running Total
# FROM Employees;

# Find employees with salary greater than the average salary of their department.

# SELECT Dept_id, salary
# FROM (Select Dept_id,Salary, AVG(salary) OVER(Partition BY Dept_id ORDER BY Salary) as avg_salary
# FROM employees ) t
# Where salary > avg_salary;

# Query to find employees whose salary is in the top 10%.

# SELECT * FROM (Select *, PERCENT_RANK() OVER(Order By Salary DESC) as pct_rank 
# FROM Employees) t
# where pct_rank <= 0.10;

class FindEven:
    def __init__(self,limit):
        self.limit=limit
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        val = self.current
        self.current+=2
        return val
for num in FindEven(10):
    # print(num)
    pass

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper


def incre_num(count):
    if count==4:
        return
    incre_num(count+1)
    print(count)

def add(*args):
    print(args)
    return max(args)

# print(add(1, 2, 3, 4))

# Find the first non-repeating character in a string.
def find_1st_unique_char(word):
    dict_data = {}
    for ch in word:
        dict_data[ch] = dict_data.get(ch,0)+1
    
    for ch in word:
        if dict_data[ch] ==1:
            return ch
# print(find_1st_unique_char('swiss'))

# Find highest salary employee in each department
# select * from (select * , DENSE_RANK() OVER(Partition By Dept Order By Salary DESC)as rn
#     From Employee) t 
# where rn=1;

# Running Total using Window Function
# SELECT order_date, amount, SUM(amount)
# OVER(Partition By Order_date) as running_total
# from order;

lst = [(1,"one"), (2,"two"), (3,"three"), (3,"iii"), (3,"III")]
# output {1:"one",2:"two",3:["three","iii","III"]}


