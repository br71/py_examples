def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return  array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# O(n^2) time | O(1) space
array = [8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(array))