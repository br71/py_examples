def bubble_sort(array):
    is_sorted = False
    # After firs iteration biggest number will be last
    # After second next to biggest will be second from end
    # Because that we shall not check ordered numbers at end
    # It is optimization T and S are same.
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                is_sorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# O(n^2) time | O(1) space

array = [8, 5, 2, 9, 5, 6, 3]

print(bubble_sort(array))
