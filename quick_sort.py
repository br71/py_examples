

# Recursion
# O(nLog(n) time | O(Log(n) space
def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)
    return array


def quick_sort_helper(array: object, start_idx, end_idx):

    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    # Moving pointers
    while right_idx >= left_idx:
        # In that case left and right index will be switched
        # Longer if is commented
        # if array[left_idx] > array[pivot_idx] and  array[right_idx] < array[pivot_idx]:
        if array[left_idx] > array[pivot_idx] > array[right_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1

    swap(pivot_idx, right_idx, array)

    # Choosing short subarray which will be sorted firs
    left_subarray_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)

    if left_subarray_smaller:
        quick_sort_helper((array, start_idx, right_idx - 1))
        quick_sort_helper(array, right_idx + 1, end_idx)
    else:
        quick_sort_helper(array, right_idx + 1, end_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


a = [8, 5, 2, 9, 5, 6, 3]

print(quick_sort(a))



