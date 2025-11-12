arr = [2, 4, 6, 8, 10, 12]


def binary_search(arr, target):
    right, left = len(arr) - 1, 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search(arr, 12))


def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, left, mid, target)
    else:
        return binary_search_recursive(arr, mid, right, target)


print(binary_search(arr, 8))


def first_occurance(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            result = mid
            left = mid + 1  # First or last occurance depends on here
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return result


print(first_occurance([1, 2, 2, 2, 3, 4], 2))


def search_insert(arr, element):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    arr.insert(left, element)
    return arr


print(search_insert([1, 3, 5, 6], 4))
