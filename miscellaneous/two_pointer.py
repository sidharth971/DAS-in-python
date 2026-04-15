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

duplicate_lst = [1, 1, 2, 2, 2, 3, 4, 4]


def remove_duplicate(lst):
    if not lst or len(lst) < 1:
        return lst

    i = 0
    for j in range(1, len(lst)):
        if lst[i] != lst[j]:
            i += 1
            lst[i] = lst[j]

    return lst[:i + 1]


print(remove_duplicate(duplicate_lst))


# 5. Move Zeroes to End
def move_zeroes(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr


print('move_zeroes: ', move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print('move_zeroes: ', move_zeroes([0, 0, 1]))  # [1, 0, 0]
print('move_zeroes: ', move_zeroes([1, 2, 3]))  # [1,2,3]
print('move_zeroes: ', move_zeroes([0, 0, 0]))  # [0,0,0]


# 6. Find Pair With Given Sum (Sorted Array)
def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return False


print('has_pair_with_sum: ', has_pair_with_sum([1, 2, 3, 4, 6], 6))
print('has_pair_with_sum: ', has_pair_with_sum([1, 2, 3, 9], 8))


def find_difference_k(arr, k):
    i, j = 0, 1

    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k and i != j:
            return True
        elif diff < k:
            j += 1
        else:
            i += 1

        if i == j:
            j += 1
    return False

print('find_difference_k: ',find_difference_k([1, 3, 5, 8, 12], 7))  # True
print('find_difference_k: ',find_difference_k([1, 2, 3, 4, 5], 10)) # False

def three_sum(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left, right = i + 1, len(arr) - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
            elif target > total:
                right -= 1
            else:
                left += 1

    return result

print('three_sum: ', three_sum([-1,0,1,2,-1,-4], 0))

def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        w = right - left
        area = min(heights[left], heights[right]) * w
        max_area = max(area, max_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

print('max_area: ', max_area([1,8,6,2,5,4,8,3,7]))  # 49
print('max_area: ', max_area([1,1]))                # 1
print('max_area: ', max_area([4,3,2,1,4]))          # 16

def max_consecutive_ones(arr):
    max_counter = 0
    current = 0
    for x in arr:
        if x == 1:
            current += 1
            max_counter = max(max_counter, current)
        else:
            current = 0

    return max_counter

print('max_consecutive_ones: ', max_consecutive_ones([1, 1, 0, 1, 1, 1])) #3

