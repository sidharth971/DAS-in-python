

def merge_sort(arr):
    n = len(arr)
    if n ==0 or n== 1:
        return arr
    m = n // 2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])

    sorted_arr = [0] * n
    i = l = r = 0
    l_len = len(L)
    r_len = len(R)

    while l<l_len and r<r_len:
        if L[l]<R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1

        i += 1

    while l<l_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r<r_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


count_st = [4, 2, 2, 8, 3, 3, 1]

def counting_sort(arr):
    max_no = max(arr)

    count = [0] * (max_no + 1)
    for num in arr:
        count[num] += 1

    i = 0
    for c in range(max_no + 1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1


counting_sort(count_st)
print(count_st)