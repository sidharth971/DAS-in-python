lst_data = [-4, -3, 0, 1, 2, 10]


def square_sort_1(lst):
    left = 0
    right = len(lst_data) - 1
    result = []

    while left < right:
        if abs(lst[left]) > abs(lst[right]):
            result.append(lst[left] ** 2)
            left += 1
        else:
            result.append(lst[right] ** 2)
            right -= 1

    return result


print(square_sort_1(lst_data))

# 1. Check if Array is Sorted
lst1 = [1, 2, 2, 3, 6]
lst2 = [1, 3, 2, 4]
def check_sorted(lst):
    if len(lst) < 2:
        return True

    left, right = 0, 1
    while right < len(lst) - 1:
        if lst[left] > lst[right]:
            return False
        left += 1
        right += 1

    return True


print(check_sorted(lst1))
print(check_sorted(lst2))

# 2. Reverse a List (Two-pointers swap)
def reverse(lst):
    if len(lst) < 2:
        return lst
    left, right = 0, len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst
print(reverse(lst1))

word = 'madam'
def pallindrum(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

print(pallindrum(word))

duplicate_lst = [1,1,2,2,2,3,4,4]
def remove_duplicate(lst):
    if not lst or len(lst) < 1:
        return lst

    i = 0
    for j in range(1, len(lst)):
        if lst[i] != lst[j]:
            i += 1
            lst[i] = lst[j]

    return lst[:i+1]
print(remove_duplicate(duplicate_lst))