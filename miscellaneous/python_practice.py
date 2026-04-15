# def check_fibonacci():
#     a=0
#     b=1
#     while True:
#         yield a
#         a,b = b,a+b
# for x in check_fibonacci():
    # if x<100:
        # print(x)
    # pass

char_str='python_laptop'
spl_chr = char_str.split('_')
# print(spl_chr)
length_chr = len(spl_chr)
# print(length_chr-1)
emp_lis = []
for i in range(len(spl_chr)-1, -1, -1):
    emp_lis.append(spl_chr[i])
# print(emp_lis)

# s='sanjaykumar'
# spl_chr = s.split()
# chr_lis = []
# for x in spl_chr:
#     chr_lis.append(x[::-1])
# print(chr_lis)
# chr = ''.join(chr_lis)
# print(chr)

# str_lets='kumarsanjay'
# spl_list = list(str_lets)
# even=[]
# odd=[]
# incre = 0
# while incre<len(spl_list):
#     print(spl_list[incre])
#     if incre%2==0:
#         even.append(spl_list[incre])
#     else:
#         odd.append(spl_list[incre])
#     incre+=1
# print(even)
# print(odd)


# str1 = 'san kum sah kus ctc ods'
# str_spl = str1.split()
# str_store = []
# i=0
# while i<len(str_spl):
#     str_store.append(str_spl[i])
#     i+=2
# print(' '.join(str_store))
# print(str_store)

str2='f2r3t1y6'
list_chr = ''
for i in str2:
    if i.isalpha():
        char_str=i
    else:
        int_chr = int(i)
        output = char_str*int_chr
        list_chr+=output
# print(list_chr)

duplicate_chr='aaaaaasssssffffgggg'
emp_str = ''
for x in duplicate_chr:
    if x not in emp_str:
        emp_str+=x
# print(emp_str)

# dic={'a':100,'b':200,'c':400,'d':900}
# dic['e']=760
# print(dic)
# print(dic.get('k',1000))
# print(dic)

# dic['a']=dic.get('a',3999)+30
# print(dic)
# for k,v in dic.items():
#     print(k,v)

# a=[10,20,30,40,50]
# b=[10,20,30,40,50]
# print(a is b)
# c=a
# print(a is c)
# print(a==c)

a=10
b=20
c=30

max_num = a if a>b and a>c else b if b>c else c
# print(max_num)

list1=[10,20,30,40,50,60,70,80]
list2=[29,39,94,59,69,79,89,34]

lambda_list = list(map(lambda x : x*10, list1))
# print(lambda_list)

mul_str = list(map(lambda x,y : x+y, list1,list2))
# print(mul_str)

lambda_filter = list(filter(lambda x : x>10,  list1))
# print(lambda_filter)

from functools import reduce
lambda_reduce = reduce(lambda x,y : x+y, list1)
# print(lambda_reduce)

def reverse_str(str1):
    list_char= ''
    for x in str1:
        list_char = x + list_char
    return list_char
str1='sanjaykumar'
print(reverse_str(str1))

# reverse all odd position string value
str_input='one two three four five six'

spl_list = str_input.split(' ')
spl_list_length = len(spl_list)
# print(spl_list)
odd_str=[]
for x in range(0,spl_list_length):
    if x % 2 != 0:
        odd_str.append(spl_list[x][::-1])
# print(odd_str)

str1='sanjaoiaaiiy'
vowels=['a','e','i','o','u']
list_vowels = {}
for x in str1:
    if x in vowels:
        list_vowels[x] = list_vowels.get(x,0)+1

# print(list_vowels)

p = {x:x*2 for x in range(0,10)}
# print(p)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

