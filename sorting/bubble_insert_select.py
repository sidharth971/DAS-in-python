bubble_arr = [64, 34, 25, 12, 22, 11, 90]


def bubble(arr):
    flag, n = True, len(arr)
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = True


bubble(bubble_arr)
print('Bubble Sort ', bubble_arr)

insert_arr = [64, 34, 25, 12, 22, 11, 90]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


insertion_sort(insert_arr)
print('Insertion Sort ', insert_arr)

selection_arr = [64, 34, 25, 12, 22, 11, 90]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


selection_sort(selection_arr)
print('Selection Sort ', selection_arr)