list1=[10,20,30,40,50,60]
list1.insert(len(list1)//2, 100)
# print(list1)

a={'m':2,'q':5,'w':8,'d':3}
sorted_dict_item = dict(sorted(a.items() ,reverse=False))
# print(sorted_dict_item)
sorted_key = {k:v for k,v in sorted(a.items(), reverse=False)}
# print(sorted_key)

s='lenovolaptop'
len_s = len(s)
# print(len_s)
# print(s[len_s-3])

square = [x**2 for x in range(1,10)]
# print(square)

even_num = [x for x in range(2,10) if x % 2 == 0]
# print(even_num)

from itertools import combinations
s=[1,2,3,4,5]
comb=combinations(s,2)
# print(list(comb))

list_of_num = (10,20,30,40,50)
import sys
size_of_num = sys.getsizeof(list_of_num)
# print(size_of_num)

for a in range(3):
    for b in range(a):
        # print(a,b)
        pass
dict1 = {9: [2, 11, 7, 15]}
arr1 = dict1[9]
# print(arr1)
keys= next(iter(dict1))

# for chr1 in range(len(arr1)):
#     for chr2 in (chr1+1, len(arr1)):
#         print(arr1[chr1]+arr1[chr2])
#         if arr1[chr1]+arr1[chr2] == keys:
#             print(arr1[chr1],arr1[chr2])
            # pass


a={100:'sanjay',200:'kumar',400:'sahoo',400:'Natia',500:'batia'}
for x in a.keys():
    # print(x)
    pass

dict6 = {'a': 10, 'b': 8}
dict7 = {'d': 6, 'c': 4}
dict8={'e':3,'f': 7}

def add_dict(dict1, dict2,dict3):
    dict_val = {**dict1, **dict2, **dict3}
    return dict_val
# print(add_dict(dict6,dict7,dict8))


def check_palindrome(str1):
    cleaned = str1.lower().replace(" ", "")
    emp_str = ''
    for each_chr in cleaned:
        emp_str = each_chr + emp_str
    print(emp_str)
    if emp_str==cleaned:
        return True
    else:
        return False
# print(check_palindrome('Race car'))

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 ==0 and i%5==0:
            print('FizzBuzz')
        elif i % 3 ==0:
            print('Fizz')
            continue
        elif i % 5 ==0:
            print('Buzz')
            continue
        else:
            print (i)
# print(fizzbuzz(15))

def reverse_sent(sentence):
    spl_sentence = sentence.split()
    emp_list = ''
    for sent in spl_sentence:
        emp_list = sent+' '+emp_list
    return emp_list.strip()
# print(reverse_sent('hello world'))

def count_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    emp_str = ''
    for vow in vowels:
        if vow in words:
            emp_str += vow
    return len(emp_str)
# print(count_vowels('sanjay'))

def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n*find_factorial(n-1)
# print(find_factorial(5))

def check_anagram(word1, word2):
    word1 = word1.replace(' ','')
    word2 = word2.replace(' ','')
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
# print(check_anagram("listen", "silent"))

def fibonacci(n):
    a,b=0,1
    list_fibo=[]
    for x in range(n):
        list_fibo.append(a)
        a,b = b,a+b
    return list_fibo

# print(list(fibonacci(7)))

def find_second_largest(list1):
    second=largest=0
    for num in list1:
        if num > largest:
            second=largest
            largest=num
        elif largest>num>second:
            second=num
    return second
# =============================================================================
# print(find_second_largest([10, 20, 4, 23,45,98,1012,4,5,6,45, 99]))
# =============================================================================

def fibo(num):
    a, b = 0, 1
    for _ in range(num):

        yield a
        a,b = b,a+b
# =============================================================================
# print(list(fibo(7)))
# =============================================================================


def find_missing_number(list_num):
    length_num = len(list_num)+1
    find_nth_sum = length_num*(length_num+1)//2
    sum_of_array =  sum(list_num)
    missing_num = find_nth_sum-sum_of_array
    return missing_num

# =============================================================================
# print(find_missing_number([1, 2, 4, 5, 6]))
# =============================================================================

def longest_word(word):
    spl_word = word.split()
    # longest_word = max(spl_word, key=len)
    # return longest_word

    longest=''
    for word in spl_word:
        if len(word) > len(longest):
            longest = word
    return longest

# print(longest_word("I love programming in Python"))

def pair_sum(lst, target):
    pairs = []
    for each in range(len(lst)):
        for each_chr in range(each+1, len(lst)):
            if lst[each]+lst[each_chr]==target and  (lst[each_chr], lst[each]) not in pairs:
                pairs.append((lst[each], lst[each_chr]))
    return pairs
print(pair_sum([2, 4, 3, 5, 7, 8, -1], 7))


def rotate_list(lst, index):
    n= len(lst)
    index = index % n
    return lst[-index:] + lst[:-index]
# print(rotate_list([10, 20, 30, 40, 50], 2))  # [40, 50, 10, 20, 30]


def first_non_repeating_char(str):
    emp_lis= []
    for ch in str:
        if  str.count(ch) ==1:
            return ch
    return None
# print(first_non_repeating_char("swiss"))  # "w"

from collections import Counter
def first_non_repeating_char(str):
    freq = Counter(str)
    for ch in str:
        if freq[ch] == 1:
            return ch
    return None

# print(first_non_repeating_char("swiss"))


def check_palindrome(pali_str):
    clean_str = pali_str.lower().replace(" ", "")
    print(clean_str)
    emp_lis = []
    for each_chr in range(len(clean_str)-1, -1, -1):
        emp_lis.append(clean_str[each_chr])
    val = ''.join(emp_lis)
    if val == clean_str:
        return True
    else:
        return False

print(check_palindrome("A man a plan a canal Panama"))

# [1,2,3,4] and [3,4,5,6] → [3,4].
list1 = [1,2,3,4]
list2 = [3,4,5,6]
uni_num=[]
# def unique_num(list1, list2):
#     for x in list1:
#         if x in list2:
#             uni_num.append(x)
#     return uni_num
# print(unique_num(list1, list2))

def unique_num(list1, list2):
    return list(set(list1) ^ set(list2))

# print(unique_num(list1, list2))

dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}

def merge_dict(dict1, dict2):
    merge_val = dict1|dict2
    return merge_val
# print(merge_dict(dict1, dict2))

def find_prime(n):
    emp_lis = []
    is_prime = True
    if n<=1:
        is_prime=False
    for x in range(2,n):
        if x%n==0:
            emp_lis.append(x)

# =============================================================================
#     return emp_lis
# =============================================================================
# =============================================================================
# print(find_prime(10))
# =============================================================================

def get_square(n):
    for x in range(n):
        print(x**x)

get_square(3)

def average(array):
    # your code goes here
    total = 0
    count = 0
    for x in array:
        total += x
        count += 1
    average = total / count
# =============================================================================
#     return average
# =============================================================================

# =============================================================================
# print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))
# =============================================================================

def permute(nums):
    if len(nums) == 0:
        return [[]]
    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]
        for p in permute(rest):
            result.append([nums[i]] + p)
# =============================================================================
#     return result
# =============================================================================

# =============================================================================
# print(permute([1, 2, 3]))
# =============================================================================


#permutation question
result = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            result.append((i,j,k))
# =============================================================================
# print(result)
# =============================================================================

from itertools import permutations

perm = permutations(range(3),3)
print(list(perm))

lis = [1,2,3,4,5]
lis2 = [3,4,5,6,7]
list1 = list(map(lambda x,y :x+y, lis2,lis))
# =============================================================================
# print(list1)
# =============================================================================

sum_num = reduce(lambda x,y :x+y, lis)
# =============================================================================
# print(sum_num)
# =============================================================================


arr = [2,3,4,5,6,7]
def runners_up(arr):
    largest = second = 0
    for ex in arr:
        if ex > largest:
            second=largest
            largest=ex
        elif largest>ex>second:
            second = ex
# =============================================================================
#     return second
# =============================================================================
        
# =============================================================================
# print(runners_up(arr))
# =============================================================================

# =============================================================================
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# =============================================================================


# =============================================================================
# emp_lst_name = [('Harry', 37.21), ('Berry', 37.21), ('Tina', 37.2), ('Akriti', 41.0), ('Harsh', 39.0)]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     emp_lst_name.append((name,score))
#     print(emp_lst_name)
# =============================================================================
    
# =============================================================================
# emp_lst_name = [('Harry', 37.21), ('Berry', 37.21), ('Tina', 37.2), ('Akriti', 41.0), ('Harsh', 39.0)]
# 
# emp_dict = {}
# for ch in emp_lst_name:
#     emp_dict[ch[0]]=ch[1]
# sorted_val = sorted(emp_dict.values())
# for key in emp_dict:
#     if emp_dict[key]==sorted_val[1]:
#         print(key)
# =============================================================================

# =============================================================================
# emp_dict = {}
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         emp_dict[name] =score
# print(emp_dict)
# =============================================================================
emp_dict = {'Harsh': 20.0, 'Beria': 20.0, 'Varun': 19.0, 'Kakunami': 19.0, 'Vikas': 21.0}
sorted_val = sorted(emp_dict.values())

lowest  = sorted_val[0]
for n in sorted_val:
    if n < lowest:
        lowest=n
second_lowest = None
for n in sorted_val:
    if n != lowest:
        if second_lowest is None or n < second_lowest:
            second_lowest=n

for key in emp_dict:
    if emp_dict[key]==second_lowest:
        print(key)


str_list='d2f3g4g5'

for x in str_list:
    if x.isalpha():
        char_var = x
    else:
        char_int = int(x)
        result = char_var * char_int
# =============================================================================
# print(result)
# =============================================================================

str_list='d2f3g4g5'
empt_chr = ''

for x in str_list:
    if x.isalpha():
        char_var = x
    else:
        char_int = int(x)
        result = char_var * char_int
        empt_chr += result
print(empt_chr)

list1=[10,20,30,40,50,60,70]
index_num = list1.index(50)
print(index_num)

str_one='aaassssjjjsjsjsjsnnsns'

uni_list = []
for x in str_one:
    if x not in uni_list:
        uni_list.append(x)
print(''.join(uni_list))

a=10
b=20
max_num = a if a>b else b
print(max_num)

import sys
list_of_num = (10,20,30,40,50)
size_num = sys.getsizeof(list_of_num)
print(size_num)

random_string = 'sanjaoiaaiiy'
vowels=['a','e','i','o','u']

dict_val = {}
for str1 in random_string:
    if str1 in vowels:
        dict_val[str1] = dict_val.get(str1,0)+1
print(dict_val)

output : {2: 3, 4: 6, 6: 9, 8: 12, 10: 15, 12: 18, 14: 21, 16: 24, 18: 27}

square_val = {x*2:x*3 for x in range(1,10)} 


print(square_val)

import pickle
# The Python object to be pickled
data = {'name': 'Alice', 'age': 30, 'cities': ['New York', 'London']}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
print('Pickling completed and saved to data.pkl')

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print('Unpickling completed.')
print('Original data:', data)
print('Loaded data:', loaded_data)
print('Are the objects identical?', data == loaded_data)

class session:
    def __init__(self, money, location, name):
        self.__money = money
        self._location = location
        self.name = name
    
    def session1(self):
        money_amount = self.__money
        return money_amount
    def session2(self):
        location_details = self.__location
        return location_details
    
session_obj = session(100,'india','sahoo')
# =============================================================================
# print(session_obj._location)
# 
# print(session_obj.session1())
# =============================================================================

# =============================================================================
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# =============================================================================
n = int(input())
student_dic = {}
for x in range(n):
    name, *line = input().split()
    student_dic[name]=line
    print(student_dic)
query_name = input()
scores = student_dic[query_name]
result = sum(scores)/len(scores)
print(result)
    
    


    
    






